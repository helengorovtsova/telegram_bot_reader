from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    admin_id: list[int]

@dataclass
class Config:
    bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        bot=TgBot(
            token=env.str("TOKEN"),
            admin_id=env.list("ADMIN_ID")
        )
    )