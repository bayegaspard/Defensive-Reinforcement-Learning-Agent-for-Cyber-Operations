from enum import Enum

class ActionTypes(Enum):
    NOTIFY_ADMINISTRATOR = "notify_administrator"
    ANALYZE_FILE = "analyze_file"
    QUARANTINE_FILE = "quarantine_file"
    DELETE_FILE = "delete_file"
    ISOLATE_HOST = "isolate_host"
    CLOSE_PORT = "close_port" 
    DO_NOTHING = "do_nothing"