from brigade.plugins.tasks.commands.remote_command import remote_command
from brigade.plugins.tasks.data.load_json import load_json
from brigade.plugins.tasks.data.load_yaml import load_yaml
from brigade.plugins.tasks.napalm.config import napalm_configure
from brigade.plugins.tasks.napalm.get_facts import napalm_get_facts
from brigade.plugins.tasks.text.template import template_file, template_string


__all__ = (
    "load_json",
    "load_yaml",
    "napalm_configure",
    "napalm_get_facts",
    "remote_command",
    "template_file",
    "template_string",
)