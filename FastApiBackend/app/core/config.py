from pydantic import BaseSettings


class Settings(BaseSettings):
    # Base
    api_v1_prefix: str
    debug: bool
    project_name: str
    version: str
    description: str

    # Database
    db_connection_str: str
