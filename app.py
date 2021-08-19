# Logging import and settings
import logging
logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s", level=logging.DEBUG,
                    filename='log.txt')
log = logging.getLogger('cp_flue_gases')

# Other imports
