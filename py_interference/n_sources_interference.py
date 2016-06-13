#! /usr/bin/env python3
from math import *
import numpy as np
import matplotlib.pyplot as plt

class Sources(object):
    """ Class that contains all the properties of wave source """
    def __init__(self):
        self.nSources = 100 # Amount of sources
        #self.wavelength = wavelength * (10 ** (-9))# Wavelength of the sources in nm
        self.wavelength = 0.5 # Wavelength of the sources in m
        self.distance = 2 # Distance between the sources, default is 1m

    def setup(self):
        """ Function to change all properties of the source. """
        print("Setting up the source")
        self.nSources = int(input("Amount of sources ( min = 2 ): "))
        if self.nSources < 2:
            while self.nSources < 2:
                self.nSources = input("Error: amount of sources must be higher than 2: ")

        #self.wavelength = float(input("Give a wavelength for the waves: ")) * (10 **(-9))
        self.wavelength = float(input("Give a wavelength for the waves: "))
        self.distance = float(input("Set the distance between the sources: "))

    def source_print(self):
        """ Function that prints all the properties of the source class"""
        print("Amount of sources: {}".format(self.nSources))
        print("Wavelength: {}".format(self.wavelength))
        print("distance between sources: {}".format(self.distance))

    def plot_graph(self):
        """ Function to plot a graph of the interference pattern"""
        teta = np.arange(-2 * np.pi, 2 * np.pi, 0.001)
        delta = (2 * np.pi / self.wavelength * self.distance * np.sin(teta))
        rel_intensity = (np.sin(0.5 * self.nSources * delta) / np.sin(0.5 * delta)) ** 2
        plt.plot(teta, rel_intensity)
        plt.xlabel("angle of the sources")
        plt.ylabel("relative intensity")
        plt.title("Interference of two coherent sources")
        plt.grid(True)
        plt.savefig("n_sources_interference.png")
        plt.show()

