from pydantic import BaseModel, BaseSettings, PostgresDsn
from src import PROJECT_ROOT_PATH


class DatabaseSettings(BaseModel):
    hostname: str
    port: int
    username: str
    password: str
    name: str

    @property
    def dsn(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            host=self.hostname,
            port=str(self.port),
            user=self.username,
            password=self.password,
            path='/' + self.name
        )


class Settings(BaseSettings):
    database_settings: DatabaseSettings


def get_settings(env_file=f'{PROJECT_ROOT_PATH}/.env') -> Settings:
    return Settings(_env_file=env_file)


GLOBAL_CONFIG = get_settings()
