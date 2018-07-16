#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import sys

# ====== ARGUMENTS CODE ======

options = {
    "height": None,
    "width": None,
    "count": 1,
    "file": None,
    "output": None
}

def heightArg(argument):
    try:
        height = int(argument)
    except ValueError:
        print("ERROR: An integer should be used to represent the desired height")
        exit(1)
    options["height"] = height

def widthArg(argument):
    try:
        width = int(argument)
    except ValueError:
        print("ERROR: An integer should be used to represent the desired height")
        exit(1)
    options["width"] = width

def countArg(argument):
    try:
        count = int(argument)
    except ValueError:
        print("ERROR: An integer should be used to represent the desired amount of images")
        exit(1)
    options["count"] = count

def fileArg(argument):
    options["file"] = argument

def outputArg(argument):
    options["output"] = argument

def helpArg():
    print("usage: resize-asset -f [file] -o [output] -w [width] -h [height]")
    print("\nARGUMENTS:")
    print("-f <name>   : REQUIRED  Input image that is being resized")
    print("-o <name>   : REQUIRED  Name of the output file, extension must NOT be included")
    print("")
    print("-w <width>  : REQUIRED* Width of the resized image, use alone or alongside height")
    print("-h <height> : REQUIRED* Height of the resized image, use alone or alongside width")
    print("")
    print("-c <amount> : Amount of sizes outputted (x2, x3), default is 1")
    exit(0)

# a tuple to used to represent if the flag accepts an argument followed by the handler function
args = {
    "height": (True, heightArg),
    "h": (True, heightArg),
    "width": (True, widthArg),
    "w": (True, widthArg),
    "count": (True, countArg),
    "c": (True, countArg),
    "file": (True, fileArg),
    "f": (True, fileArg),
    "output": (True, outputArg),
    "o": (True, outputArg),
    "help": (False, helpArg),
    "h": (False, helpArg)
}

def runArgument(flag, argumentIndex):
    if flag in args:
        arg = args[flag]
        if arg[0] == True:
            arg[1](sys.argv[argumentIndex])
        else:
            arg[1]()
    else:
        print("ERROR: Invalid argument `" + argument + "`")

for index in range(0, len(sys.argv)):
    arg = sys.argv[index]
    if arg[0] == "-":
        if arg[1] == "-":
            runArgument(arg[2:], index + 1)
        else:
            runArgument(arg[1], index + 1)

# ====== RESIZE CODE ======

if options["file"] != None:
    try:
        image = Image.open(options["file"])
        print("Loaded {} image ({} x {})".format(image.format, image.size[0], image.size[1]))
    except FileNotFoundError:
        print("ERROR: File does not exist")
        exit(1)

    if options["output"] != None:
        if options["width"] != None and options["height"] == None:
            # only width specified
            width = options["width"]
            height = round((options["width"] / image.size[0]) * image.size[1])
        elif options["height"] != None and options["width"] == None:
            # only height specified
            height = options["height"]
            width = round((options["height"] / image.size[1]) * image.size[0])
        elif options["height"] != None and options["width"] != None:
            # height AND width specified
            height = options["height"]
            width = options["width"]
            pass
        else:
            # neither height OR width specified
            print("ERROR: Width/height not specified, use --width [width] or/and --height [height]")
            exit(1)

        for i in range(0, options["count"]):
            print("")

            multiplier = i + 1
            if i == 0:
                filename = options["output"] + "." + image.format.lower()
            else:
                filename = options["output"] + "@" + str(multiplier) + "." + image.format.lower()

            print("Creating `{}`".format(filename))

            if (width * multiplier > image.size[0]):
                print("WARNING ({}): Resized image ({}) width larger than base image ({})".format(filename, width * multiplier, image.size[0]))

            if (height * multiplier > image.size[1]):
                print("WARNING ({}): Resized image ({}) height larger than base image ({})".format(filename, height * multiplier, image.size[1]))

            resizedImage = image.resize((width * multiplier, height * multiplier), Image.ANTIALIAS)
            resizedImage.save(filename)
            print("Done")
        if (multiplier < 2):
            plural = ""
        else:
            plural = "s"
        print("\n{} image{} saved".format(multiplier, plural))
    else:
        print("ERROR: No output file name specified, use --output [file]")

else:
    print("ERROR: No file specified, use --file [file]")
