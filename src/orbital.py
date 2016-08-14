import math

mu = {"Sun": 132712440018.0, "Mercury": 22032.0, "Venus": 324859.0, "Earth": 398600.4418, "Moon": 4904.8695,
      "Mars": 42828.0, "Ceres": 63.1, "Jupiter": 126686534.0, "Saturn": 37931187.0, "Uranus": 5793939.0,
      "Neptune": 6836529.0, "Pluto": 871.0, "Eris": 1108.0}  # Units = km^3/s^2

radius = {"Sun": 696342.0, "Mercury": 2439.0, "Venus": 6052.0, "Earth": 6371.0, "Moon": 1737.0, "Mars": 3389.5,
          "Ceres": 473.0, "Jupiter": 69911.0, "Saturn": 58232.0, "Uranus": 25362.0, "Neptune": 24622.0, "Pluto": 1186.0,
          "Eris": 1163.0}  # Units = km


class Orbit:
    def __init__(self, planet, **kwargs):
        self.planet = planet
        if "inclination" in kwargs:
            self.inclination = kwargs["inclination"]
        else:
            self.inclination = 0.0
        if "altApoapsis" in kwargs:
            self.apoapsis = kwargs["altApoapsis"] + radius[self.planet]
        if "altPeriapsis" in kwargs:
            self.periapsis = kwargs["altPeriapsis"] + radius[self.planet]
        if "semiMajorAxis" in kwargs:
            self.a = kwargs["semiMajorAxis"]
        if "eccentricity" in kwargs:
            self.e = kwargs["eccentricity"]
        if "radApoapsis" in kwargs:
            self.apoapsis = kwargs["radApoapsis"]
        if "radPeriapsis" in kwargs:
            self.periapsis = kwargs["radPeriapsis"]
        self.energy = -mu[self.planet] / (self.periapsis + self.apoapsis)

    def __str__(self):
        return "Periapsis of %f km (%f km/s) and apoapsis of %f km (%f km/s) around %s, Energy = %f" % (
            self.periapsis, self.vel_periapsis(), self.apoapsis, self.vel_apoapsis(), self.planet, self.energy)

    def vel_periapsis(self):
        return math.sqrt(2.0 * (self.energy + mu[self.planet] / self.periapsis))

    def vel_apoapsis(self):
        return math.sqrt(2.0 * (self.energy + mu[self.planet] / self.apoapsis))

    def hohmann(self, orbit2):
        xfer_args = {"radPeriapsis": self.periapsis, "radApoapsis": orbit2.apoapsis, "inclination": self.inclination}
        xfer = Orbit(self.planet, **xfer_args)
        # print(xfer)
        DV1 = xfer.vel_periapsis() - self.vel_periapsis()
        DV2 = math.sqrt(
            orbit2.vel_apoapsis() ** 2 + xfer.vel_apoapsis() ** 2 - 2.0 * orbit2.vel_apoapsis() * xfer.vel_apoapsis() * math.cos(
                orbit2.inclination - xfer.inclination))
        return DV1 + DV2, DV1, DV2


if __name__ == "__main__":
    orbit1 = Orbit("Moon", radPeriapsis=5000.0, radApoapsis=5000.0, inclination=28.5)
    print(orbit1)
    orbit2 = Orbit("Moon", radPeriapsis=10000.0, radApoapsis=10000.0, inclination=28.5)
    print(orbit2)
    DVtot, DV1, DV2 = orbit1.hohmann(orbit2)
    print("Total DV: %f" % DVtot)
    print("First DV: %f" % DV1)
    print("Second DV: %f" % DV2)
    print(orbit1.inclination, orbit2.inclination)

    # def foo(**kwargs):
    #     print(kwargs)
    #
    #
    # foo(**radius)
