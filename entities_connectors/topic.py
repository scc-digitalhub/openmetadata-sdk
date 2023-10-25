from helper.basic_properties import BasicProperties
from helper.openMetaData import MetaDataServer
from metadata.generated.schema.api.services.createMetadataService import (
    CreateMetadataServiceRequest
)
# from metadata.generated.schema.api.services. import (
#     CreateMetadataServiceRequest
# )
from metadata.generated.schema.entity.data.topic import (
    Topic
)
from metadata.generated.schema.api.data.createTopic import (
    CreateTopicRequest
)
from metadata.generated.schema.type.basic import (Uuid,UUID,EntityName,FullyQualifiedEntityName)
from metadata.generated.schema.type.entityReference import (EntityReference)

class TopicCustom(BasicProperties):
    openMetadata: MetaDataServer

    def __init__(self,openMetadata: MetaDataServer= None) -> None:
        if openMetadata == None:
            pass
        self.openMetadata = openMetadata
        

    def ingest_data(self, openMetadata: MetaDataServer = None):
        """
        Ingest data for the specific entity to metadata,
        it is possible to pass a new MetadataServer
        """
        if openMetadata == None:
            openMetadata = self.openMetadata
        #service_custom = CreateMetadataServiceRequest()
        # service_custom = CreateMetadataServiceRequest(self.name,"self.display_name","self.description",serviceType=openMetadata.auth_prov,connection=openMetadata.metadata,owner=self.owner)
        uiid = UUID('{12345678-1234-5678-1234-567812345678}')
        id_ = Uuid(__root__=uiid)
        # entity = EntityReference(id=id_,type="topic-type")
        # topic_to_send = Topic(id=id_,name=self.name,partitions=2454363,service=entity, fullyQualifiedName=self.fully_qualified_name,) # owner=self.owner
        name_request = EntityName(__root__="sdasdad3f4gef2rf4fewaegh4hyq35")
        fully_qualy = FullyQualifiedEntityName(__root__="abaco")
        request = CreateTopicRequest(name=name_request,service=fully_qualy,partitions=2321)
        entity_generated = openMetadata.metadata.create_or_update(data=request)
        print(f"entity: {entity_generated}")