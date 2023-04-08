import logging
import m
logging.basicConfig(level=logging.NOTSET,format="%(funcName)s %(asctime)s %(levelname)s-%(name)s:%(message)s")

logger = logging.getLogger("test")
logging.debug(" debug")
logger.info("info")
logging.critical(" problem")
logging.error("test error")
logging.warning("test warning")
m.main()

