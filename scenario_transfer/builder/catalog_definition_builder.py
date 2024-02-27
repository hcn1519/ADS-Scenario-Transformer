from openscenario_msgs import CatalogDefinition, Catalog
from scenario_transfer.builder import Builder


class CatalogDefinitionBuilder(Builder):
    """
    message CatalogDefinition {
        required Catalog catalog = 1;  // 1..1
    }
    """

    def __init__(self):
        pass

    def get_result(self) -> CatalogDefinition:
        return CatalogDefinition(catalog=Catalog())
