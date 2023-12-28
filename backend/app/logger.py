import os
import logging

log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)

#logging config
logging.basicConfig(
    filename=os.path.join(log_folder, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

log = logging.getLogger(__name__)