from enum import Enum 


class HostStatus(Enum):
    ONLINE = "online"
    COMPROMISED = "compromised"
    RESTORED = "restored"
    ISOLATED = "isolated"

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
