# A file to hold the exceptions classes and other erros
from sqlite3 import IntegrityError

class TableSetError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class UnableToCreateFile(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class DatabaseInitError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class UnableToAdd(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class DuplicatedName(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)