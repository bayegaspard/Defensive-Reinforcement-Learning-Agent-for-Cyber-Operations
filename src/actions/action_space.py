from src.environment.state import State
from src.environment.cyber_environment import CyberEnvironment
from src.environment.enums import HostStatus
from src.actions.action_types import ActionTypes
from src.actions.actions import quarantine_file, isolate_host, restore_host, close_port, do_nothing 

def get_valid_actions(state: State) -> list[ActionTypes]:

    valid_actions = [] 

    # quarantine file 
    if state.suspicious_file is not None and not state.suspicious_file.quarantined:
        valid_actions.append(ActionTypes.QUARANTINE_FILE)

    # isolate host
    if state.host_status != HostStatus.ISOLATED:
        valid_actions.append(ActionTypes.ISOLATE_HOST)

    # restore host
    if state.host_status == HostStatus.COMPROMISED:
        valid_actions.append(ActionTypes.RESTORE_HOST)

    # close port
    if len(state.open_ports) > 0:
        valid_actions.append(ActionTypes.CLOSE_PORT)

    # do nothing  
    valid_actions.append(ActionTypes.DO_NOTHING)

    return valid_actions

def execute_action(environment: CyberEnvironment, valid_actions: list[ActionTypes], action: ActionTypes, port: int = None):

    if action not in valid_actions:
        raise ValueError("Invalid Action")

    # quarantine file  
    if action == ActionTypes.QUARANTINE_FILE:
        quarantine_file(environment)
    # isolate host
    elif action == ActionTypes.ISOLATE_HOST:
        isolate_host(environment)
    # restore host
    elif action == ActionTypes.RESTORE_HOST:
        restore_host(environment)
    # close port 
    elif action == ActionTypes.CLOSE_PORT:
        if port in environment.open_ports:
            close_port(environment, port)
        else:
            raise ValueError("Invalid port #")
    # do nothing
    elif action == ActionTypes.DO_NOTHING:
        do_nothing()


