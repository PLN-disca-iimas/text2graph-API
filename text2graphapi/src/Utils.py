from joblib import Parallel, delayed
import joblib
import os 
import sys
import logging

from src import configs

# Logging configs
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(asctime)s; - %(levelname)s; - %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Utils(object):
    def __init__(self):
        ...


    def joblib_delayed(self, funct, params):
        return delayed(funct)(params)


    def joblib_parallel(self, delayed_funct, n_jobs=configs.DEFAULT_NUM_CPU_JOBLIB, backend='loky'):
        return Parallel(
            n_jobs=n_jobs,
            backend=backend
        )(delayed_funct)


    def save_data(self, data, file_name, path=configs.OUTPUT_DIR_PATH, format_file='.pkl', compress=False):
        if not os.path.exists(path):
            self.create_dir(path)
        path_file = os.path.join(path, file_name + format_file)
        joblib.dump(data, path_file, compress=compress)


    def create_dir(self, path):
        try:
            os.makedirs(path)
        except Exception as e:
            logger.error('Error: %s', str(e))