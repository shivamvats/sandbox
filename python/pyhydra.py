import os
import hydra
import logging
from hydra.utils import to_absolute_path

logger = logging.getLogger(__name__)

@hydra.main(config_path='hydra_conf.yaml')
def main(cfg):
    logger.info('Hydra Working dir: %s' % os.getcwd())
    logger.info('Loaded file path: %s' % cfg.data.path)
    logger.info('Absolute file path: %s' % to_absolute_path(cfg.data.path))
    with open(to_absolute_path(cfg.data.path), 'r') as f:
        print(f.readlines())

if __name__ == "__main__":
    main()
