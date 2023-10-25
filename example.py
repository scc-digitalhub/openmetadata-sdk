from helper.openMetaData import MetaDataServer
from entities_connectors.table import (TableCustom,DbType)
token = "eyJraWQiOiJHYjM4OWEtOWY3Ni1nZGpzLWE5MmotMDI0MmJrOTQzNTYiLCJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJvcGVuLW1ldGFkYXRhLm9yZyIsInN1YiI6ImFhYWFhYWFhYSIsImVtYWlsIjoiYWFhYWFhYWFhQGFhYWFhYWFhYS5pdCIsImlzQm90Ijp0cnVlLCJ0b2tlblR5cGUiOiJCT1QiLCJpYXQiOjE2OTU3MTQ1NTgsImV4cCI6bnVsbH0.lrOqjrBeADyFr5VOStQXpoPcXYm8w0nfPwptBirVdHjYBufnf-qIppPGh6uSUguoPAfnsMOFUyIUJbfanEez3H43w_Wewg9LjZuYkJi8Zh94euy5s3nVq_tXIQpZoE9UJl0QdQJtJV4e66Imr0S8sW-2XB_AheBWf_MJnI76HlyLHafSl_9k5_Iru9GFTF97GWPSlUY-fNuP8cVUKcLs3gITLMyLcupf_Cej2PgTqjaABjZRM23joKKLa2qyfqj0XjAVa1eh4LbK9AWpJvGU_NiXj_4PjyRKE7VCCksiR3pEqetyJy-G1sWaDJIsRrM0Gi8ZVc6F_GB8xxpxjG7Jag"
host = "http://localhost:8585/api"
authProv = "openmetadata"
metaData = MetaDataServer(token=token,host=host,authProvider=authProv) 
table = TableCustom(metaData)
table.id= "dafrsnfrghsehshsh"
table.fully_qualified_name = "fully-qualified-custom-name"
table.name = "this-is-my-name"
table.owner = "owner-name"
table.ingest_data(DbType.POSTGRES,"the-company-3","db_loot","schema-first","comm",[{"name":"id","type":"int"},{"name":"position","type":"int"},{"name":"comment","type":"string","description":"This is the description"}])
# table.create_service_postgres("my-company-1")
# table.create_db("DATABASEEE")
# table.create_schema("SCHEMA_FOR_TABLE")
# table.create_table("table-name",[{"name":"id","type":"int"},{"name":"position","type":"int"},{"name":"comment","type":"string","description":"This is the description"}])
# table.ingest_data()