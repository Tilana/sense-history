import L76X
import time
import logging
import pdb

class GPS:
    def __init__(self, baudrate=9600):
        self.gps = L76X.L76X()
        self.gps.L76X_Set_Baudrate(115200)
        time.sleep(2)
        self.gps.L76X_Send_Command(self.gps.SET_POS_FIX_400MS)
        self.gps.L76X_Exit_BackupMode()

    def get_position(self, logs=True):
        self.gps.L76X_Gat_GNRMC()
        if logs:
            self.print_position()
        return (self.gps.lon_DD, self.gps.lat_DD)

    def print_position(self):
        logging.info('Time {}:{}:{}'.format(self.gps.Time_H, self.gps.Time_M, self.gps.Time_S))
        logging.info('Longitude = {}  Latitude = {}'.format(self.gps.lon_DD, self.gps.lat_DD))

    def stop(self):
        #GPIO.cleanup()
        logging.info('GPS stopped')

