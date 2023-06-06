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

import json

doc = __revit__.ActiveUIDocument.Document


class Calc:
    """This class initialises with the type of components.
    At the moment the type of Wall, Roofbase and Floor is supported."""

    def __init__(self, type):
        self.type = type

    def filer_parts(self):
        """Collects the elements and filters by them types"""

        if self.type == Wall:
            return FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).ToElements()
        elif self.type == Floor:
            return FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).ToElements()
        elif self.type == RoofBase:
            return FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Roofs).ToElements()

    def get_items(self):
        """Checks if every item is instance of required type."""

        elements = []
        for item in self.filer_parts():
            if isinstance(item, self.type):
                el = doc.GetElement(item.Id)
                elements.append(el)
        return elements

    def get_element(self):
        """Loops through all items.
        if the item is instance of Wall, should be filtered for just outer walls.
        but if the item is not instance of wall, it will be return just the value of get_items()"""

        list_of_components = []
        if isinstance(self.type, Wall):
            for item in self.get_items():
                if item.Name == "Aussenwand":
                    list_of_components.append(doc.GetElement(item.Id))
        else:
            list_of_components.append(doc.GetElement(self.get_items()[0].Id))
        return list_of_components

    def get_area(self):
        """Calculates the total area of selected component"""

        total_area = 0
        for item in self.get_element():
            area = item.LookupParameter("Area").AsDouble()
            total_area += self.converts_to_squaremeters(area)
        return total_area

    @staticmethod
    def converts_to_squaremeters(area):
        """converts the value to Square Meter"""

        return UnitUtils.ConvertFromInternalUnits(area, UnitTypeId.SquareMeters)

    def get_compound_structor(self):
        """Gets the structor of compound"""

        element_type = doc.GetElement(self.get_element()[0].GetTypeId())
        return element_type.GetCompoundStructure()

    @staticmethod
    def converts_to_millimeters(feet):
        """converts the value to Millimeter"""

        return UnitUtils.ConvertFromInternalUnits(feet, UnitTypeId.Millimeters)

    def get_thickness(self, layer):
        """Calculates width of each element"""

        width = self.get_compound_structor().GetLayerWidth(layer)
        return self.converts_to_millimeters(width)

    def create_dict(self, components):
        """Adds the final result to dict"""
        material_list = []
        material_dict = {}

        # Layers are getting an ID from inside to outside.
        roofbase_counter = self.get_compound_structor().LayerCount
        wall_floor_counter = 1

        # loops through all layers and add its name and thickness to the dict
        for layer in range(self.get_compound_structor().LayerCount):
            material_id = self.get_compound_structor().GetMaterialId(layer)
            material = doc.GetElement(material_id)

            material_list.append({material.Name: {"thickness": round(self.get_thickness(layer)),
                                                  "id": roofbase_counter if self.type == RoofBase else wall_floor_counter
                                                  }})
            roofbase_counter -= 1
            wall_floor_counter += 1
        # Adds the area of each component to the dict
        material_list.append({"area": "%.2f" % self.get_area()})

        # updates the material_dict with the list created as material_list
        for item in material_list:
            material_dict.update(item)

        components[self.type.__name__.lower()] = material_dict

        return components


def show_components():
    """Creates the final dict"""

    components = {}
    types = [Wall, Floor, RoofBase]
    for type in types:
        json_dict = Calc(type).create_dict(components)

    return json.dumps(json_dict)


print(show_components())
