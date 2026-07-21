from enums import HostStatus, ThreatSeverity
from suspicious_file import SuspiciousFile


class State:

    def __init__(
        self,
        host_status: str = "online",
        suspicious_file: SuspiciousFile | None = None,
        open_ports: list[int] | None = None,
        dns_anomaly: bool = False,
        threat_severity: str = "none",
        host_isolated: bool = False,
        step_number: int = 0
    ):
        
        try:
            self.host_status = HostStatus(host_status)
        except ValueError:
            print("Value Error: invalid host status found within agent state")
            raise ValueError

        self.suspicious_file = suspicious_file
        self.open_ports = list(open_ports) if open_ports is not None else []
        self.dns_anomaly = dns_anomaly

        try:
            self.threat_severity = ThreatSeverity(threat_severity)
        except ValueError:
            print("Value Error: invalid threat severity found within agent state")
            raise ValueError

        self.host_isolated = host_isolated
        self.step_number = step_number