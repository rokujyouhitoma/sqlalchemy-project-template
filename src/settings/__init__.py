import importlib
import os

default_env = 'default'
supported_env = ['default', 'test']

env = os.environ.get('ENV')

env = env if env in supported_env else default_env

relative_module_name = '.{}'.format(env)

module = importlib.import_module(relative_module_name, 'settings')

DATABASE_URI = module.DATABASE_URI

__all__ = (DATABASE_URI)
