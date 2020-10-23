import os
from importlib import import_module

VALID_ENVS = ('development', 'staging', 'production')

env = 'development'
if env not in VALID_ENVS:
    raise RuntimeError("Invalid environment")

config_name = 'main.cfg.' + env
module = import_module(config_name)
config = module.Config
