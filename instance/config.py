import os


class Config():
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """Configurations for the development environment"""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for testing environment"""
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for a production environment"""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
