# Enviroment configurations


class Config:
    """Parent configurations."""
    DEBUG = False


class DevelopmentConfig(Config):
    """Development enviroment configurations."""
    DEBUG = True


class TestingConfig(Config):
    """Testing enviroment configurations."""
    TESTING = True


class ProductionConfig(Config):
    """Production enviroment configurations."""
    TESTING = False


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
