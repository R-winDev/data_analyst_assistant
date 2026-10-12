class DataValidationError(Exception):
    """The data input has rejected our rules."""
    def __init__(self, message: str, column: str | None = None):
        super().__init__(message)
        self.column = column