import logging

LOG_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'

logger = logging.getLogger(__name__)

logging.basicConfig(format=LOG_FORMAT,
                    level=logging.INFO,
                    filename='microservice/logs/main_logs.log',
                    filemode='a')
