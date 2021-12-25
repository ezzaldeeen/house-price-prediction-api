class Config(object):
    """
        Base application configuration
    """
    DEBUG = False
    TESTING = False

    def __init__(self):
        pass


class ProductionConfig(Config):
    """
        Production application configuration
    """
    DEBUG = True
    ENV = 'production'


class DevelopmentConfig(Config):
    """
        Development application configuration
    """
    DEBUG = True
    ENV = 'dev'
