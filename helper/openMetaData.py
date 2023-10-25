from metadata.ingestion.ometa.ometa_api import OpenMetadata
from metadata.generated.schema.entity.services.connections.metadata.openMetadataConnection import (
    OpenMetadataConnection,
)
from metadata.generated.schema.security.client.openMetadataJWTClientConfig import (
    OpenMetadataJWTClientConfig
)
import os

from constants.environment import TOKEN,HOST,AUTH_PROV

class MetaDataServer:
    token: str
    host: str
    auth_prov: str
    server_config: OpenMetadataConnection
    metadata: OpenMetadata

    def __init__(self,token=None,host= None,authProvider=None):
        """
        Initialize the OpenMetaData collector
        """
        if token == None or host== None or authProvider == None:
            token,host,authProvider = self.load_data_from_env()
        self.token = token
        self.auth_prov = authProvider
        self.host = host
        jwtConfig = OpenMetadataJWTClientConfig(jwtToken=token)
        self.server_config = OpenMetadataConnection(hostPort=host,authProvider=authProvider, securityConfig=jwtConfig)
        self.metadata = OpenMetadata(self.server_config)
    
    def load_data_from_env(self):
        """
        TODO Load automatically the resources from the environment 
        """
        token = os.getenv(TOKEN)
        host = os.getenv(HOST)
        authProv = os.getenv(AUTH_PROV)
        if token== None or host == None or authProv == None or token=="" or host =="" or authProv=="":
            s = "Configurations from the environment for openmetadata not provided! Provide the three env variable: (OPEN_META_DATA_TOKEN,OPEN_META_DATA_HOST,OPEN_META_DATA_AUTH_PROV) or set though coding while initalizing the MetaDataServer"
            raise(Exception(s))
        # token = "eyJraWQiOiJHYjM4OWEtOWY3Ni1nZGpzLWE5MmotMDI0MmJrOTQzNTYiLCJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJvcGVuLW1ldGFkYXRhLm9yZyIsInN1YiI6ImFhYWFhYWFhYSIsImVtYWlsIjoiYWFhYWFhYWFhQGFhYWFhYWFhYS5pdCIsImlzQm90Ijp0cnVlLCJ0b2tlblR5cGUiOiJCT1QiLCJpYXQiOjE2OTU3MTQ1NTgsImV4cCI6bnVsbH0.lrOqjrBeADyFr5VOStQXpoPcXYm8w0nfPwptBirVdHjYBufnf-qIppPGh6uSUguoPAfnsMOFUyIUJbfanEez3H43w_Wewg9LjZuYkJi8Zh94euy5s3nVq_tXIQpZoE9UJl0QdQJtJV4e66Imr0S8sW-2XB_AheBWf_MJnI76HlyLHafSl_9k5_Iru9GFTF97GWPSlUY-fNuP8cVUKcLs3gITLMyLcupf_Cej2PgTqjaABjZRM23joKKLa2qyfqj0XjAVa1eh4LbK9AWpJvGU_NiXj_4PjyRKE7VCCksiR3pEqetyJy-G1sWaDJIsRrM0Gi8ZVc6F_GB8xxpxjG7Jag"
        # host = "http://localhost:8585/api"
        # authProv = "openmetadata"
        return token,host,authProv