"""
Get environment variables.
"""

from dataclasses import dataclass
from environs import Env


@dataclass
class Config:
    """
    Class to store environment variables.
    """

    app_mode : str
    db_url : str


def load_config() -> Config:
    """
    Function to load the environment config.
    """

    # Env instance
    env = Env()

    # read_env
    env.read_env()

    app_mode = env.str('APP_MODE')
    db_url = env.str('DATABASE_URL')
    decoded_db_url = db_url.encode('latin1').decode('unicode_escape')


    return Config(
        app_mode=app_mode,
        db_url=decoded_db_url,
    )

settings = load_config()
