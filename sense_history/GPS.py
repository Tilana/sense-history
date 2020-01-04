from sense_history import L76X
from typing import Tuple
import time
import logging
import pdb

class GPS:
    def __init__(self, baudrate: int=9600) -> None:
        self.gps = L76X.L76X()
        self.gps.L76X_Set_Baudrate(baudrate)
        time.sleep(2)
        self.gps.L76X_Send_Command(self.gps.SET_POS_FIX_400MS)
        self.gps.L76X_Exit_BackupMode()

    def get_position(self, logs: bool=True) -> Tuple[float, float]:
        self.gps.L76X_Gat_GNRMC()
        if logs:
            self.print_position()
        return (self.gps.lon_DD, self.gps.lat_DD)

    def print_position(self) -> None:
        logging.info('Time {}:{}:{}'.format(self.gps.Time_H, self.gps.Time_M, self.gps.Time_S))
        logging.info('Longitude = {}  Latitude = {}'.format(self.gps.lon_DD, self.gps.lat_DD))

    def stop(self) -> None:
        #GPIO.cleanup()
        logging.info('GPS stopped')

    def islocated(self) -> bool:
        return self.gps.Status

