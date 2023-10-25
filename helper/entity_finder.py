from typing import Any
from entities_connectors.chart import Chart
from entities_connectors.container import Container
from helper import basic_properties


class EntityFinder:
    entity: Any
    # entity: Any | Chart | Container
    def __init__(self,entity_value,basicProperty: basic_properties) -> None:
        if entity_value == "chart":
            self.entity =  Chart(basicProperty)
        elif entity_value == "container":
            self.entity =  Container(basicProperty)
        else:
            pass
