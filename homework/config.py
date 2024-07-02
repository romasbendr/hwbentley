class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    DB_HOST = 'database'

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    DB_HOST = 'big.production.database'

class TestingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DB_HOST = 'mock.database'