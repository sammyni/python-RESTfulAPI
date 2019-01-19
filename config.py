# Created by Samuel Ndubuisi
# On 12th January, 2019

# Application configuration

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """docstring for Config."""
    PORT = 8080
    HOST = '0.0.0.0'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(Config):
    """docstring for ProductionConfig."""
    DEBUG = False


class DevelopmentConfig(Config):
    """docstring for DevelopmentConfig."""
    DEVELOPMENT = True
    DEBUG = True

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
