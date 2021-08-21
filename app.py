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
from utils.fuel import Fuel

host_name = 'stored_info'

app_db = Database(host_name)
app_db.update_fuel('lignite_coal', 51.12, 3.89, 14.65, 0.61, 1.87, 14.36, 13.5)
nat_gas = Fuel('lignite_coal', app_db)

