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
        
        try:
            self.analysis_status = FileAnalysis(analysis_status)
        except ValueError:
            print("Value Error: invalid File Analysis found within suspicious file definiton")
            raise ValueError

        self.quarantined = quarantined
        self.deleted = deleted