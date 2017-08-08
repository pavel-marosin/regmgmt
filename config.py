import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False
    EVENTBRITE_EVENT_ID = '33739955114'
    EVENTBRITE_OAUTH_TOKEN = 'CBGAUJ744FPLCTIL6ILI'
    PUSHER_APP_ID = '66194'
    PUSHER_KEY = '0fbca878a6fe2601bbb2'
    PUSHER_SECRET = '1dffbd2510f9cac8d966'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    EVENTBRITE_EVENT_ID = '33739955114'
    EVENTBRITE_OAUTH_TOKEN = 'CBGAUJ744FPLCTIL6ILI'
    PUSHER_APP_ID = '66194'
    PUSHER_KEY = '0fbca878a6fe2601bbb2'
    PUSHER_SECRET = '1dffbd2510f9cac8d966'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    EVENTBRITE_EVENT_ID = '33739955114'
    EVENTBRITE_OAUTH_TOKEN = 'CBGAUJ744FPLCTIL6ILI'
    PUSHER_APP_ID = '66194'
    PUSHER_KEY = '0fbca878a6fe2601bbb2'
    PUSHER_SECRET = '1dffbd2510f9cac8d966'


class TestingConfig(Config):
    TESTING = True
    EVENTBRITE_EVENT_ID = '33739955114'
    EVENTBRITE_OAUTH_TOKEN = 'CBGAUJ744FPLCTIL6ILI'
    PUSHER_APP_ID = '66194'
    PUSHER_KEY = '0fbca878a6fe2601bbb2'
    PUSHER_SECRET = '1dffbd2510f9cac8d966'