from environment.cyber_environment import CyberEnvironment
from src.environment.enums import FileAnalysis

def quarantine_file(environment: CyberEnvironment):
    environment.suspicious_file.quarantined = True

    if environment.get_active_threats() == 0:
        environment.threat_contained = True

def isolate_host(environment: CyberEnvironment):
    environment.host_status = "isolated"

def restore_host(environment: CyberEnvironment):
    environment.host_status = "restored"

def close_port(environment: CyberEnvironment, port: int):
    environment.open_ports.remove(port)

def do_nothing():
    pass