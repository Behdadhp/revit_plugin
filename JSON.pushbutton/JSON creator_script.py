"""Converting a model to JSON"""

__title__ = "3DToJSON"
__author__ = "Behdad Hajipour"

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = __revit__.ActiveUIDocument.Document

wall_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType()

total_volume = 0.0

for wall in wall_collector:
    vol_param = wall.LookupP arameter("Volume")
    if vol_param:
        total_volume += vol_param.AsDouble()

print ("Total volume is {}".format(total_volume))
