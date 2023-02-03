''' Determine the age on a planet given time in seconds. '''
class SpaceAge(object):
    SECONDS_IN_DAY = 86400
    EARTH_DAYS = 365.25
    EARTH_SECONDS = EARTH_DAYS * SECONDS_IN_DAY
    MERCURY_SECONDS = 0.2408467 * EARTH_SECONDS
    VENUS_SECONDS = 0.61519726 * EARTH_SECONDS
    MARS_SECONDS = 1.8808158 * EARTH_SECONDS
    JUPITER_SECONDS = 11.862615 * EARTH_SECONDS
    SATURN_SECONDS = 29.447498 * EARTH_SECONDS
    URANUS_SECONDS = 84.016846 * EARTH_SECONDS
    NEPTUNE_SECONDS = 164.79132 * EARTH_SECONDS

    def __init__(self, seconds):
        self.seconds = seconds

        self.SECONDS_IN_DAY = 86400
        self.EARTH_DAYS = 365.25
        self.EARTH_SECONDS = self.EARTH_DAYS * self.SECONDS_IN_DAY
        self.MERCURY_SECONDS = 0.2408467 * self.EARTH_SECONDS
        self.VENUS_SECONDS = 0.61519726 * self.EARTH_SECONDS
        self.MARS_SECONDS = 1.8808158 * self.EARTH_SECONDS
        self.JUPITER_SECONDS = 11.862615 * self.EARTH_SECONDS
        self.SATURN_SECONDS = 29.447498 * self.EARTH_SECONDS
        self.URANUS_SECONDS = 84.016846 * self.EARTH_SECONDS
        self.NEPTUNE_SECONDS = 164.79132 * self.EARTH_SECONDS
    
    def on_earth(self):
        return round(self.seconds / self.EARTH_SECONDS,2)

    def on_mercury(self):
        return round(self.seconds / self.MERCURY_SECONDS, 2)

    def on_venus(self):
        return round(self.seconds / self.VENUS_SECONDS, 2)

    def on_mars(self):
        return round(self.seconds / self.MARS_SECONDS, 2)

    def on_jupiter(self):
        return round(self.seconds / self.JUPITER_SECONDS, 2)

    def on_saturn(self):
        return round(self.seconds / self.SATURN_SECONDS, 2)

    def on_uranus(self):
        return round(self.seconds / self.URANUS_SECONDS, 2)

    def on_neptune(self):
        return round(self.seconds / self.NEPTUNE_SECONDS, 2)
