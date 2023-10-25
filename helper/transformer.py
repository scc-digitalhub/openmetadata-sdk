from metadata.generated.schema.entity.data.table import (
    Column,
    DataType,
)
from metadata.generated.schema.type.basic import (
    Markdown
)

def from_dict_to_columns(list_columns: []):
    """
    List of dictionaries with the following keys:
    - "name" : name of the column
    - "type": type of the column values between: int,string,str,boolean,bool,array,list,[],char,float
    - "description": description of the column 
    the values of the dictionary are string
    """
    result = []
    for column_ in list_columns:
        column  = create_column(column_)
        result.append(column)
    return result

def create_column(column_dict: dict):
    """
    Given a dictionary retun the Column object
    currently support the following parameter:
    - name
    - type
    - description
    """
    name = None
    type_ = None
    description = None
    tags = None
    glossary = None
    for key in column_dict:
        #  print(key)
        if key=="name":
            name = column_dict[key]
        if key == "type":
            if column_dict[key] == "int":
                type_ = DataType.INT
            elif column_dict[key] == "string" or column_dict[key] == "str":
                type_ = DataType.STRING
            elif column_dict[key] == "boolean" or column_dict[key] == "bool":
                type_ = DataType.BOOLEAN
            elif column_dict[key] == "array" or column_dict[key] == "list" or column_dict[key] == "[]":
                type_ = DataType.ARRAY
            elif column_dict[key] == "char":
                type_ = DataType.CHAR
            elif column_dict[key] == "float":
                type_ = DataType.FLOAT
            else:
                t = column_dict[key]
                error_s = f"type provided: '{t}' is not supported! Try to use one of the supported types."
                raise(Exception(error_s))
            # if column_dict[key] == "":
            #     type_ = DataType.
        if key == "description":
            description = Markdown(__root__=column_dict[key])
        if key == "tags":
            pass
    return Column(name=name,dataType=type_,description=description)