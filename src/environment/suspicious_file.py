from enums import FileAnalysis


class SuspiciousFile:

    def __init__(
        self,
        path: str,
        analysis_status: str = "not_analyzed",
        quarantined: bool = False,
        deleted: bool = False
    ):
        self.path = path
        self.analysis_status = FileAnalysis(analysis_status)
        self.quarantined = quarantined
        self.deleted = deleted