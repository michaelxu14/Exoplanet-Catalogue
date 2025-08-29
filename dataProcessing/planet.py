
class Planet:
    def __init__(self, name, type, detectionMethod, mass, radius, flux, tSurf, period, age, distance, esi):
        self.name = name
        self.type = type
        self.detectionMethod = detectionMethod
        self.mass = mass
        self.radius = radius
        self.flux = flux
        self.tSurf = tSurf
        self.period = period
        self.age = age
        self.distance = distance
        self.esi = esi

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_mass(self):
        return self.mass

    def set_mass(self, mass):
        self.mass = mass

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_flux(self):
        return self.flux

    def set_flux(self, flux):
        self.flux = flux

    def get_tSurf(self):
        return self.tSurf

    def set_tSurf(self, tSurf):
        self.tSurf = tSurf

    def get_period(self):
        return self.period

    def set_period(self, period):
        self.period = period

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def get_esi(self):
        return self.esi

    def set_esi(self, esi):
        self.esi = esi

    def __str__(self):
        return f"Planet(name={self.name}, type={self.type}, mass={self.mass}, radius={self.radius}, flux={self.flux}, tSurf={self.tSurf}, period={self.period}, distance={self.distance}, esi={self.esi})"