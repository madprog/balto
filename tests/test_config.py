from os.path import dirname, join

from balto.config import (convert_json_config_to_toml, find_configuration_file,
                          parse_toml_config)

NO_CONFIG_DIR = join(dirname(__file__), "test_directories", "no_config")

CONFIG_JSON_DIR = join(dirname(__file__), "test_directories", "balto_json")

CONFIG_TOML_DIR = join(dirname(__file__), "test_directories", "balto_toml")


def test_find_no_configuration_file():
    assert find_configuration_file(NO_CONFIG_DIR) == None


def test_find_json_file():
    expected = join(CONFIG_JSON_DIR, ".balto.json")
    assert find_configuration_file(CONFIG_JSON_DIR) == expected


def test_find_toml_file():
    expected = join(CONFIG_TOML_DIR, ".balto.toml")
    assert find_configuration_file(CONFIG_TOML_DIR) == expected


def test_convert_json_config_to_toml():
    name = "Acceptance Test Suite Subprocess"
    tool = "pytest"
    json_config = [{"tool": tool, "name": name}]

    config = convert_json_config_to_toml(json_config)

    expected = """name = "%s"
tool = "%s"
"""

    assert config == expected % (name, tool)


def test_parse_toml_config():
    name = "Acceptance Test Suite Subprocess"
    tool = "pytest"
    raw_config = """name = "%s"
tool = "%s"
""" % (
        name,
        tool,
    )
    config = parse_toml_config(raw_config)

    assert config["name"] == name
    assert config["tool"] == tool

def test_parse_toml_config_runners():
    name = "Acceptance Test Suite Subprocess"
    tool = "pytest"
    command_override = "not-pytest-litf"
    raw_config = """name = "%s"
tool = "%s"

[subprocess]
command = "not-pytest-litf"
""" % (
        name,
        tool,
    )
    config = parse_toml_config(raw_config)

    assert config["subprocess"]["command"] == command_override