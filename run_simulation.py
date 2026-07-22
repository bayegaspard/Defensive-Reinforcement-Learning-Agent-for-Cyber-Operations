from src.agent.agent import Agent
from src.environment.cyber_environment import CyberEnvironment
agent = Agent("models/llama-3-8b-instruct.gguf")

environment = CyberEnvironment(
    host_status="compromised",
    open_ports=[22, 80, 4444],
    malicious_ports=[4444],
    suspicious_file=None,
    suspicious_file_malicious=None,
    network_attack_active=True,
    dns_anomaly=False,
    dns_anomaly_malicious=False,
    actual_threat_severity="high",
    threat_contained=False,
    current_step=0,
    max_steps=5,
    episode_done=False
)

result = agent.run_loop(environment)

for action in result:
    print(action)




 