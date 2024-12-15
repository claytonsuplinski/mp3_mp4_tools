import ffmpeg

##########
# Inputs #
##########

START_TIME = "00:00:08"
END_TIME   = "00:04:05" # False # "00:00:30"

####################
# Global Variables #
####################

BASE_DIR = "/Users/csuplinski/Desktop/mp3_mp4_tools/dev"

INPUT_FILE  = "{0}/input.mp3".format(  BASE_DIR )
OUTPUT_FILE = "{0}/trimmed.mp3".format( BASE_DIR )

############
# Trim mp4 #
############

if   START_TIME and END_TIME : ffmpeg.input( INPUT_FILE, ss=START_TIME, to=END_TIME ).output( OUTPUT_FILE ).run()
elif START_TIME              : ffmpeg.input( INPUT_FILE, ss=START_TIME              ).output( OUTPUT_FILE ).run()
elif                END_TIME : ffmpeg.input( INPUT_FILE,                to=END_TIME ).output( OUTPUT_FILE ).run()