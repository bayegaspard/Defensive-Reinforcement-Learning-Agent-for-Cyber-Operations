from enums import HostStatus, ThreatSeverity
from suspicious_file import SuspiciousFile


class State:

    def __init__(
        self,
        host_status: str = "online",
        suspicious_file: SuspiciousFile | None = None,
        open_ports: list[int] | None = None,
        dns_anomaly: bool = False,
        email_attachment_flagged: bool = False,
        threat_severity: str = "none",
        host_isolated: bool = False,
        administrator_notified: bool = False,
        step_number: int = 0
    ):
        self.host_status = HostStatus(host_status)
        self.suspicious_file = suspicious_file
        self.open_ports = list(open_ports) if open_ports is not None else []
        self.dns_anomaly = dns_anomaly
        self.email_attachment_flagged = email_attachment_flagged
        self.threat_severity = ThreatSeverity(threat_severity)
        self.host_isolated = host_isolated
        self.administrator_notified = administrator_notified
        self.step_number = step_number