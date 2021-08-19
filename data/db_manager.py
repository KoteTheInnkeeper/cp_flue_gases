import os
import logging
from sqlite3.dbapi2 import OperationalError

from data.db_cursor import DBCursor
from utils.errors import *

# Setting loggers
log = logging.getLogger('cp_flue_gases.db_manager')


class Database:
    def __init__(self, host: str) -> None:
        try:
            self.host = self.db_path(host)
        except Exception:
            log.critical("An exception was raised.")
        else:
            log.debug(f"The database file was setted to {self.host}")
            try:
                log.debug("Initializing database.")
                # Checking if the database file exists at all
                if not self.check_if_exists():
                    # Database file doesn't exists
                    self.create_file()
                self.set_tables()
            except Exception:
                log.critical("An exception was raised.")
                raise DatabaseInitError("There was an error while trying to initialize the database.")
            finally:
                log.debug("Database set up successfully.")
    
    def db_path(self, host_name: str) -> str:
        """Returns the absolute path for the database file provided.
        :param host_name: the host name as a string."""
        log.debug("Getting the database file path")
        app_path = os.path.abspath(os.getcwd())
        folder = 'data'
        path = os.path.join(app_path, folder)
        return os.path.normpath(os.path.join(path, host_name)) + '.db'
    
    def check_if_exists(self) -> bool:
        """Checks if the file exists"""
        try:
            log.debug("Checking if database file exists.")
            with open(self.host, 'r'):
                pass
            log.debug("Database file exists.")
            return True
        except FileNotFoundError:
            log.critical("Database file doesn't exists.")
            return False
    
    def create_file(self) -> None:
        """Sets the database from zero. To be called when the file doesn't exists at all."""
        try:
            with open(self.host, 'w'):
                log.debug("File created.")
        except Exception:
            log.critical("An exception was raised")
            raise UnableToCreateFile("Couldn't create the database file.")

    def set_tables(self) -> None:
        """Sets the tables."""
        log.debug("Setting the tables.")
        try:
            with DBCursor(self.host) as cursor:
                cursor.execute("CREATE TABLE IF NOT EXISTS fuels(name TEXT UNIQUE, carbon REAL, hydrogen REAL, oxygen REAL, nitrogen REAL, sulfur REAL, moisture REAL, ashes REAL)")
                cursor.execute("CREATE TABLE IF NOT EXISTS combustion(temperature REAL, cp REAL)")
        except Exception:
            log.critical("An exception was raised.")
            raise TableSetError("There was an error while trying to set the tables.")
        else:
            log.debug("Database tables are fine.")

    def add_fuel(self, name: str, kC: float, kH: float, kO: float, kN: float, kS: float, kM: float, kAsh: float):
        """Adds the fuel.
        :param name: fuel's name.
        :param kC: carbon prescence in %
        :param kH: hydrogen prescence in %
        :param kO: oxygen prescence in %
        :param kN: nitrogen prescence in %
        :param kS: sulfur prescence in %
        :param kM: moisture prescence in %
        :param kAsh: ashes prescence in %"""
        try:
            log.debug(f"Adding a fuel named {name.title()}")
            with DBCursor(self.host) as cursor:
                cursor.execute(
                    "INSERT INTO fuels VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (name.lower(),kC/100, kH/100, kO/100, kN/100, kS/100, kM/100, kAsh/100)
                )
        except IntegrityError:
            log.critical("An IntegrityError was raised, meaning the name wasn't unique.")
            raise DuplicatedName("There's already a fuel in store with this name.")
        except Exception:
            log.critical("An exception was raised.")
            raise UnableToAdd("There was an issue when trying to add this fuel.")
        else:
            log.critical(f"This {name.title()} fuel was added successfully.")

        
    