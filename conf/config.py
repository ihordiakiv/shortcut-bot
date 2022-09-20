from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Shortcut bot"

    SHORTCUT_API_TOKEN: str
    SHORTCUT_API_URL: AnyHttpUrl = "https://api.app.shortcut.com/api"

    ROOT_PATH: str = "/shortcut"
    OPENAPI_URL: str = "/openapi.json"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"

    class Config:
        case_sensitive = True
        env_file = ".env"


conf = Settings()
