from src.environment.enums import HostStatus, ThreatSeverity
from src.environment.suspicious_file import SuspiciousFile


class State:

    def __init__(
        self,
        host_status: HostStatus = "online",
        suspicious_file: SuspiciousFile | None = None,
        open_ports: list[int] | None = None,
        dns_anomaly: bool = False,
        threat_severity: HostStatus = "none",
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

        self.step_number = step_number

    def to_string(self) -> str:
        return f"""
host_status: {self.host_status}
suspicious_file_quarantined: {self.suspicious_file.quarantined if self.suspicious_file else None}
open_ports: {self.open_ports}
dns_anomaly: {self.dns_anomaly}
threat_severity: {self.threat_severity}
step_number: {self.step_number}
"""