from typing import Any
from helper.basic_properties import BasicProperties
from helper.openMetaData import MetaDataServer
from metadata.generated.schema.api.services.createDatabaseService import (
    CreateDatabaseServiceRequest,
)
from metadata.generated.schema.entity.services.databaseService import (
    DatabaseService,
    DatabaseServiceType,
    DatabaseConnection,
)
from metadata.generated.schema.entity.services.connections.database.postgresConnection import (
    PostgresConnection
)
from metadata.generated.schema.entity.services.connections.database.datalakeConnection import (
    DatalakeConnection,
    LocalConfig
)
from metadata.generated.schema.entity.services.connections.database.datalake.s3Config import (
    S3Config
)
from metadata.generated.schema.security.credentials.awsCredentials import(
    AWSCredentials
)
from metadata.generated.schema.entity.services.connections.database.mysqlConnection import (
    MysqlConnection,
)

from metadata.generated.schema.api.data.createDatabase import (
    CreateDatabaseRequest,
)
from metadata.generated.schema.api.data.createDatabaseSchema import (
    CreateDatabaseSchemaRequest,
)
from metadata.generated.schema.api.data.createTable import CreateTableRequest
from helper.transformer import from_dict_to_columns
from enum import Enum

class DbType(Enum):
    POSTGRES = 1
    S3 = 2
    MYSQL = 3

class TableCustom(BasicProperties):
    openMetadata: MetaDataServer
    service: Any
    database: CreateDatabaseRequest
    company_name: str
    schema: CreateDatabaseSchemaRequest

    def __init__(self,openMetadata: MetaDataServer= None) -> None:
        """
        Initialize the TableCustom entity check the BasicProperty

        :param openMetadata: it's the metadataserver MetaDataServer() object if it is not initialize an exception will be raised 
        """
        if openMetadata == None:
            raise Exception("No MetaDataServer was provided! Cannot initialize the entity!")
        self.openMetadata = openMetadata

    def ingest_data(self,type_db: DbType,company_name: str,database_name: str,schema_name: str,table_name: str,columns: []):
        """
        Send to the server the table provided

        :param type_db: It's the type of db that we want to create DbType
        :param company_name: it's going be the service name in the metadata, the service name will be the same as the company_name
        :param database_name: The name of the database inside the service
        :param schema_name: The name of the schema inside the database
        :param table_name: Tha name of the table inside the schema
        :param columns: List of dictionaries with the following keys {"name":"name","type":"int","description":"Description"} type of the column values between: int,string,str,boolean,bool,array,list,[],char,float
        """
        if type_db.value == DbType.POSTGRES.value:
            self.create_service_postgres(company_name=company_name)
        elif type_db.value == DbType.S3.value:
            self.create_service_s3(company_name=company_name)
        elif type_db.value == DbType.MYSQL.value:
            self.create_service(company_name=company_name)
        else:
            e = f"Database type provided: {type_db.name} is not valid or supported!"
            raise(Exception(e))
        self.create_db(database_name)
        self.create_schema(schema_name)
        self.create_table(table_name,columns)

    def create_service(self,company_name: str):
        """
        Create the service for MySql
        :param company_name: the name of the service or company
        """
        self.company_name = company_name
        if self.openMetadata.metadata.health_check():
            create_service = CreateDatabaseServiceRequest(
                name=company_name,
                serviceType=DatabaseServiceType.Mysql,
                connection=DatabaseConnection(
                    config=MysqlConnection(
                        username="username",
                        #password="password",
                        hostPort="http://localhost:1234",
                    )
                ),
            )
            self.service = self.openMetadata.metadata.create_or_update(data=create_service)
        else:
            print("Error openMetadata is not running!")

    def create_service_postgres(self,company_name: str):
        """
        Create the service for the postgres server
        :param company_name: the name of the service or company
        """
        self.company_name = company_name
        if self.openMetadata.metadata.health_check():
            create_service = CreateDatabaseServiceRequest(
            name=company_name,
            serviceType=DatabaseServiceType.Postgres,
            connection=DatabaseConnection(
                config=PostgresConnection(
                    username="",
                    # type=PostgresType.Postgres,
                    database="",
                    # password="password",
                    # authType= BasicAuth(password="admin"),
                    hostPort="",
                    )
                ),
            )
            self.service = self.openMetadata.metadata.create_or_update(data=create_service)
        else:
            print("Error openMetadata is not running!")
    
    def create_service_s3(self,company_name: str):
        """
        Create the service for the s3 server
        :param company_name: the name of the service or company
        """
        self.company_name = company_name
        if self.openMetadata.metadata.health_check():
            create_service = CreateDatabaseServiceRequest(
            name=company_name,
            serviceType=DatabaseServiceType.Datalake,
            connection=DatabaseConnection(
                config=DatalakeConnection(
                    configSource= S3Config(securityConfig=AWSCredentials(awsRegion="Europe")) # LocalConfig()
                    )
                ),
            )
            self.service = self.openMetadata.metadata.create_or_update(data=create_service)
        else:
            print("Error openMetadata is not running!")

    def create_db(self,name_db: str):
        """
        Create the database inside the service
        :param name_db: the name of the database
        """
        create_db = CreateDatabaseRequest(
            name=name_db,
            service=self.company_name,
            )
        # print(create_db)
        self.database =self.openMetadata.metadata.create_or_update(data=create_db)
    
    def create_schema(self,name_schema: str):
        """
        Create the database inside the database
        :param name_schema: the name of the schema
        """
        create_schema = CreateDatabaseSchemaRequest(
            name=name_schema,
            database=self.database.fullyQualifiedName
        )
        self.schema = self.openMetadata.metadata.create_or_update(data=create_schema)

    def create_table(self,name_table: str, listColumn = []):
        """
        Create the table inside the schema
        :param name_table: the name of the table
        :param listColumn: list of dictionaries {"name":"name","type":"int","description":"Description",...} 
        """
        create_table = CreateTableRequest(
            name=name_table,
            databaseSchema=self.schema.fullyQualifiedName,
            columns= from_dict_to_columns(listColumn), # [Column(name="id", dataType=DataType.BIGINT)]
        )
        table_entity = self.openMetadata.metadata.create_or_update(create_table)

    def get_service(self,company_name: str):
        pass