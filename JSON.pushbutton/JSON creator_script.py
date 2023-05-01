"""Converting a model to JSON"""

__title__ = "3DToJSON"
__author__ = "Behdad Hajipour"

from Autodesk.Revit.DB import (
    FilteredElementCollector,
    BuiltInCategory,
    Wall,
    Floor,
    RoofBase,
    UnitUtils,
    UnitTypeId,
)

doc = __revit__.ActiveUIDocument.Document


class Calc:

    def __init__(self, type):
        self.type = type

    def filer_parts(self):
        """Collects the elements by their type"""

        if self.type == Wall:
            return FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).ToElements()
        elif self.type == Floor:
            return FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).ToElements()
        elif self.type == RoofBase:
            return FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Roofs).ToElements()

    def get_items(self):
        """Checks if every item is instance of required type"""

        elements = []
        for item in self.filer_parts():
            if isinstance(item, self.type):
                el = doc.GetElement(item.Id)
                elements.append(el)
        return elements

    def get_element(self):
        """Gets the required wall"""

        for el in self.get_items():
            if el.Name == "Aussenwand":
                return doc.GetElement(el.Id)
        return doc.GetElement(self.get_items()[0].Id)

    def get_compound_structor(self):
        """Gets the structor of compound"""

        element_type = doc.GetElement(self.get_element().GetTypeId())
        return element_type.GetCompoundStructure()

    def feet_to_cm(self, feet):
        """Changes feet to cm"""

        return UnitUtils.ConvertFromInternalUnits(feet, UnitTypeId.Millimeters)

    def get_thickness(self, layer):
        """Calculates width of each element"""

        width = self.get_compound_structor().GetLayerWidth(layer)
        return self.feet_to_cm(width)

    def create_dict(self, components):
        """Adds the final result to dict"""

        for layer in range(self.get_compound_structor().LayerCount):
            material_id = self.get_compound_structor().GetMaterialId(layer)
            material = doc.GetElement(material_id)
            components[self.type.__name__.lower()].append({material.MaterialCategory: round(self.get_thickness(layer))})

        return components


def show_components():
    """Creates the final dict"""

    components = {
        "wall": [],
        "roofbase": [],
        "floor": [],
    }
    parts = [Wall, Floor, RoofBase]
    for part in parts:
        result_dict = CalcAttr(part).create_dict(components)

    return result_dict


print(show_components())
