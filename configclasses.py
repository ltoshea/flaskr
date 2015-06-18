class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class TestConfig(BaseConfig):
    DEBUG = False
    TESTING = True