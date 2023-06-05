#!/usr/bin/env python3

import sys

from math import sqrt

def print_results(pSize, sSize, p, v):
    low95 = p - (1.96 * sqrt(v) * 100)
    high95 = p + (1.96 * sqrt(v) * 100)
    low99 = p - (2.58 * sqrt(v) * 100)
    high99 = p + (2.58 * sqrt(v) * 100)
    print("Population size:\t\t{x:.0f}".format(x = pSize))
    print("Sample size:\t\t\t{x:.0f}".format(x = sSize))
    print("Voting intentions:\t\t{x:.2f}%".format(x = p))
    print("Variance:\t\t\t{x:.6f}".format(x = v))
    print("95% confidence interval:\t[{x:.2f}%; {y:.2f}%]".format(x = low95, y = high95))
    print("99% confidence interval:\t[{x:.2f}%; {y:.2f}%]".format(x = low99, y = high99))
    return 0

def poll209(pSize, sSize, p):
    try:
        v = ((p*(100-p)/10000) / sSize) * (pSize - sSize)/(pSize - 1)
    except ZeroDivisionError:
        v = ((p*(100-p)/10000) / sSize) * (pSize - sSize)/(-1)
    print_results(pSize, sSize, p, v)
    return 0

def error_handling():
    if (len(sys.argv) == 1):
        return 84
    if (len(sys.argv) == 2 and sys.argv[1] != "-h"):
        return 84
    if (sys.argv[1] == "-h"):
        return 0
    if (len(sys.argv) != 4):
        return 84
    try:
        arg1 = int(sys.argv[1])
        arg2 = int(sys.argv[2])
        arg3 = float(sys.argv[3])
    except ValueError:
        return 84
    if (int(sys.argv[1]) < 0 or int(sys.argv[2]) <= 0):
        return 84
    if (int(sys.argv[1]) < int(sys.argv[2])):
        return 84
    if (100.0 < float(sys.argv[3]) or float(sys.argv[3]) < 0.0):
        return 84
    return 0

def help():
    print("USAGE")
    print("\t./209poll pSize sSize p")
    print("")
    print("DESCRIPTION")
    print("\tpSize\tsize of the population")
    print("\tsSize\tsize of the sample (supposed to be representative)")
    print("\tp\tpercentage of voting intentions for a specific candidate")
    return 0

def main():
    if (error_handling() == 84):
        return 84
    if (sys.argv[1] == "-h"):
        help()
    else:
        try:
            poll209(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))
        except:
            return 84
    return 0

sys.exit(main())