import logging

logging.basicConfig(
  level=logging.INFO,
  format='[%(asctime)s] %(levelname)s - %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S',
  handlers=[logging.StreamHandler()],
)

log = logging.getLogger('ETNA')
