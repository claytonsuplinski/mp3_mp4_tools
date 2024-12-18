import ffmpeg
import os

##########
# Inputs #
##########

START_TIME = False
END_TIME   = False
CRF        = 28    # Typical values between [18,28]. Higher value => lesser quality and lower file size.

# START_TIME = "00:00:02" 
END_TIME   = "00:00:02" # "00:00:06.5"

####################
# Global Variables #
####################

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DEV_DIR  = '{0}/dev'.format( BASE_DIR )

INPUT_FILE  = "{0}/input.mp4".format(   DEV_DIR )
OUTPUT_FILE = "{0}/trimmed.mp4".format( DEV_DIR )

############
# Trim mp4 #
############

if   START_TIME and END_TIME : ffmpeg.input( INPUT_FILE, ss=START_TIME, to=END_TIME ).output( OUTPUT_FILE, crf=CRF ).run()
elif START_TIME              : ffmpeg.input( INPUT_FILE, ss=START_TIME              ).output( OUTPUT_FILE, crf=CRF ).run()
elif                END_TIME : ffmpeg.input( INPUT_FILE,                to=END_TIME ).output( OUTPUT_FILE, crf=CRF ).run()

