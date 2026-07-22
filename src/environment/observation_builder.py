from src.environment.cyber_environment import CyberEnvironment
from src.environment.state import State
from src.environment.suspicious_file import SuspiciousFile

def build_observation(environment: CyberEnvironment) -> State:

    # construct new suspicious object file so the agent can't modify the environment

    observed_file = None

    if environment.suspicious_file is not None:
        observed_file = SuspiciousFile(
            path=environment.suspicious_file.path,
            analysis_status=environment.suspicious_file.analysis_status.value,
            quarantined=environment.suspicious_file.quarantined,
        )

    return State(        
        host_status=environment.host_status, 
        suspicious_file=observed_file,
        open_ports=environment.open_ports,
        dns_anomaly=environment.dns_anomaly,
        threat_severity=environment.actual_threat_severity, #TODO later make observed severity imperfect or derived from telemetry
        step_number=environment.current_step
    )