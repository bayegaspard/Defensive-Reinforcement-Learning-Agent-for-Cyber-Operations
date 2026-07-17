from enums import FileAnalysis


class SuspiciousFile:

    def __init__(
        self,
        path: str,
        detection_confidence: float = 0.0,
        analysis_status: str = "not_analyzed",
        malware_score: float | None = None,
        quarantined: bool = False,
        deleted: bool = False
    ):
        if not 0.0 <= detection_confidence <= 1.0:
            raise ValueError(
                "Detection confidence must be between 0.0 and 1.0."
            )

        if malware_score is not None and not 0.0 <= malware_score <= 1.0:
            raise ValueError(
                "Malware score must be between 0.0 and 1.0."
            )

        self.path = path
        self.detection_confidence = detection_confidence
        self.analysis_status = FileAnalysis(analysis_status)
        self.malware_score = malware_score
        self.quarantined = quarantined
        self.deleted = deleted