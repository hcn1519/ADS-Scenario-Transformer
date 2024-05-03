from pathlib import Path
import pytest
from ads_scenario_transformer.transformer.scenario_transformer import ScenarioTransformer, ScenarioTransformerConfiguration
from ads_scenario_transformer.openscenario import OpenScenarioEncoder
from ads_scenario_transformer.tools.error import InvalidScenarioInputError


def test_invalid_scenario_input(borregas_vector_map_path,
                                borregas_apollo_map_path,
                                borregas_doppel_scenario160_path):

    configuration = ScenarioTransformerConfiguration(
        apollo_scenario_path=borregas_doppel_scenario160_path,
        apollo_hd_map_path=borregas_apollo_map_path,
        vector_map_path=borregas_vector_map_path,
        road_network_lanelet_map_path=
        "/home/sora/Desktop/changnam/autoware_map/borregasave_map/lanelet2_map.osm",
        obstacle_waypoint_frequency_in_sec=2,
        use_last_position_as_destination=True)

    with pytest.raises(InvalidScenarioInputError) as excinfo:
        transformer = ScenarioTransformer(configuration=configuration)

    assert "No localization poses found in scenario" in str(excinfo.value)


def test_scenario_transformer(borregas_doppel_scenario9_path,
                              borregas_vector_map_path,
                              borregas_apollo_map_path):

    configuration = ScenarioTransformerConfiguration(
        apollo_scenario_path=borregas_doppel_scenario9_path,
        apollo_hd_map_path=borregas_apollo_map_path,
        vector_map_path=borregas_vector_map_path,
        road_network_lanelet_map_path=
        "/home/sora/Desktop/changnam/autoware_map/borregasave_map/lanelet2_map.osm",
        obstacle_waypoint_frequency_in_sec=1,
        use_last_position_as_destination=True)
    transformer = ScenarioTransformer(configuration=configuration)

    scenario = transformer.transform()

    encoded_scenario = OpenScenarioEncoder.encode_proto_pyobject_to_dict(
        proto_pyobject=scenario, wrap_result_with_typename=False)

    assert len(transformer.entities.scenarioObjects) == 7
    assert encoded_scenario['OpenSCENARIO']['RoadNetwork']['LogicFile'][
        'filepath'] == configuration.road_network_lanelet_map_path
    assert len(
        encoded_scenario['OpenSCENARIO']['Entities']['ScenarioObject']) == 7
    assert len(encoded_scenario['OpenSCENARIO']['Storyboard']['Story']) == 7

    # scenario_yaml = OpenScenarioEncoder.encode_proto_pyobject_to_yaml(
    #     proto_pyobject=scenario, wrap_result_with_typename=False)

    # with open("doppel_9.yaml", 'w') as file:
    #     file.write(scenario_yaml)


def test_gen_all_samples(borregas_vector_map_path, borregas_apollo_map_path,
                         borregas_scenorita_scenario9_path,
                         borregas_scenorita_scenario75_path,
                         borregas_doppel_scenario9_path):

    scenario_paths = [
        borregas_scenorita_scenario9_path,
        borregas_scenorita_scenario75_path,
        borregas_doppel_scenario9_path,
    ]

    for scenario_path in scenario_paths:
        configuration = ScenarioTransformerConfiguration(
            apollo_scenario_path=scenario_path,
            apollo_hd_map_path=borregas_apollo_map_path,
            vector_map_path=borregas_vector_map_path,
            road_network_lanelet_map_path=
            "/home/sora/Desktop/changnam/autoware_map/borregasave_map/lanelet2_map.osm",
            obstacle_waypoint_frequency_in_sec=2,
            use_last_position_as_destination=True)
        transformer = ScenarioTransformer(configuration=configuration)
        scenario = transformer.transform()
        scenario_yaml = OpenScenarioEncoder.encode_proto_pyobject_to_yaml(
            proto_pyobject=scenario, wrap_result_with_typename=False)

        # filename = Path(scenario_path).parent.stem + "-" + Path(
        #     scenario_path).stem

        # with open(f"{filename}.yaml", 'w') as file:
        #     file.write(scenario_yaml)

    # assert True == False
