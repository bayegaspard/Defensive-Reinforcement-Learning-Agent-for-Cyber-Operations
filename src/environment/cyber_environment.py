from enums import ThreatSeverity,HostStatus
from suspicious_file import SuspiciousFile


class CyberEnvironment:

    def __init__(
            self,
            host_status: str, 
            host_isolated: bool, 
            open_ports: list[int],
            malicious_ports: list[int] | None,
            suspicious_file: str | None,
            suspicious_file_malicious: bool | None, 
            network_attack_active: bool, 
            dns_anomaly: bool, 
            dns_anomaly_malicious: bool,  
            actual_threat_severity: str,
            threat_contained: bool,
            administrator_notified: bool,
            current_step: int, 
            max_steps: int, 
            episode_done: bool, 
            ):
        
        try: 
            self.host_status = HostStatus(host_status)
        except ValueError:
            print("Value Error: invalid host status found within Cyber Environment definiton")
            raise ValueError

        self.host_isolated = host_isolated
        self.open_ports = open_ports
        self.malicious_ports = malicious_ports if malicious_ports is not None else []

        self.suspicious_file = SuspiciousFile(suspicious_file) if suspicious_file is not None else None

        self.suspicious_file_malicious = suspicious_file_malicious
        self.network_attack_active = network_attack_active
        self.dns_anomaly = dns_anomaly
        self.dns_anomaly_malicious = dns_anomaly_malicious

        try:
            self.actual_threat_severity = ThreatSeverity(actual_threat_severity)
        except ValueError:
            print("Value Error: invalid threat severity found within Cyber Environment definiton")
            raise ValueError

        self.threat_contained = threat_contained
        self.administrator_notified = administrator_notified
        self.current_step = current_step
        self.max_steps = max_steps
        self.episode_done = episode_done
            


