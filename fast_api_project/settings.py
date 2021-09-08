import os
from pathlib import Path

import environ

# Set base project dir
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


env = environ.Env()

FAST_API_ENV = env('FAST_API_ENV')

if FAST_API_ENV == 'LOCAL':
    env.read_env(os.path.join(BASE_DIR, 'env_vars/local.conf'))
elif FAST_API_ENV == 'PROD':
    env.read_env(os.path.join(BASE_DIR, 'env_vars/prod.conf'))


DB_USER = env('DB_USER')
DB_PASSWORD = env('DB_PASSWORD')
DB_NAME = env('DB_NAME')
DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')
