#!/usr/bin/env python3

## @package doxygit
# This is an example module representing a human
#
# Written for the CS tutorial
#
# @author Jens Dede <jd@comnets.uni-bremen.de>
# @date 2018-05-25

## A class which represents a human
class Human(object):
    ## Default constructor
    #
    # Constructor for the class. Default age for new objects: 0
    #
    # @param age    Age of the human. Default: 0
    # @param name   Name of the human. Default: None
    def __init__(self, age=0, name=None):
        self.__age=age
        self.__name=name

    def __str__(self):
        return type(self).__name__ + " with the name " \
                + str(self.__name) + " (" + str(self.__age) + " years old)"

    ## Return the age of the human
    #
    # @return The age
    def getAge(self):
        return self.__age

    ## Set the age of the human
    # @param age    Age of the human
    def setAge(self, age):
        self.__age = age

    ## Get the name of the human
    # @return The name
    def getName(self):
        return self.__name

    ## Set the name of the human
    # @param name   The name
    def setName(self, name):
        self.__name=name


if __name__ == "__main__":
    # Test this class
    print("Testing ", __file__)
    h = Human()
    print(h.getAge())
    h.setAge(12)
    print(h.getAge())
    print(h)