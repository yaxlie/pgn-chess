from enum import Enum

class Endpoint(Enum):
    login = '/user/login'
    logout = '/user/logout'
    engine_start = '/engine/start'
    engine_stop = '/engine/stop'