from magicapi.config import MagicSettings, find_file


class CustomSettings(MagicSettings):
    custom_settings: bool = True

    app_name: str = "sploopery"

    class Config:
        env_file = find_file(glob_string="*.env") or ".env"


custom_settings = CustomSettings()
