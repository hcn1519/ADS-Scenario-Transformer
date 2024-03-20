import unittest
import yaml
from openscenario_msgs import Actors, Condition, ByEntityCondition, Rule, LanePosition, Position, DirectionalDimension, RelativeDistanceType, CoordinateSystem, RoutingAlgorithm
from openscenario_msgs.parameter_pb2 import ParameterDeclaration, ParameterType
from scenario_transfer.builder.entities_builder import EntityType, EntitiesBuilder
from scenario_transfer.builder.story_board.by_entity_condition_builder import ByEntityConditionBuilder
from scenario_transfer.builder.story_board.by_value_condition_builder import ByValueConditionBuilder


class TestConditionBuilder(unittest.TestCase):

    def setUp(self):
        input_dir = "./tests/data/"
        self.route_file_path = input_dir + "openscenario_route.yaml"
        builder = EntitiesBuilder(entities=[
            EntityType.NPC, EntityType.NPC, EntityType.EGO,
            EntityType.PEDESTRIAN, EntityType.NPC
        ])
        self.entities = builder.get_result()
        self.ego_name = self.entities.scenarioObjects[0].name

    def test_entity_condition_builder_collision(self):

        colliding_npc_name = self.entities.scenarioObjects[1].name

        builder = ByEntityConditionBuilder(triggering_entity=self.ego_name)
        builder.make_collision_condition(
            colliding_entity_name=colliding_npc_name)
        by_entity_condition = builder.get_result()

        assert by_entity_condition is not None
        assert by_entity_condition.triggeringEntities.entityRefs[
            0].entityRef == "ego"
        assert by_entity_condition.entityCondition.collisionCondition is not None
        assert by_entity_condition.entityCondition.collisionCondition.entityRef.entityRef == "npc_1"

    def test_entity_condition_builder_acceleration(self):

        builder = ByEntityConditionBuilder(triggering_entity=self.ego_name)
        builder.make_acceleration_condition(value_in_ms=10,
                                            rule=Rule.GREATER_THAN)
        by_entity_condition = builder.get_result()

        assert by_entity_condition is not None
        assert by_entity_condition.triggeringEntities.entityRefs[
            0].entityRef == "ego"
        assert by_entity_condition.entityCondition.accelerationCondition.value == 10.0
        assert by_entity_condition.entityCondition.accelerationCondition.rule == Rule.GREATER_THAN

    def test_entity_condition_builder_speed(self):

        builder = ByEntityConditionBuilder(triggering_entity=self.ego_name)
        builder.make_speed_condition(
            direction=DirectionalDimension.DIRECTIONALDIMENSION_LONGITUDINAL, 
            value_in_ms=0.001, 
            rule=Rule.GREATER_THAN)
        by_entity_condition = builder.get_result()

        assert by_entity_condition is not None
        assert by_entity_condition.triggeringEntities.entityRefs[
            0].entityRef == "ego"

        speed_condition = by_entity_condition.entityCondition.speedCondition
        assert speed_condition.value == 0.001
        assert speed_condition.rule == Rule.GREATER_THAN
        assert speed_condition.direction == DirectionalDimension.DIRECTIONALDIMENSION_LONGITUDINAL

    def test_entity_condition_builder_stand_still(self):

        builder = ByEntityConditionBuilder(triggering_entity=self.ego_name)
        builder.make_stand_still_condition(duration_in_sec=3)
        by_entity_condition = builder.get_result()

        assert by_entity_condition is not None
        assert by_entity_condition.triggeringEntities.entityRefs[
            0].entityRef == "ego"
        assert by_entity_condition.entityCondition.standStillCondition.duration == 3

    def test_entity_condition_builder_reach_position(self):

        lane_position = LanePosition(laneId="154", s=10.9835, offset=-0.5042)

        builder = ByEntityConditionBuilder(triggering_entity=self.ego_name)
        builder.make_reach_position_condition(
            tolerance=1, position=Position(lanePosition=lane_position))
        by_entity_condition = builder.get_result()

        assert by_entity_condition is not None
        assert by_entity_condition.triggeringEntities.entityRefs[
            0].entityRef == "ego"
        assert by_entity_condition.entityCondition.reachPositionCondition.position.lanePosition.laneId == "154"

    # def make_distance_condition(self, 
    #     coordinateSystem: CoordinateSystem,
    #     freespace: bool,
    #     relativeDistanceType: RelativeDistanceType,
    #     routingAlgorithm: RoutingAlgorithm,
    #     value_in_meter: float,
    #     rule: Rule,
    #     position: Position):
        
    def test_entity_condition_builder_distance(self):

        lane_position = LanePosition(laneId="154", s=10.9835, offset=-0.5042)

        builder = ByEntityConditionBuilder(triggering_entity=self.ego_name)
        builder.make_distance_condition(
            coordinateSystem=CoordinateSystem.LANE,
            freespace=True,
            relativeDistanceType = RelativeDistanceType.
            RELATIVEDISTANCETYPE_LATERAL,
            routingAlgorithm=RoutingAlgorithm.SHORTEST,
            value_in_meter=5,
            rule=Rule.LESS_THAN,
            position=Position(lanePosition=lane_position))
        by_entity_condition = builder.get_result()

        assert by_entity_condition is not None
        assert by_entity_condition.triggeringEntities.entityRefs[
            0].entityRef == "ego"
        assert by_entity_condition.entityCondition.distanceCondition.position.lanePosition.laneId == "154"
        assert by_entity_condition.entityCondition.distanceCondition.value == 5

    def test_entity_condition_builder_time_headway(self):

        headway_npc_name = self.entities.scenarioObjects[1].name

        builder = ByEntityConditionBuilder(triggering_entity=self.ego_name)
        builder.make_time_headway_condition(
            coordinateSystem=CoordinateSystem.LANE,
            entity_name=headway_npc_name,
            relativeDistanceType = RelativeDistanceType.
            RELATIVEDISTANCETYPE_LATERAL,
            rule=Rule.GREATER_THAN,
            value_in_sec=3)
        by_entity_condition = builder.get_result()

        assert by_entity_condition is not None
        assert by_entity_condition.triggeringEntities.entityRefs[
            0].entityRef == "ego"
        assert by_entity_condition.entityCondition.timeHeadwayCondition.value == 3
        assert by_entity_condition.entityCondition.timeHeadwayCondition.entityRef == headway_npc_name

    def test_entity_condition_builder_relative_distance(self):

        target_npc_name = self.entities.scenarioObjects[1].name

        builder = ByEntityConditionBuilder(triggering_entity=self.ego_name)
        builder.make_relative_distance_condition(
            entity_name=target_npc_name,
            relativeDistanceType=RelativeDistanceType.
            RELATIVEDISTANCETYPE_LATERAL,
            value_in_meter=5,
            freespace=True,
            rule=Rule.GREATER_THAN)
        by_entity_condition = builder.get_result()

        assert by_entity_condition is not None
        assert by_entity_condition.triggeringEntities.entityRefs[
            0].entityRef == "ego"
        assert by_entity_condition.entityCondition.relativeDistanceCondition.value == 5
        assert by_entity_condition.entityCondition.relativeDistanceCondition.entityRef == target_npc_name

    def test_value_condition_builder_parameter(self):
        
        builder = ByValueConditionBuilder()
        builder.make_parameter_condition(
            parameter_declaration=ParameterDeclaration(name="param", parameterType=ParameterType.PARAMETERTYPE_INT, value="1", constraintGroups=[]), 
            rule=Rule.GREATER_THAN, 
            value="condition_value")

        by_value_condition = builder.get_result()
        assert by_value_condition is not None

        declaration = by_value_condition.parameterCondition.parameterRef
        assert declaration.name == "param"
        assert declaration.parameterType == ParameterType.PARAMETERTYPE_INT