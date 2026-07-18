from enums import ThreatSeverity


class CyberEnvironment:

    def __init__(
            self,
            host_online: bool, 
            host_compromised: bool, 
            host_isolated: bool, 
            open_ports: list[int],
            malicious_ports: list[int],
            network_attack_active: bool, 
            malicious_dns_activity: bool, 
            actual_threat_severity: str,
            threat_contained: bool,
            administrator_notified: bool,
            current_step: int, 
            max_steps: int, 
            episode_done: bool, 
            ):
        
        self.host_online = host_online
        self.host_compromised = host_compromised
        self.host_isolated = host_isolated
        self.open_ports = open_ports
        self.malicious_ports = malicious_ports
        self.network_attack_active = network_attack_active
        self.malicious_dns_activity = malicious_dns_activity

        try:
            self.actual_threat_severity = ThreatSeverity(actual_threat_severity)
        except ValueError:
            print("Value Error: invalid threat severity found within Cyber Environment definiton")

        self.threat_contained = threat_contained
        self.administrator_notified = administrator_notified
        self.current_steps = current_step
        self.max_steps = max_steps
        self.episode_done = episode_done
            


