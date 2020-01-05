from sense_history.Vibrator import Vibrator
from sense_history.GPS import GPS
from absl import flags
from absl import app
from run_POIs import run_POIs
from run_border import run_border
import logging

ALL_MODULES = ['BERLIN_WALL', 'BERLIN_HISTORIC', 'ZURICH_TREES']
MODULE_TYPES = {'BERLIN_WALL': 'border',
                'BERLIN_HISTORIC': 'POIs',
                'ZURICH_TREES': 'POIs'}

FLAGS = flags.FLAGS

flags.DEFINE_enum('module', 'BERLIN_WALL', ALL_MODULES, 'The module')
flags.DEFINE_boolean('debug', False, 'Outputs the logs in the console')
flags.DEFINE_float('radius', 5.00, 'Radius in which a POI is detected')


def setup_logs(module: str, debug: bool) -> None:
    FORMAT = '%(asctime)-15s: %(message)s'
    if debug:
        logging.basicConfig(format=FORMAT, level=logging.INFO) 
    else:
        log_file = './logs/{}.log'.format(module)
        logging.basicConfig(format=FORMAT, level=logging.INFO, filename=log_file, filemode='a')


def main(argv) -> None:

    setup_logs(FLAGS.module, FLAGS.debug)

    # Get hardware ready
    vibrator: Vibrator = Vibrator()
    gps: GPS = GPS()
    vibrator.stop()

    # Run module dependent on its type
    module_type = MODULE_TYPES[FLAGS.module]
    if module_type == 'border':
        run_border(FLAGS.module, gps, vibrator)
        pass
    if module_type == 'POIs':
        run_POIs(FLAGS.module, gps, vibrator, FLAGS.radius)


if __name__=='__main__':
    app.run(main)

