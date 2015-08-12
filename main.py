# arg1: input directory
# arg2: output directory

#TODO Handle spaces in filenames
#TODO Handle if Key is not present or artist not present
#TODO in that case, create dir called misc and move them there
#TODO if output directory is present, copy files there.
#TODO in that case, don't attempt to create directory
#TODO create a usage interface

from ID3 import *
from sys import argv
import os
from os import path
import shutil

print argv

# get the contents of the source directory
# TODO check if the source directory exists
directory_contents = os.listdir(argv[1])

input_directory = argv[1]

# create directory in source directory called output-music
# TODO check for permissions in output directory
output_path = argv[2] + "/output-music"
os.mkdir(output_path)

for current_file in directory_contents:
    print input_directory + '/' + current_file
    # TODO check if file is MP3 file
    # check ID3 artist tag
    try:
        id3 = ID3(input_directory + current_file)
        artist_name = id3['ARTIST']
        output_artist_dir = output_path + '/' + artist_name
        if not path.isdir(output_artist_dir):
            # create the directory
            os.mkdir(output_artist_dir)
        #copy the file to the output directory
        shutil.copy(input_directory + '/' + current_file, output_artist_dir)
    except KeyError:
        print "KeyError",
    except InvalidTagError, message:
        print "Invalid Tags: ", message
