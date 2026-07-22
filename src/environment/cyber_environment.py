from src.environment.enums import ThreatSeverity,HostStatus
from src.environment.suspicious_file import SuspiciousFile


class CyberEnvironment:

    def __init__(
            self,
            host_status: str, 
            open_ports: list[int],
            malicious_ports: list[int] | None,
            suspicious_file: str | None,
            suspicious_file_malicious: bool | None, 
            network_attack_active: bool, 
            dns_anomaly: bool, 
            dns_anomaly_malicious: bool,  
            actual_threat_severity: str,
            threat_contained: bool,
            current_step: int, 
            max_steps: int, 
            episode_done: bool, 
            ):
        
        try: 
            self.host_status = HostStatus(host_status)
        except ValueError:
            print("Value Error: invalid host status found within Cyber Environment definiton")
            raise ValueError

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
        self.current_step = current_step
        self.max_steps = max_steps
        self.episode_done = episode_done
    
    # returns number of active threats
    def get_active_threats(self) -> int:
        count = 0

        mp_count = 0
        for port in self.open_ports:
            if port in self.malicious_ports:
                mp_count += 1

        if self.suspicious_file is not None and self.suspicious_file_malicious and not self.suspicious_file.quarantined:
            count += 1
        if self.network_attack_active and mp_count > 0:
            count += 1
        if self.dns_anomaly_malicious and not self.host_isolated:
            count += 1
        if self.host_status.value == "compromised":
            count += 1
        
        return count
        


            


