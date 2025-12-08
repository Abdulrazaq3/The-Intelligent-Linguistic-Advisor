from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    FIREWORKS_API_KEY: str
    CHROMA_PATH: str = "my_arabic_db"

    EMBEDDING_MODEL: str = "accounts/fireworks/models/qwen3-embedding-8b"
    LLM_MODEL: str = "accounts/fireworks/models/qwen2p5-vl-32b-instruct"

    # إعدادات Pydantic Settings (تقرأ من .env)
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
