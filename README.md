# openmetadata-sdk
This project is used as a python library to ingest data to a openmetadata server

## Install the requirements
To install the dependencies
```
python3 -m pip install -r requirements.txt
```
Notice that the client (this library) and the server(Openmetadata) must have the same version. So when installing the requirements in the requirements.txt is it possible to modify the version of openemetadata-ingestion dependency. When installing the openmetada from the https://docs.open-metadata.org/v1.1.x/quick-start it is possible to check the version

## Usage
The main use of this library is to create a MetadataServer object this object will be used as a connector to openmetadata host, in particular the MetadataServer takes 3 aguments token for the autentication, host is the ip to the openmetadata while authprovider is the provider for the token,
this parameters can be read from the environment variables when they are not explicit. If there is no environments varible an exception will be thrown.
```
The three environment variable are:

OPEN_META_DATA_TOKEN
OPEN_META_DATA_HOST
OPEN_META_DATA_AUTH_PROV
```
```
metaData = MetaDataServer(token,host,authProvider) 
table = TableCustom(metaData)
```
Then there is going to be the entity that we want to create, (table only supported for now). The entity will need the MetaDataServer as a parameter, then each entity might have custom fields. But in order to ingest the data each entity has to call the method:
```
ingest_data(self,...)
```
which will be pushing the entity to the metadata server, each ingest_data() will have some specific parameters.
