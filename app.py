import logging
# Erasing previous log
with open('log.log', 'w'):
    pass

# Setting the logger
logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s", level=logging.DEBUG,
                    filename='log.log')
log = logging.getLogger('cp_flue_gases')

# Other imports


# Test Area
from data.db_manager import Database

host_name = 'stored_info'

app_db = Database(host_name)
app_db.add_fuel("NATGas", 40, 10, 10, 10, 10, 10, 10)
