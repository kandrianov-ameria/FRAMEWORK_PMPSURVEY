
import sys
from sys import platform
import os


class DriverLocations:
    
    DRIVERS_FOLDER = os.path.join(os.getcwd(), "FRAMEWORK_PMPSURVEY", "drivers", "")

    def get_Chrome_driver_location(self):
        return self.DRIVERS_FOLDER + "chromedriver.exe"

    def get_Firefox_driver_location(self):
        return self.DRIVERS_FOLDER + "geckodriver.exe"

    def get_Edge_driver_location(self):
        return self.DRIVERS_FOLDER + "msedgedriver.exe"

        

