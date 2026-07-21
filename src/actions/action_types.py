from enum import Enum

class ActionTypes(Enum):
    QUARANTINE_FILE = "quarantine_file"
    ISOLATE_HOST = "isolate_host"
    RESTORE_HOST = "restore_host" 
    CLOSE_PORT = "close_port" 
    DO_NOTHING = "do_nothing"