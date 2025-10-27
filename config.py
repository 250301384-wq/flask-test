import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """应用配置"""
    host: str = "0.0.0.0"
    port: int = 5000
    debug: bool = True
    model_path: str = "models/news_classifier"
    
class Settings:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5000
        self.debug = True

def get_settings():
    return Settings()

    class Config:
        env_file = ".env"

def get_settings():
    """获取配置实例"""
    return Settings()
