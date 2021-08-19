# A file to hold the exceptions classes

class TableSetError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class UnableToCreateFile(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class DatabaseInitError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)