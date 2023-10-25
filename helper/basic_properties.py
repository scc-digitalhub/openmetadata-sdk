class BasicProperties:
    id: str
    name: str
    owner: str
    fully_qualified_name: str
    description: str
    display_name: str
    version: str
    updated_at: str
    updated_by: str
    service: str
    service_type: str
    message_schema: str
    partitions: str
    cleanup_policies: str
    sample_data: str
    tags: str
    domain: str

    def __init__(self,id= None,name= None,owner= None,description= None,display_name= None,tags= None,domain= None,) -> None:
        self.id = id
        self.name = name
        self.owner = owner
        self.description = description
        self.display_name = display_name
        self.tags = tags
        self.domain = domain