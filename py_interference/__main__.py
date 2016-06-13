#! /usr/bin/env python3

import os, sys, getopt
import py_interference.n_sources_interference as ns
import py_interference.two_sources_interference as ts

def usage():
    print("usage:")
    print("-t       calculate interference pattern for two coherent sources")
    print("-n       calculate interference pattern for n coherent sources")
    print("-h       print this help")
    print("--help   same as -h")

def twoSources():
    source = ts.Sources()
    source.setup()
    source.plot_graph()

def nSources():
    source = ns.Sources()
    source.setup()
    source.plot_graph()

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "htn:", "help")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, args in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == "-t":
            twoSources()
            sys.exit()
        elif opt == "-n":
            nSources()
            sys.exit()
        else:
            usage()
            sys.exit()

if __name__ == "py_interference.__main__":
    main(sys.argv[1:])
