#! /usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

class Sources(object):
    """ Class that contains all the properties of wave source """
    def __init__(self):
        self.sourcesDist = 2 * (10 ** (-2))# Amount of sources
        self.wavelength = 855.995 * (10 ** (-9)) # Wavelength of the sources
        self.distance = 1 # Distance to the screen, default is 1m

    def setup(self):
        """ Function to change all properties of the source. """
        print("Setting up the source")
        self.sourcesDist = int(input("distance between the sources in cm: ")) * (10 ** (-2))
        self.wavelength = float(input("Give a wavelength for the waves in nm (sodium = 588.995nm): ")) * (10 ** (-9))
        self.distance = float(input("Set the distance to the screen in m: "))

    def source_print(self):
        """ Function that prints all the properties of the source class"""
        print("Distance between sources is {} cm".format(self.sourcesDist))
        print("Wavelength is {} nm".format(self.wavelength))
        print("distance to the screen is {} m".format(self.distance))

    def plot_graph(self):
        """ Function to plot a graph of the interference pattern"""
        x = np.arange(-0.0005, 0.0005, 0.000001)
        rel_intensity = np.cos((np.pi * self.sourcesDist * x)/(self.distance * self.wavelength))
        plt.plot(x, rel_intensity)
        plt.xlabel("distance on screen (m)")
        plt.ylabel("relative intensity")
        plt.title("Interference of two coherent sources")
        plt.grid(True)
        plt.savefig("two_sources_interference.png")
        plt.show()
