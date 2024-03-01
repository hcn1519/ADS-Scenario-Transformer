# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openscenario_msgs/common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from openscenario_msgs import boundingbox_pb2 as openscenario__msgs_dot_boundingbox__pb2
from openscenario_msgs import by_type_pb2 as openscenario__msgs_dot_by__type__pb2
from openscenario_msgs import directory_pb2 as openscenario__msgs_dot_directory__pb2
from openscenario_msgs import environment_pb2 as openscenario__msgs_dot_environment__pb2
from openscenario_msgs import file_pb2 as openscenario__msgs_dot_file__pb2
from openscenario_msgs import following_mode_pb2 as openscenario__msgs_dot_following__mode__pb2
from openscenario_msgs import parameter_pb2 as openscenario__msgs_dot_parameter__pb2
from openscenario_msgs import pedestrian_pb2 as openscenario__msgs_dot_pedestrian__pb2
from openscenario_msgs import position_pb2 as openscenario__msgs_dot_position__pb2
from openscenario_msgs import property_pb2 as openscenario__msgs_dot_property__pb2
from openscenario_msgs import route_pb2 as openscenario__msgs_dot_route__pb2
from openscenario_msgs import rule_pb2 as openscenario__msgs_dot_rule__pb2
from openscenario_msgs import shape_pb2 as openscenario__msgs_dot_shape__pb2
from openscenario_msgs import traffic_signal_pb2 as openscenario__msgs_dot_traffic__signal__pb2
from openscenario_msgs import vehicle_pb2 as openscenario__msgs_dot_vehicle__pb2
from openscenario_msgs import transition_dynamics_pb2 as openscenario__msgs_dot_transition__dynamics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eopenscenario_msgs/common.proto\x12\x0copenscenario\x1a#openscenario_msgs/boundingbox.proto\x1a\x1fopenscenario_msgs/by_type.proto\x1a!openscenario_msgs/directory.proto\x1a#openscenario_msgs/environment.proto\x1a\x1copenscenario_msgs/file.proto\x1a&openscenario_msgs/following_mode.proto\x1a!openscenario_msgs/parameter.proto\x1a\"openscenario_msgs/pedestrian.proto\x1a openscenario_msgs/position.proto\x1a openscenario_msgs/property.proto\x1a\x1dopenscenario_msgs/route.proto\x1a\x1copenscenario_msgs/rule.proto\x1a\x1dopenscenario_msgs/shape.proto\x1a&openscenario_msgs/traffic_signal.proto\x1a\x1fopenscenario_msgs/vehicle.proto\x1a+openscenario_msgs/transition_dynamics.proto\"~\n\x0cOpenScenario\x12,\n\nfileHeader\x18\x01 \x02(\x0b\x32\x18.openscenario.FileHeader\x12@\n\x14openScenarioCategory\x18\x02 \x02(\x0b\x32\".openscenario.OpenScenarioCategory\"c\n\nFileHeader\x12\x10\n\x08revMajor\x18\x01 \x02(\r\x12\x10\n\x08revMinor\x18\x02 \x02(\r\x12\x0c\n\x04\x64\x61te\x18\x03 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x02(\t\x12\x0e\n\x06\x61uthor\x18\x05 \x02(\t\"\x90\x01\n\x14OpenScenarioCategory\x12<\n\x12scenarioDefinition\x18\x01 \x02(\x0b\x32 .openscenario.ScenarioDefinition\x12:\n\x11\x63\x61talogDefinition\x18\x02 \x02(\x0b\x32\x1f.openscenario.CatalogDefinition\"\x99\x02\n\x12ScenarioDefinition\x12\x41\n\x15parameterDeclarations\x18\x01 \x03(\x0b\x32\".openscenario.ParameterDeclaration\x12\x38\n\x10\x63\x61talogLocations\x18\x02 \x02(\x0b\x32\x1e.openscenario.CatalogLocations\x12.\n\x0broadNetwork\x18\x03 \x02(\x0b\x32\x19.openscenario.RoadNetwork\x12(\n\x08\x65ntities\x18\x04 \x02(\x0b\x32\x16.openscenario.Entities\x12,\n\nstoryboard\x18\x05 \x02(\x0b\x32\x18.openscenario.Storyboard\"\x9f\x01\n\x0bRoadNetwork\x12%\n\tlogicFile\x18\x01 \x01(\x0b\x32\x12.openscenario.File\x12*\n\x0esceneGraphFile\x18\x02 \x01(\x0b\x32\x12.openscenario.File\x12=\n\x0etrafficSignals\x18\x03 \x03(\x0b\x32%.openscenario.TrafficSignalController\";\n\x11\x43\x61talogDefinition\x12&\n\x07\x63\x61talog\x18\x01 \x02(\x0b\x32\x15.openscenario.Catalog\"\xfe\x02\n\x07\x43\x61talog\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\'\n\x08vehicles\x18\x02 \x03(\x0b\x32\x15.openscenario.Vehicle\x12-\n\x0b\x63ontrollers\x18\x03 \x03(\x0b\x32\x18.openscenario.Controller\x12-\n\x0bpedestrians\x18\x04 \x03(\x0b\x32\x18.openscenario.Pedestrian\x12-\n\x0bmiscObjects\x18\x05 \x03(\x0b\x32\x18.openscenario.MiscObject\x12/\n\x0c\x65nvironments\x18\x06 \x03(\x0b\x32\x19.openscenario.Environment\x12)\n\tmaneuvers\x18\x07 \x03(\x0b\x32\x16.openscenario.Maneuver\x12.\n\x0ctrajectories\x18\x08 \x03(\x0b\x32\x18.openscenario.Trajectory\x12#\n\x06routes\x18\t \x03(\x0b\x32\x13.openscenario.Route\"\xe2\x02\n\x10\x43\x61talogLocations\x12<\n\x0evehicleCatalog\x18\x01 \x01(\x0b\x32$.openscenario.VehicleCatalogLocation\x12\x42\n\x11\x63ontrollerCatalog\x18\x02 \x01(\x0b\x32\'.openscenario.ControllerCatalogLocation\x12\x42\n\x11pedestrianCatalog\x18\x03 \x01(\x0b\x32\'.openscenario.PedestrianCatalogLocation\x12\x42\n\x11miscObjectCatalog\x18\x04 \x01(\x0b\x32\'.openscenario.MiscObjectCatalogLocation\x12\x44\n\x12\x65nvironmentCatalog\x18\x05 \x01(\x0b\x32(.openscenario.EnvironmentCatalogLocation\"D\n\x16VehicleCatalogLocation\x12*\n\tdirectory\x18\x01 \x02(\x0b\x32\x17.openscenario.Directory\"G\n\x19\x43ontrollerCatalogLocation\x12*\n\tdirectory\x18\x01 \x02(\x0b\x32\x17.openscenario.Directory\"G\n\x19PedestrianCatalogLocation\x12*\n\tdirectory\x18\x01 \x02(\x0b\x32\x17.openscenario.Directory\"G\n\x19MiscObjectCatalogLocation\x12*\n\tdirectory\x18\x01 \x02(\x0b\x32\x17.openscenario.Directory\"H\n\x1a\x45nvironmentCatalogLocation\x12*\n\tdirectory\x18\x01 \x02(\x0b\x32\x17.openscenario.Directory\"E\n\x17ManeuverCatalogLocation\x12*\n\tdirectory\x18\x01 \x02(\x0b\x32\x17.openscenario.Directory\"G\n\x19TrajectoryCatalogLocation\x12*\n\tdirectory\x18\x01 \x02(\x0b\x32\x17.openscenario.Directory\"B\n\x14RouteCatalogLocation\x12*\n\tdirectory\x18\x01 \x02(\x0b\x32\x17.openscenario.Directory\"\x80\x01\n\nStoryboard\x12 \n\x04init\x18\x01 \x02(\x0b\x32\x12.openscenario.Init\x12$\n\x07stories\x18\x02 \x03(\x0b\x32\x13.openscenario.Story\x12*\n\x0bstopTrigger\x18\x03 \x02(\x0b\x32\x15.openscenario.Trigger\"2\n\x04Init\x12*\n\x07\x61\x63tions\x18\x01 \x02(\x0b\x32\x19.openscenario.InitActions\"\xa6\x01\n\x0bInitActions\x12\x31\n\rglobalActions\x18\x01 \x03(\x0b\x32\x1a.openscenario.GlobalAction\x12;\n\x12userDefinedActions\x18\x02 \x03(\x0b\x32\x1f.openscenario.UserDefinedAction\x12\'\n\x08privates\x18\x03 \x03(\x0b\x32\x15.openscenario.Private\"g\n\x07Private\x12\'\n\tentityRef\x18\x01 \x02(\x0b\x32\x14.openscenario.Entity\x12\x33\n\x0eprivateActions\x18\x02 \x03(\x0b\x32\x1b.openscenario.PrivateAction\"z\n\x08\x45ntities\x12\x35\n\x0fscenarioObjects\x18\x01 \x03(\x0b\x32\x1c.openscenario.ScenarioObject\x12\x37\n\x10\x65ntitySelections\x18\x02 \x03(\x0b\x32\x1d.openscenario.EntitySelection\"\x89\x01\n\x11\x42yEntityCondition\x12<\n\x12triggeringEntities\x18\x01 \x02(\x0b\x32 .openscenario.TriggeringEntities\x12\x36\n\x0f\x65ntityCondition\x18\x02 \x02(\x0b\x32\x1d.openscenario.EntityCondition\"\xc6\x01\n\x12TriggeringEntities\x12W\n\x16triggeringEntitiesRule\x18\x01 \x02(\x0e\x32\x37.openscenario.TriggeringEntities.TriggeringEntitiesRule\x12+\n\nentityRefs\x18\x02 \x03(\x0b\x32\x17.openscenario.EntityRef\"*\n\x16TriggeringEntitiesRule\x12\x07\n\x03\x41LL\x10\x00\x12\x07\n\x03\x41NY\x10\x01\"\xd6\x04\n\x10\x42yValueCondition\x12<\n\x12parameterCondition\x18\x01 \x01(\x0b\x32 .openscenario.ParameterCondition\x12<\n\x12timeOfDayCondition\x18\x02 \x01(\x0b\x32 .openscenario.TimeOfDayCondition\x12\x46\n\x17simulationTimeCondition\x18\x03 \x01(\x0b\x32%.openscenario.SimulationTimeCondition\x12V\n\x1fstoryboardElementStateCondition\x18\x04 \x01(\x0b\x32-.openscenario.StoryboardElementStateCondition\x12J\n\x19userDefinedValueCondition\x18\x05 \x01(\x0b\x32\'.openscenario.UserDefinedValueCondition\x12\x44\n\x16trafficSignalCondition\x18\x06 \x01(\x0b\x32$.openscenario.TrafficSignalCondition\x12X\n trafficSignalControllerCondition\x18\x07 \x01(\x0b\x32..openscenario.TrafficSignalControllerCondition\x12:\n\x11variableCondition\x18\x08 \x01(\x0b\x32\x1f.openscenario.VariableCondition\"J\n\x17SimulationTimeCondition\x12 \n\x04rule\x18\x01 \x02(\x0e\x32\x12.openscenario.Rule\x12\r\n\x05value\x18\x02 \x02(\x01\"Z\n\x19UserDefinedValueCondition\x12\x0c\n\x04name\x18\x01 \x02(\t\x12 \n\x04rule\x18\x02 \x02(\x0e\x32\x12.openscenario.Rule\x12\r\n\x05value\x18\x03 \x02(\t\"\x13\n\x11VariableCondition\"\x14\n\x12TimeOfDayCondition\"\xa6\x01\n\x10\x43\x61talogReference\x12\x13\n\x0b\x63\x61talogName\x18\x01 \x02(\t\x12\x11\n\tentryName\x18\x02 \x02(\t\x12?\n\x14parameterAssignments\x18\x03 \x03(\x0b\x32!.openscenario.ParameterAssignment\x12)\n\x03ref\x18\x04 \x02(\x0b\x32\x1c.openscenario.CatalogElement\"\x9e\x03\n\x0e\x43\x61talogElement\x12<\n\x11\x63ontrollerVehicle\x18\x04 \x01(\x0b\x32\x1f.openscenario.ControllerVehicleH\x00\x12\x30\n\x0b\x65nvironment\x18\x05 \x01(\x0b\x32\x19.openscenario.EnvironmentH\x00\x12*\n\x08maneuver\x18\x06 \x01(\x0b\x32\x16.openscenario.ManeuverH\x00\x12.\n\nmiscObject\x18\x07 \x01(\x0b\x32\x18.openscenario.MiscObjectH\x00\x12.\n\npedestrian\x18\x08 \x01(\x0b\x32\x18.openscenario.PedestrianH\x00\x12$\n\x05route\x18\t \x01(\x0b\x32\x13.openscenario.RouteH\x00\x12.\n\ntrajectory\x18\n \x01(\x0b\x32\x18.openscenario.TrajectoryH\x00\x12(\n\x07vehicle\x18\x0b \x01(\x0b\x32\x15.openscenario.VehicleH\x00\x42\x10\n\x0eimplementation\"\x13\n\x11\x43ontrollerVehicle\"h\n\x08RouteRef\x12\"\n\x05route\x18\x01 \x01(\x0b\x32\x13.openscenario.Route\x12\x38\n\x10\x63\x61talogReference\x18\x02 \x01(\x0b\x32\x1e.openscenario.CatalogReference\"w\n\rTrajectoryRef\x12,\n\ntrajectory\x18\x01 \x02(\x0b\x32\x18.openscenario.Trajectory\x12\x38\n\x10\x63\x61talogReference\x18\x02 \x02(\x0b\x32\x1e.openscenario.CatalogReference\"\xf6\x01\n\x10\x43ontrollerAction\x12\x44\n\x16\x61ssignControllerAction\x18\x01 \x01(\x0b\x32$.openscenario.AssignControllerAction\x12R\n\x1doverrideControllerValueAction\x18\x02 \x01(\x0b\x32+.openscenario.OverrideControllerValueAction\x12H\n\x18\x61\x63tivateControllerAction\x18\x03 \x01(\x0b\x32&.openscenario.ActivateControllerAction\"\x8b\x02\n\x16\x41ssignControllerAction\x12\x17\n\x0f\x61\x63tivateLateral\x18\x01 \x02(\x08\x12\x18\n\x10\x61\x63tivateLighting\x18\x02 \x02(\x08\x12\x1c\n\x14\x61\x63tivateLongitudinal\x18\x03 \x02(\x08\x12,\n\ncontroller\x18\x04 \x02(\x0b\x32\x18.openscenario.Controller\x12\x38\n\x10\x63\x61talogReference\x18\x05 \x02(\x0b\x32\x1e.openscenario.CatalogReference\x12\x38\n\x10\x63ontrollerAction\x18\x06 \x02(\x0b\x32\x1e.openscenario.ControllerAction\"\x1f\n\x1dOverrideControllerValueAction\"\x1a\n\x18\x41\x63tivateControllerAction\"=\n\x0e\x43onditionGroup\x12+\n\nconditions\x18\x01 \x03(\x0b\x32\x17.openscenario.Condition\"\xa7\x02\n\tCondition\x12<\n\rconditionEdge\x18\x01 \x02(\x0e\x32%.openscenario.Condition.ConditionEdge\x12\r\n\x05\x64\x65lay\x18\x02 \x02(\x01\x12\x0c\n\x04name\x18\x03 \x02(\t\x12:\n\x11\x62yEntityCondition\x18\x04 \x01(\x0b\x32\x1f.openscenario.ByEntityCondition\x12\x38\n\x10\x62yValueCondition\x18\x05 \x01(\x0b\x32\x1e.openscenario.ByValueCondition\"I\n\rConditionEdge\x12\x0b\n\x07\x46\x41LLING\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\n\n\x06RISING\x10\x02\x12\x15\n\x11RISING_OR_FALLING\x10\x03\"\xc1\x01\n\nController\x12\x34\n\x0e\x63ontrollerType\x18\x01 \x01(\x0e\x32\x1c.openscenario.ControllerType\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x41\n\x15parameterDeclarations\x18\x03 \x03(\x0b\x32\".openscenario.ParameterDeclaration\x12,\n\nproperties\x18\x04 \x02(\x0b\x32\x18.openscenario.Properties\"z\n\x10ObjectController\x12\x38\n\x10\x63\x61talogReference\x18\x01 \x01(\x0b\x32\x1e.openscenario.CatalogReference\x12,\n\ncontroller\x18\x02 \x01(\x0b\x32\x18.openscenario.Controller\"\xb0\x01\n\x0c\x45ntityAction\x12*\n\tentityRef\x18\x01 \x02(\x0b\x32\x17.openscenario.EntityRef\x12\x36\n\x0f\x61\x64\x64\x45ntityAction\x18\x02 \x01(\x0b\x32\x1d.openscenario.AddEntityAction\x12<\n\x12\x64\x65leteEntityAction\x18\x03 \x01(\x0b\x32 .openscenario.DeleteEntityAction\"m\n\x0f\x41\x64\x64\x45ntityAction\x12(\n\x08position\x18\x01 \x02(\x0b\x32\x16.openscenario.Position\x12\x30\n\x0c\x65ntityAction\x18\x02 \x02(\x0b\x32\x1a.openscenario.EntityAction\"\x14\n\x12\x44\x65leteEntityAction\"\xf5\x06\n\x0f\x45ntityCondition\x12<\n\x12\x65ndOfRoadCondition\x18\x01 \x01(\x0b\x32 .openscenario.EndOfRoadCondition\x12<\n\x12\x63ollisionCondition\x18\x02 \x01(\x0b\x32 .openscenario.CollisionCondition\x12\x38\n\x10offroadCondition\x18\x03 \x01(\x0b\x32\x1e.openscenario.OffroadCondition\x12@\n\x14timeHeadwayCondition\x18\x04 \x01(\x0b\x32\".openscenario.TimeHeadwayCondition\x12H\n\x18timeToCollisionCondition\x18\x05 \x01(\x0b\x32&.openscenario.TimeToCollisionCondition\x12\x42\n\x15\x61\x63\x63\x65lerationCondition\x18\x06 \x01(\x0b\x32#.openscenario.AccelerationCondition\x12>\n\x13standStillCondition\x18\x07 \x01(\x0b\x32!.openscenario.StandStillCondition\x12\x34\n\x0espeedCondition\x18\x08 \x01(\x0b\x32\x1c.openscenario.SpeedCondition\x12\x44\n\x16relativeSpeedCondition\x18\t \x01(\x0b\x32$.openscenario.RelativeSpeedCondition\x12J\n\x19traveledDistanceCondition\x18\n \x01(\x0b\x32\'.openscenario.TraveledDistanceCondition\x12:\n\x11\x64istanceCondition\x18\x0b \x01(\x0b\x32\x1f.openscenario.DistanceCondition\x12J\n\x19relativeDistanceCondition\x18\x0c \x01(\x0b\x32\'.openscenario.RelativeDistanceCondition\x12L\n\x1arelativeClearanceCondition\x18\r \x01(\x0b\x32(.openscenario.RelativeClearanceCondition\"l\n\x12\x43ollisionCondition\x12*\n\tentityRef\x18\x01 \x02(\x0b\x32\x17.openscenario.EntityRef\x12*\n\x06\x62yType\x18\x02 \x02(\x0b\x32\x1a.openscenario.ByObjectType\"\xbc\x02\n\x14TimeHeadwayCondition\x12\x38\n\x10\x63oordinateSystem\x18\x01 \x01(\x0e\x32\x1e.openscenario.CoordinateSystem\x12*\n\tentityRef\x18\x02 \x02(\x0b\x32\x17.openscenario.EntityRef\x12\x11\n\tfreespace\x18\x03 \x02(\x08\x12@\n\x14relativeDistanceType\x18\x04 \x01(\x0e\x32\".openscenario.RelativeDistanceType\x12\x38\n\x10routingAlgorithm\x18\x05 \x02(\x0e\x32\x1e.openscenario.RoutingAlgorithm\x12 \n\x04rule\x18\x06 \x02(\x0e\x32\x12.openscenario.Rule\x12\r\n\x05value\x18\x07 \x02(\x01\"\x1a\n\x18TimeToCollisionCondition\"\x7f\n\x15\x41\x63\x63\x65lerationCondition\x12\x35\n\tdirection\x18\x01 \x01(\x0e\x32\".openscenario.DirectionalDimension\x12 \n\x04rule\x18\x02 \x02(\x0e\x32\x12.openscenario.Rule\x12\r\n\x05value\x18\x03 \x02(\x01\"\xaa\x01\n\x0eSpeedCondition\x12\x35\n\tdirection\x18\x01 \x01(\x0e\x32\".openscenario.DirectionalDimension\x12\x30\n\tcondition\x18\x02 \x02(\x0b\x32\x1d.openscenario.EntityCondition\x12 \n\x04rule\x18\x03 \x02(\x0e\x32\x12.openscenario.Rule\x12\r\n\x05value\x18\x04 \x02(\x01\"Y\n\x13StandStillCondition\x12\x10\n\x08\x64uration\x18\x01 \x02(\x01\x12\x30\n\tcondition\x18\x02 \x02(\x0b\x32\x1d.openscenario.EntityCondition\"\xe1\x01\n\x1aRelativeClearanceCondition\x12\x18\n\x10\x64istanceBackward\x18\x01 \x01(\x01\x12\x17\n\x0f\x64istanceForward\x18\x02 \x01(\x01\x12\x11\n\tfreeSpace\x18\x03 \x02(\x08\x12\x15\n\roppositeLanes\x18\x04 \x02(\x08\x12:\n\x11relativeLaneRange\x18\x05 \x03(\x0b\x32\x1f.openscenario.RelativeLaneRange\x12*\n\tentityRef\x18\x06 \x03(\x0b\x32\x17.openscenario.EntityRef\"-\n\x11RelativeLaneRange\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x05\x12\n\n\x02to\x18\x02 \x01(\x05\"\x8d\x02\n\x11\x44istanceCondition\x12\x38\n\x10\x63oordinateSystem\x18\x01 \x02(\x0e\x32\x1e.openscenario.CoordinateSystem\x12\x11\n\tfreespace\x18\x02 \x02(\x08\x12@\n\x14relativeDistanceType\x18\x03 \x02(\x0e\x32\".openscenario.RelativeDistanceType\x12\x38\n\x10routingAlgorithm\x18\x04 \x02(\x0e\x32\x1e.openscenario.RoutingAlgorithm\x12 \n\x04rule\x18\x05 \x02(\x0e\x32\x12.openscenario.Rule\x12\r\n\x05value\x18\x06 \x02(\x01\"\x14\n\x12\x45ndOfRoadCondition\"\x12\n\x10OffroadCondition\"\x18\n\x16RelativeSpeedCondition\"\x1b\n\x19TraveledDistanceCondition\"\x1b\n\x19RelativeDistanceCondition\"\xc2\x01\n\x06\x45ntity\x12\x38\n\x0f\x65ntitySelection\x18\x01 \x01(\x0b\x32\x1d.openscenario.EntitySelectionH\x00\x12\x36\n\x0escenarioObject\x18\x02 \x01(\x0b\x32\x1c.openscenario.ScenarioObjectH\x00\x12\x34\n\rspawnedObject\x18\x03 \x01(\x0b\x32\x1b.openscenario.SpawnedObjectH\x00\x42\x10\n\x0eimplementation\"\x8a\x01\n\x0eScenarioObject\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x30\n\x0c\x65ntityObject\x18\x02 \x02(\x0b\x32\x1a.openscenario.EntityObject\x12\x38\n\x10objectController\x18\x03 \x01(\x0b\x32\x1e.openscenario.ObjectController\"\xaa\x01\n\x0c\x45ntityObject\x12(\n\x07vehicle\x18\x01 \x01(\x0b\x32\x15.openscenario.VehicleH\x00\x12.\n\npedestrian\x18\x02 \x01(\x0b\x32\x18.openscenario.PedestrianH\x00\x12.\n\nmiscObject\x18\x03 \x01(\x0b\x32\x18.openscenario.MiscObjectH\x00\x42\x10\n\x0eimplementation\"4\n\tEntityRef\x12\'\n\tentityRef\x18\x01 \x02(\x0b\x32\x14.openscenario.Entity\"\x0f\n\rSpawnedObject\"P\n\x0f\x45ntitySelection\x12\x0c\n\x04name\x18\x01 \x02(\t\x12/\n\x07members\x18\x02 \x02(\x0b\x32\x1e.openscenario.SelectedEntities\"d\n\x10SelectedEntities\x12*\n\tentityRef\x18\x01 \x03(\x0b\x32\x17.openscenario.EntityRef\x12$\n\x06\x62yType\x18\x02 \x03(\x0b\x32\x14.openscenario.ByType\"\'\n\x17\x45xternalObjectReference\x12\x0c\n\x04name\x18\x01 \x02(\t\"\xb2\x01\n\x05\x45vent\x12\x1d\n\x15maximumExecutionCount\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12(\n\x08priority\x18\x03 \x02(\x0e\x32\x16.openscenario.Priority\x12%\n\x07\x61\x63tions\x18\x04 \x03(\x0b\x32\x14.openscenario.Action\x12+\n\x0cstartTrigger\x18\x05 \x01(\x0b\x32\x15.openscenario.Trigger\"@\n\x07Trigger\x12\x35\n\x0f\x63onditionGroups\x18\x01 \x03(\x0b\x32\x1c.openscenario.ConditionGroup\"\xb8\x01\n\x06\x41\x63tion\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x30\n\x0cglobalAction\x18\x02 \x01(\x0b\x32\x1a.openscenario.GlobalAction\x12:\n\x11userDefinedAction\x18\x03 \x01(\x0b\x32\x1f.openscenario.UserDefinedAction\x12\x32\n\rprivateAction\x18\x04 \x01(\x0b\x32\x1b.openscenario.PrivateAction\"\xa8\x02\n\x0cGlobalAction\x12:\n\x11\x65nvironmentAction\x18\x01 \x01(\x0b\x32\x1f.openscenario.EnvironmentAction\x12\x30\n\x0c\x65ntityAction\x18\x02 \x01(\x0b\x32\x1a.openscenario.EntityAction\x12@\n\x14infrastructureAction\x18\x03 \x01(\x0b\x32\".openscenario.InfrastructureAction\x12\x32\n\rtrafficAction\x18\x04 \x01(\x0b\x32\x1b.openscenario.TrafficAction\x12\x34\n\x0evariableAction\x18\x05 \x01(\x0b\x32\x1c.openscenario.VariableAction\"V\n\x14InfrastructureAction\x12>\n\x13trafficSignalAction\x18\x01 \x02(\x0b\x32!.openscenario.TrafficSignalAction\"\x13\n\x11\x45nvironmentAction\"\x0f\n\rTrafficAction\"\x10\n\x0eVariableAction\"\xc7\x01\n\rLateralAction\x12\x38\n\x10laneChangeAction\x18\x01 \x01(\x0b\x32\x1e.openscenario.LaneChangeAction\x12\x38\n\x10laneOffsetAction\x18\x02 \x01(\x0b\x32\x1e.openscenario.LaneOffsetAction\x12\x42\n\x15lateralDistanceAction\x18\x03 \x01(\x0b\x32#.openscenario.LateralDistanceAction\"\xaa\x01\n\x10LaneOffsetAction\x12\x12\n\ncontinuous\x18\x01 \x02(\x08\x12H\n\x18laneOffsetActionDynamics\x18\x02 \x02(\x0b\x32&.openscenario.LaneOffsetActionDynamics\x12\x38\n\x10laneOffsetTarget\x18\x03 \x02(\x0b\x32\x1e.openscenario.LaneOffsetTarget\"\xaa\x01\n\x10LaneChangeAction\x12\x18\n\x10targetLaneOffset\x18\x01 \x02(\x01\x12\x42\n\x18laneChangeActionDynamics\x18\x02 \x02(\x0b\x32 .openscenario.TransitionDynamics\x12\x38\n\x10laneChangeTarget\x18\x03 \x02(\x0b\x32\x1e.openscenario.LaneChangeTarget\"\x8e\x01\n\x10LaneChangeTarget\x12<\n\x12relativeTargetLane\x18\x01 \x01(\x0b\x32 .openscenario.RelativeTargetLane\x12<\n\x12\x61\x62soluteTargetLane\x18\x02 \x01(\x0b\x32 .openscenario.AbsoluteTargetLane\"O\n\x12RelativeTargetLane\x12*\n\tentityRef\x18\x01 \x02(\x0b\x32\x17.openscenario.EntityRef\x12\r\n\x05value\x18\x02 \x02(\x05\"#\n\x12\x41\x62soluteTargetLane\x12\r\n\x05value\x18\x01 \x02(\t\"\x1a\n\x18LaneOffsetActionDynamics\"\x12\n\x10LaneOffsetTarget\"\x17\n\x15LateralDistanceAction\"\xd0\x01\n\x12LongitudinalAction\x12.\n\x0bspeedAction\x18\x01 \x01(\x0b\x32\x19.openscenario.SpeedAction\x12L\n\x1alongitudinalDistanceAction\x18\x02 \x01(\x0b\x32(.openscenario.LongitudinalDistanceAction\x12<\n\x12speedProfileAction\x18\x03 \x01(\x0b\x32 .openscenario.SpeedProfileAction\"\x1c\n\x1aLongitudinalDistanceAction\"\xc8\x01\n\rManeuverGroup\x12\x1d\n\x15maximumExecutionCount\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12$\n\x06\x61\x63tors\x18\x03 \x02(\x0b\x32\x14.openscenario.Actors\x12\x39\n\x11\x63\x61talogReferences\x18\x04 \x03(\x0b\x32\x1e.openscenario.CatalogReference\x12)\n\tmaneuvers\x18\x05 \x03(\x0b\x32\x16.openscenario.Maneuver\"W\n\x06\x41\x63tors\x12 \n\x18selectTriggeringEntities\x18\x01 \x02(\x08\x12+\n\nentityRefs\x18\x02 \x03(\x0b\x32\x17.openscenario.EntityRef\"\x80\x01\n\x08Maneuver\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x41\n\x15parameterDeclarations\x18\x02 \x03(\x0b\x32\".openscenario.ParameterDeclaration\x12#\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x13.openscenario.Event\"\xaa\x05\n\nMiscObject\x12=\n\x12miscObjectCategory\x18\x01 \x02(\x0e\x32!.openscenario.MiscObject.Category\x12\x0f\n\x07model3d\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x02(\t\x12\x41\n\x15parameterDeclarations\x18\x04 \x03(\x0b\x32\".openscenario.ParameterDeclaration\x12.\n\x0b\x62oundingBox\x18\x05 \x02(\x0b\x32\x19.openscenario.BoundingBox\x12,\n\nproperties\x18\x06 \x02(\x0b\x32\x18.openscenario.Properties\"\x9c\x03\n\x08\x43\x61tegory\x12\x14\n\x10\x43\x41TEGORY_BARRIER\x10\x00\x12\x15\n\x11\x43\x41TEGORY_BUILDING\x10\x01\x12\x16\n\x12\x43\x41TEGORY_CROSSWALK\x10\x02\x12\x13\n\x0f\x43\x41TEGORY_GANTRY\x10\x03\x12\x11\n\rCATEGORY_NONE\x10\x04\x12\x15\n\x11\x43\x41TEGORY_OBSTACLE\x10\x05\x12\x1a\n\x16\x43\x41TEGORY_PARKING_SPACE\x10\x06\x12\x12\n\x0e\x43\x41TEGORY_PATCH\x10\x07\x12\x11\n\rCATEGORY_POLE\x10\x08\x12\x14\n\x10\x43\x41TEGORY_RAILING\x10\t\x12\x16\n\x12\x43\x41TEGORY_ROAD_MARK\x10\n\x12\x1a\n\x16\x43\x41TEGORY_SOUND_BARRIER\x10\x0b\x12\x18\n\x14\x43\x41TEGORY_STREET_LAMP\x10\x0c\x12\x1b\n\x17\x43\x41TEGORY_TRAFFIC_ISLAND\x10\r\x12\x11\n\rCATEGORY_TREE\x10\x0e\x12\x17\n\x13\x43\x41TEGORY_VEGETATION\x10\x0f\x12\x1c\n\x18\x43\x41TEGORY_WIND_DEPRECATED\x10\x10\"\xd5\x03\n\rPrivateAction\x12<\n\x12longitudinalAction\x18\x01 \x01(\x0b\x32 .openscenario.LongitudinalAction\x12\x32\n\rlateralAction\x18\x02 \x01(\x0b\x32\x1b.openscenario.LateralAction\x12\x38\n\x10visibilityAction\x18\x03 \x01(\x0b\x32\x1e.openscenario.VisibilityAction\x12:\n\x11synchronizeAction\x18\x04 \x01(\x0b\x32\x1f.openscenario.SynchronizeAction\x12\x38\n\x10\x63ontrollerAction\x18\x05 \x01(\x0b\x32\x1e.openscenario.ControllerAction\x12\x34\n\x0eteleportAction\x18\x06 \x01(\x0b\x32\x1c.openscenario.TeleportAction\x12\x32\n\rroutingAction\x18\x07 \x01(\x0b\x32\x1b.openscenario.RoutingAction\x12\x38\n\x10\x61ppearanceAction\x18\x08 \x01(\x0b\x32\x1e.openscenario.AppearanceAction\":\n\x0eTeleportAction\x12(\n\x08position\x18\x01 \x02(\x0b\x32\x16.openscenario.Position\"\x12\n\x10VisibilityAction\"\x13\n\x11SynchronizeAction\"\x11\n\x0f\x41nimationAction\"\x12\n\x10\x41ppearanceAction\"\xd5\x01\n\rRoutingAction\x12:\n\x11\x61ssignRouteAction\x18\x01 \x01(\x0b\x32\x1f.openscenario.AssignRouteAction\x12\x44\n\x16\x66ollowTrajectoryAction\x18\x02 \x01(\x0b\x32$.openscenario.FollowTrajectoryAction\x12\x42\n\x15\x61\x63quirePositionAction\x18\x03 \x01(\x0b\x32#.openscenario.AcquirePositionAction\"\xa2\x01\n\x11\x41ssignRouteAction\x12\"\n\x05route\x18\x01 \x02(\x0b\x32\x13.openscenario.Route\x12\x38\n\x10\x63\x61talogReference\x18\x02 \x02(\x0b\x32\x1e.openscenario.CatalogReference\x12/\n\x06\x61\x63tion\x18\x03 \x02(\x0b\x32\x1f.openscenario.AssignRouteAction\"d\n\x16\x46ollowTrajectoryAction\x12\x1d\n\x15initialDistanceOffset\x18\x01 \x02(\x01\x12+\n\x06\x61\x63tion\x18\x02 \x02(\x0b\x32\x1b.openscenario.RoutingAction\"u\n\x15\x41\x63quirePositionAction\x12(\n\x08position\x18\x01 \x02(\x0b\x32\x16.openscenario.Position\x12\x32\n\rroutingAction\x18\x02 \x02(\x0b\x32\x1b.openscenario.RoutingAction\"\x88\x01\n\x0bSpeedAction\x12=\n\x13speedActionDynamics\x18\x01 \x02(\x0b\x32 .openscenario.TransitionDynamics\x12:\n\x11speedActionTarget\x18\x02 \x02(\x0b\x32\x1f.openscenario.SpeedActionTarget\"\x93\x01\n\x11SpeedActionTarget\x12>\n\x13relativeTargetSpeed\x18\x01 \x02(\x0b\x32!.openscenario.RelativeTargetSpeed\x12>\n\x13\x61\x62soluteTargetSpeed\x18\x02 \x02(\x0b\x32!.openscenario.AbsoluteTargetSpeed\"\xa6\x01\n\x13RelativeTargetSpeed\x12\x12\n\ncontinuous\x18\x01 \x02(\x08\x12*\n\tentityRef\x18\x02 \x02(\x0b\x32\x17.openscenario.EntityRef\x12@\n\x14speedTargetValueType\x18\x03 \x02(\x0e\x32\".openscenario.SpeedTargetValueType\x12\r\n\x05value\x18\x04 \x02(\x01\"$\n\x13\x41\x62soluteTargetSpeed\x12\r\n\x05value\x18\x01 \x02(\x01\"\x14\n\x12SpeedProfileAction\"\x9d\x02\n\x11StoryboardElement\x12 \n\x03\x61\x63t\x18\x0c \x01(\x0b\x32\x11.openscenario.ActH\x00\x12&\n\x06\x61\x63tion\x18\r \x01(\x0b\x32\x14.openscenario.ActionH\x00\x12$\n\x05\x65vent\x18\x0e \x01(\x0b\x32\x13.openscenario.EventH\x00\x12*\n\x08maneuver\x18\x0f \x01(\x0b\x32\x16.openscenario.ManeuverH\x00\x12\x34\n\rmaneuverGroup\x18\x10 \x01(\x0b\x32\x1b.openscenario.ManeuverGroupH\x00\x12$\n\x05story\x18\x11 \x01(\x0b\x32\x13.openscenario.StoryH\x00\x42\x10\n\x0eimplementation\"y\n\x05Story\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x41\n\x15parameterDeclarations\x18\x02 \x03(\x0b\x32\".openscenario.ParameterDeclaration\x12\x1f\n\x04\x61\x63ts\x18\x03 \x03(\x0b\x32\x11.openscenario.Act\"\xa1\x01\n\x03\x41\x63t\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x33\n\x0emaneuverGroups\x18\x02 \x03(\x0b\x32\x1b.openscenario.ManeuverGroup\x12+\n\x0cstartTrigger\x18\x03 \x02(\x0b\x32\x15.openscenario.Trigger\x12*\n\x0bstopTrigger\x18\x04 \x01(\x0b\x32\x15.openscenario.Trigger\"\xe4\x03\n\x1fStoryboardElementStateCondition\x12\x42\n\x05state\x18\x01 \x02(\x0e\x32\x33.openscenario.StoryboardElementStateCondition.State\x12=\n\x14storyboardElementRef\x18\x02 \x02(\x0b\x32\x1f.openscenario.StoryboardElement\x12Q\n\x15storyboardElementType\x18\x03 \x02(\x0e\x32\x32.openscenario.StoryboardElementStateCondition.Type\"\x95\x01\n\x05State\x12\x12\n\x0e\x43OMPLETE_STATE\x10\x00\x12\x12\n\x0e\x45ND_TRANSITION\x10\x01\x12\x11\n\rRUNNING_STATE\x10\x02\x12\x13\n\x0fSKIP_TRANSITION\x10\x03\x12\x11\n\rSTANDBY_STATE\x10\x04\x12\x14\n\x10START_TRANSITION\x10\x05\x12\x13\n\x0fSTOP_TRANSITION\x10\x06\"S\n\x04Type\x12\x07\n\x03\x41\x43T\x10\x00\x12\n\n\x06\x41\x43TION\x10\x01\x12\t\n\x05\x45VENT\x10\x02\x12\x0c\n\x08MANEUVER\x10\x03\x12\x12\n\x0eMANEUVER_GROUP\x10\x04\x12\t\n\x05STORY\x10\x05\"M\n\x17TrajectoryFollowingMode\x12\x32\n\rfollowingMode\x18\x01 \x02(\x0e\x32\x1b.openscenario.FollowingMode\"\x91\x01\n\nTrajectory\x12\x0e\n\x06\x63losed\x18\x01 \x02(\x08\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x41\n\x15parameterDeclarations\x18\x03 \x03(\x0b\x32\".openscenario.ParameterDeclaration\x12\"\n\x05shape\x18\x04 \x02(\x0b\x32\x13.openscenario.Shape\"S\n\x11UserDefinedAction\x12>\n\x13\x63ustomCommandAction\x18\x01 \x02(\x0b\x32!.openscenario.CustomCommandAction\"4\n\x13\x43ustomCommandAction\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x02(\t*\xdc\x01\n\x0e\x43ontrollerType\x12\x1a\n\x16\x43ONTROLLERTYPE_LATERAL\x10\x00\x12\x1f\n\x1b\x43ONTROLLERTYPE_LONGITUDINAL\x10\x01\x12\x1b\n\x17\x43ONTROLLERTYPE_LIGHTING\x10\x02\x12\x1c\n\x18\x43ONTROLLERTYPE_ANIMATION\x10\x03\x12\x1b\n\x17\x43ONTROLLERTYPE_MOVEMENT\x10\x04\x12\x1d\n\x19\x43ONTROLLERTYPE_APPEARANCE\x10\x05\x12\x16\n\x12\x43ONTROLLERTYPE_ALL\x10\x06*B\n\x10\x43oordinateSystem\x12\n\n\x06\x45NTITY\x10\x00\x12\x08\n\x04LANE\x10\x01\x12\x08\n\x04ROAD\x10\x02\x12\x0e\n\nTRAJECTORY\x10\x03*\xb9\x01\n\x14RelativeDistanceType\x12 \n\x1cRELATIVEDISTANCETYPE_LATERAL\x10\x00\x12%\n!RELATIVEDISTANCETYPE_LONGITUDINAL\x10\x01\x12+\n\'RELATIVEDISTANCETYPE_CARTESIAN_DISTANCE\x10\x02\x12+\n\'RELATIVEDISTANCETYPE_EUCLIDIAN_DISTANCE\x10\x03*i\n\x10RoutingAlgorithm\x12\x12\n\x0e\x41SSIGNED_ROUTE\x10\x00\x12\x0b\n\x07\x46\x41STEST\x10\x01\x12\x17\n\x13LEAST_INTERSECTIONS\x10\x02\x12\x0c\n\x08SHORTEST\x10\x03\x12\r\n\tUNDEFINED\x10\x04*\x82\x01\n\x14\x44irectionalDimension\x12%\n!DIRECTIONALDIMENSION_LONGITUDINAL\x10\x00\x12 \n\x1c\x44IRECTIONALDIMENSION_LATERAL\x10\x01\x12!\n\x1d\x44IRECTIONALDIMENSION_VERTICAL\x10\x02*?\n\x08Priority\x12\r\n\tOVERWRITE\x10\x00\x12\x0c\n\x08OVERRIDE\x10\x01\x12\x0c\n\x08PARALLEL\x10\x02\x12\x08\n\x04SKIP\x10\x03*W\n\x14SpeedTargetValueType\x12\x1e\n\x1aSPEEDTARGETVALUETYPE_DELTA\x10\x00\x12\x1f\n\x1bSPEEDTARGETVALUETYPE_FACTOR\x10\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'openscenario_msgs.common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONTROLLERTYPE._serialized_start=16439
  _CONTROLLERTYPE._serialized_end=16659
  _COORDINATESYSTEM._serialized_start=16661
  _COORDINATESYSTEM._serialized_end=16727
  _RELATIVEDISTANCETYPE._serialized_start=16730
  _RELATIVEDISTANCETYPE._serialized_end=16915
  _ROUTINGALGORITHM._serialized_start=16917
  _ROUTINGALGORITHM._serialized_end=17022
  _DIRECTIONALDIMENSION._serialized_start=17025
  _DIRECTIONALDIMENSION._serialized_end=17155
  _PRIORITY._serialized_start=17157
  _PRIORITY._serialized_end=17220
  _SPEEDTARGETVALUETYPE._serialized_start=17222
  _SPEEDTARGETVALUETYPE._serialized_end=17309
  _OPENSCENARIO._serialized_start=609
  _OPENSCENARIO._serialized_end=735
  _FILEHEADER._serialized_start=737
  _FILEHEADER._serialized_end=836
  _OPENSCENARIOCATEGORY._serialized_start=839
  _OPENSCENARIOCATEGORY._serialized_end=983
  _SCENARIODEFINITION._serialized_start=986
  _SCENARIODEFINITION._serialized_end=1267
  _ROADNETWORK._serialized_start=1270
  _ROADNETWORK._serialized_end=1429
  _CATALOGDEFINITION._serialized_start=1431
  _CATALOGDEFINITION._serialized_end=1490
  _CATALOG._serialized_start=1493
  _CATALOG._serialized_end=1875
  _CATALOGLOCATIONS._serialized_start=1878
  _CATALOGLOCATIONS._serialized_end=2232
  _VEHICLECATALOGLOCATION._serialized_start=2234
  _VEHICLECATALOGLOCATION._serialized_end=2302
  _CONTROLLERCATALOGLOCATION._serialized_start=2304
  _CONTROLLERCATALOGLOCATION._serialized_end=2375
  _PEDESTRIANCATALOGLOCATION._serialized_start=2377
  _PEDESTRIANCATALOGLOCATION._serialized_end=2448
  _MISCOBJECTCATALOGLOCATION._serialized_start=2450
  _MISCOBJECTCATALOGLOCATION._serialized_end=2521
  _ENVIRONMENTCATALOGLOCATION._serialized_start=2523
  _ENVIRONMENTCATALOGLOCATION._serialized_end=2595
  _MANEUVERCATALOGLOCATION._serialized_start=2597
  _MANEUVERCATALOGLOCATION._serialized_end=2666
  _TRAJECTORYCATALOGLOCATION._serialized_start=2668
  _TRAJECTORYCATALOGLOCATION._serialized_end=2739
  _ROUTECATALOGLOCATION._serialized_start=2741
  _ROUTECATALOGLOCATION._serialized_end=2807
  _STORYBOARD._serialized_start=2810
  _STORYBOARD._serialized_end=2938
  _INIT._serialized_start=2940
  _INIT._serialized_end=2990
  _INITACTIONS._serialized_start=2993
  _INITACTIONS._serialized_end=3159
  _PRIVATE._serialized_start=3161
  _PRIVATE._serialized_end=3264
  _ENTITIES._serialized_start=3266
  _ENTITIES._serialized_end=3388
  _BYENTITYCONDITION._serialized_start=3391
  _BYENTITYCONDITION._serialized_end=3528
  _TRIGGERINGENTITIES._serialized_start=3531
  _TRIGGERINGENTITIES._serialized_end=3729
  _TRIGGERINGENTITIES_TRIGGERINGENTITIESRULE._serialized_start=3687
  _TRIGGERINGENTITIES_TRIGGERINGENTITIESRULE._serialized_end=3729
  _BYVALUECONDITION._serialized_start=3732
  _BYVALUECONDITION._serialized_end=4330
  _SIMULATIONTIMECONDITION._serialized_start=4332
  _SIMULATIONTIMECONDITION._serialized_end=4406
  _USERDEFINEDVALUECONDITION._serialized_start=4408
  _USERDEFINEDVALUECONDITION._serialized_end=4498
  _VARIABLECONDITION._serialized_start=4500
  _VARIABLECONDITION._serialized_end=4519
  _TIMEOFDAYCONDITION._serialized_start=4521
  _TIMEOFDAYCONDITION._serialized_end=4541
  _CATALOGREFERENCE._serialized_start=4544
  _CATALOGREFERENCE._serialized_end=4710
  _CATALOGELEMENT._serialized_start=4713
  _CATALOGELEMENT._serialized_end=5127
  _CONTROLLERVEHICLE._serialized_start=5129
  _CONTROLLERVEHICLE._serialized_end=5148
  _ROUTEREF._serialized_start=5150
  _ROUTEREF._serialized_end=5254
  _TRAJECTORYREF._serialized_start=5256
  _TRAJECTORYREF._serialized_end=5375
  _CONTROLLERACTION._serialized_start=5378
  _CONTROLLERACTION._serialized_end=5624
  _ASSIGNCONTROLLERACTION._serialized_start=5627
  _ASSIGNCONTROLLERACTION._serialized_end=5894
  _OVERRIDECONTROLLERVALUEACTION._serialized_start=5896
  _OVERRIDECONTROLLERVALUEACTION._serialized_end=5927
  _ACTIVATECONTROLLERACTION._serialized_start=5929
  _ACTIVATECONTROLLERACTION._serialized_end=5955
  _CONDITIONGROUP._serialized_start=5957
  _CONDITIONGROUP._serialized_end=6018
  _CONDITION._serialized_start=6021
  _CONDITION._serialized_end=6316
  _CONDITION_CONDITIONEDGE._serialized_start=6243
  _CONDITION_CONDITIONEDGE._serialized_end=6316
  _CONTROLLER._serialized_start=6319
  _CONTROLLER._serialized_end=6512
  _OBJECTCONTROLLER._serialized_start=6514
  _OBJECTCONTROLLER._serialized_end=6636
  _ENTITYACTION._serialized_start=6639
  _ENTITYACTION._serialized_end=6815
  _ADDENTITYACTION._serialized_start=6817
  _ADDENTITYACTION._serialized_end=6926
  _DELETEENTITYACTION._serialized_start=6928
  _DELETEENTITYACTION._serialized_end=6948
  _ENTITYCONDITION._serialized_start=6951
  _ENTITYCONDITION._serialized_end=7836
  _COLLISIONCONDITION._serialized_start=7838
  _COLLISIONCONDITION._serialized_end=7946
  _TIMEHEADWAYCONDITION._serialized_start=7949
  _TIMEHEADWAYCONDITION._serialized_end=8265
  _TIMETOCOLLISIONCONDITION._serialized_start=8267
  _TIMETOCOLLISIONCONDITION._serialized_end=8293
  _ACCELERATIONCONDITION._serialized_start=8295
  _ACCELERATIONCONDITION._serialized_end=8422
  _SPEEDCONDITION._serialized_start=8425
  _SPEEDCONDITION._serialized_end=8595
  _STANDSTILLCONDITION._serialized_start=8597
  _STANDSTILLCONDITION._serialized_end=8686
  _RELATIVECLEARANCECONDITION._serialized_start=8689
  _RELATIVECLEARANCECONDITION._serialized_end=8914
  _RELATIVELANERANGE._serialized_start=8916
  _RELATIVELANERANGE._serialized_end=8961
  _DISTANCECONDITION._serialized_start=8964
  _DISTANCECONDITION._serialized_end=9233
  _ENDOFROADCONDITION._serialized_start=9235
  _ENDOFROADCONDITION._serialized_end=9255
  _OFFROADCONDITION._serialized_start=9257
  _OFFROADCONDITION._serialized_end=9275
  _RELATIVESPEEDCONDITION._serialized_start=9277
  _RELATIVESPEEDCONDITION._serialized_end=9301
  _TRAVELEDDISTANCECONDITION._serialized_start=9303
  _TRAVELEDDISTANCECONDITION._serialized_end=9330
  _RELATIVEDISTANCECONDITION._serialized_start=9332
  _RELATIVEDISTANCECONDITION._serialized_end=9359
  _ENTITY._serialized_start=9362
  _ENTITY._serialized_end=9556
  _SCENARIOOBJECT._serialized_start=9559
  _SCENARIOOBJECT._serialized_end=9697
  _ENTITYOBJECT._serialized_start=9700
  _ENTITYOBJECT._serialized_end=9870
  _ENTITYREF._serialized_start=9872
  _ENTITYREF._serialized_end=9924
  _SPAWNEDOBJECT._serialized_start=9926
  _SPAWNEDOBJECT._serialized_end=9941
  _ENTITYSELECTION._serialized_start=9943
  _ENTITYSELECTION._serialized_end=10023
  _SELECTEDENTITIES._serialized_start=10025
  _SELECTEDENTITIES._serialized_end=10125
  _EXTERNALOBJECTREFERENCE._serialized_start=10127
  _EXTERNALOBJECTREFERENCE._serialized_end=10166
  _EVENT._serialized_start=10169
  _EVENT._serialized_end=10347
  _TRIGGER._serialized_start=10349
  _TRIGGER._serialized_end=10413
  _ACTION._serialized_start=10416
  _ACTION._serialized_end=10600
  _GLOBALACTION._serialized_start=10603
  _GLOBALACTION._serialized_end=10899
  _INFRASTRUCTUREACTION._serialized_start=10901
  _INFRASTRUCTUREACTION._serialized_end=10987
  _ENVIRONMENTACTION._serialized_start=10989
  _ENVIRONMENTACTION._serialized_end=11008
  _TRAFFICACTION._serialized_start=11010
  _TRAFFICACTION._serialized_end=11025
  _VARIABLEACTION._serialized_start=11027
  _VARIABLEACTION._serialized_end=11043
  _LATERALACTION._serialized_start=11046
  _LATERALACTION._serialized_end=11245
  _LANEOFFSETACTION._serialized_start=11248
  _LANEOFFSETACTION._serialized_end=11418
  _LANECHANGEACTION._serialized_start=11421
  _LANECHANGEACTION._serialized_end=11591
  _LANECHANGETARGET._serialized_start=11594
  _LANECHANGETARGET._serialized_end=11736
  _RELATIVETARGETLANE._serialized_start=11738
  _RELATIVETARGETLANE._serialized_end=11817
  _ABSOLUTETARGETLANE._serialized_start=11819
  _ABSOLUTETARGETLANE._serialized_end=11854
  _LANEOFFSETACTIONDYNAMICS._serialized_start=11856
  _LANEOFFSETACTIONDYNAMICS._serialized_end=11882
  _LANEOFFSETTARGET._serialized_start=11884
  _LANEOFFSETTARGET._serialized_end=11902
  _LATERALDISTANCEACTION._serialized_start=11904
  _LATERALDISTANCEACTION._serialized_end=11927
  _LONGITUDINALACTION._serialized_start=11930
  _LONGITUDINALACTION._serialized_end=12138
  _LONGITUDINALDISTANCEACTION._serialized_start=12140
  _LONGITUDINALDISTANCEACTION._serialized_end=12168
  _MANEUVERGROUP._serialized_start=12171
  _MANEUVERGROUP._serialized_end=12371
  _ACTORS._serialized_start=12373
  _ACTORS._serialized_end=12460
  _MANEUVER._serialized_start=12463
  _MANEUVER._serialized_end=12591
  _MISCOBJECT._serialized_start=12594
  _MISCOBJECT._serialized_end=13276
  _MISCOBJECT_CATEGORY._serialized_start=12864
  _MISCOBJECT_CATEGORY._serialized_end=13276
  _PRIVATEACTION._serialized_start=13279
  _PRIVATEACTION._serialized_end=13748
  _TELEPORTACTION._serialized_start=13750
  _TELEPORTACTION._serialized_end=13808
  _VISIBILITYACTION._serialized_start=13810
  _VISIBILITYACTION._serialized_end=13828
  _SYNCHRONIZEACTION._serialized_start=13830
  _SYNCHRONIZEACTION._serialized_end=13849
  _ANIMATIONACTION._serialized_start=13851
  _ANIMATIONACTION._serialized_end=13868
  _APPEARANCEACTION._serialized_start=13870
  _APPEARANCEACTION._serialized_end=13888
  _ROUTINGACTION._serialized_start=13891
  _ROUTINGACTION._serialized_end=14104
  _ASSIGNROUTEACTION._serialized_start=14107
  _ASSIGNROUTEACTION._serialized_end=14269
  _FOLLOWTRAJECTORYACTION._serialized_start=14271
  _FOLLOWTRAJECTORYACTION._serialized_end=14371
  _ACQUIREPOSITIONACTION._serialized_start=14373
  _ACQUIREPOSITIONACTION._serialized_end=14490
  _SPEEDACTION._serialized_start=14493
  _SPEEDACTION._serialized_end=14629
  _SPEEDACTIONTARGET._serialized_start=14632
  _SPEEDACTIONTARGET._serialized_end=14779
  _RELATIVETARGETSPEED._serialized_start=14782
  _RELATIVETARGETSPEED._serialized_end=14948
  _ABSOLUTETARGETSPEED._serialized_start=14950
  _ABSOLUTETARGETSPEED._serialized_end=14986
  _SPEEDPROFILEACTION._serialized_start=14988
  _SPEEDPROFILEACTION._serialized_end=15008
  _STORYBOARDELEMENT._serialized_start=15011
  _STORYBOARDELEMENT._serialized_end=15296
  _STORY._serialized_start=15298
  _STORY._serialized_end=15419
  _ACT._serialized_start=15422
  _ACT._serialized_end=15583
  _STORYBOARDELEMENTSTATECONDITION._serialized_start=15586
  _STORYBOARDELEMENTSTATECONDITION._serialized_end=16070
  _STORYBOARDELEMENTSTATECONDITION_STATE._serialized_start=15836
  _STORYBOARDELEMENTSTATECONDITION_STATE._serialized_end=15985
  _STORYBOARDELEMENTSTATECONDITION_TYPE._serialized_start=15987
  _STORYBOARDELEMENTSTATECONDITION_TYPE._serialized_end=16070
  _TRAJECTORYFOLLOWINGMODE._serialized_start=16072
  _TRAJECTORYFOLLOWINGMODE._serialized_end=16149
  _TRAJECTORY._serialized_start=16152
  _TRAJECTORY._serialized_end=16297
  _USERDEFINEDACTION._serialized_start=16299
  _USERDEFINEDACTION._serialized_end=16382
  _CUSTOMCOMMANDACTION._serialized_start=16384
  _CUSTOMCOMMANDACTION._serialized_end=16436
# @@protoc_insertion_point(module_scope)
