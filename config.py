# Created by Samuel Ndubuisi
# On 12th January, 2019

# Application configuration

class Config(object):
    """docstring for Config."""
    PORT = 5000
    HOST = 'localhost'


class ProductionConfig(object):
    """docstring for ProductionConfig."""
    DEBUG = False


class DevelopmentConfig(object):
    """docstring for DevelopmentConfig."""
    DEBUG = True
