from enum import Enum 


class HostStatus(Enum):
    ONLINE = "online"
    UNDER_ATTACK = "under_attack"
    COMPROMISED = "compromised"
    OFFLINE = "offline"

class ThreatSeverity(Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium" 
    HIGH = "high"
    CRITICAL = "critical"

class FileAnalysis(Enum):
    NOT_ANALYZED = "not_analyzed"
    CLEAN = "clean"
    MALICIOUS = "malicious"
    FAILED = "failed"   
