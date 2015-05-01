#-------------------------------------------------------------------------------
# Name:        __init__.py file for a sample package
# Purpose:     Import all required classes from the modules in the package
#
# Author:      mela6959
#
# Created:     30/04/2015
# Copyright:   (c) mela6959 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
"""
START DOC

This is where we can put documentation for the package


Including requirments and such!

END DOC
"""

from .modone import firstclass
from .modtwo import secondclass


if __name__ == "__main__":

    import sampleproject
    print (sampleproject.__doc__)

    print "This is from the modone: {}".format(sampleproject.firstclass.valOne)
    print "This is from the modtwo: {}".format(sampleproject.secondclass.valTwo)