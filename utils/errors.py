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

class UnableToUpdate(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class FuelNotConfirmed(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class FuelNotFound(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class CompositionNotFound(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class FuelIntegrityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class InvalidFuel(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class InvalidNumbers(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class InvalidTemperatures(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class NoFuelsFound(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)