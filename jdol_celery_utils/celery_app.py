import os
import tomllib
from celery import Celery

def get_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.toml')
    with open(config_path, 'rb') as f:
        config = tomllib.load(f)
    return config

config = get_config()

def construct_address(config_section):
    protocol = config[config_section]['protocol']
    username = config[config_section]['username']
    password = config[config_section]['password']
    servername = config[config_section]['servername']
    port = config[config_section]['port']
    return f"{protocol}://{username}:{password}@{servername}:{port}"

broker_address = construct_address('broker')
result_backend_address = construct_address('result_backend')

package_name = os.path.basename(os.path.dirname(__file__))

app = Celery(
    package_name,
    broker=broker_address,
    backend=result_backend_address
)

def get_queue_name():
    return config['queue_name']