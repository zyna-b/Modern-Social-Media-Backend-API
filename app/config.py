from pydantic import BaseSettings  # It is used to automatically loads values from environment variables.

import os

class Settings(BaseSettings):
    database_hostname: str = ""
    database_port: str = "5432"
    database_password: str = ""
    database_name: str = ""
    database_username: str = ""

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

    def get_database_url(self):
        # Check for platform-provided DATABASE_URL (works for both Render and Heroku)
        database_url = os.getenv("DATABASE_URL")
        if database_url:
            # Both Render and Heroku use postgres:// but SQLAlchemy needs postgresql://
            if database_url.startswith("postgres://"):
                database_url = database_url.replace("postgres://", "postgresql://", 1)
            return database_url
        
        # Fallback to individual components for local development
        return f'postgresql://{self.database_username}:{self.database_password}@{self.database_hostname}:{self.database_port}/{self.database_name}'

setting = Settings()

