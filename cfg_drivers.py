import os

class DriverLocations:

    """The OS Module will get the current root directory and 
    add the 'drivers' subfolder to the driver path."""

    DRIVERS_FOLDER = os.path.join(os.getcwd(), "drivers", "")

    def get_Chrome_driver_location(self):
        return self.DRIVERS_FOLDER + "chromedriver.exe"

    def get_Firefox_driver_location(self):
        return self.DRIVERS_FOLDER + "geckodriver.exe"

    def get_Edge_driver_location(self):
        return self.DRIVERS_FOLDER + "msedgedriver.exe"


driverpath = DriverLocations()