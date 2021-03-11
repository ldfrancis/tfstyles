import pytest
from tfstyles import gatys16

# set config_dict
config_dict = {
    "content_image_path": "",
    "style_image_path": "",
    "synthesized_image_path": "",
    "iterations": "",
}

gatys16.run(config_dict)


@pytest.mark.parametrize("config_dict", [9, "495", ["content"]])
def test_valid_input_to_run(config_dict):
    with pytest.raises(TypeError):
        gatys16.run(config_dict)


def test_config_dict_key_error():
    config_dict = {
        "steps": "",
    }
    with pytest.raises(KeyError):
        gatys16.run(config_dict)


def test_config_dict_path_error():
    config_dict = {
        "content_image_path": "",
        "style_image_path": "",
        "synthesized_image_path": "",
        "iterations": 200,
    }

    with pytest.raises(FileNotFoundError):
        gatys16.run(config_dict)