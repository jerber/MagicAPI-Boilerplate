from magicapi.config import MagicSettings


class CustomSettings(MagicSettings):
    custom_settings: bool = True

    app_name: str = 'sploopery'


custom_settings = CustomSettings()
