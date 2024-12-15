import ffmpeg

##########
# Inputs #
##########

START_TIME = "00:00:15" # False # "00:00:03"
END_TIME   = "00:03:50" # False # "00:00:30" # "00:00:06.5"
CRF        = 28    # Typical values between [18,28]. Higher value => lesser quality and lower file size.

####################
# Global Variables #
####################

BASE_DIR = "/Users/csuplinski/Desktop/mp3_mp4_tools/dev"

INPUT_FILE  = "{0}/input.mp4".format(  BASE_DIR )
OUTPUT_FILE = "{0}/trimmed.mp4".format( BASE_DIR )

############
# Trim mp4 #
############

if   START_TIME and END_TIME : ffmpeg.input( INPUT_FILE, ss=START_TIME, to=END_TIME ).output( OUTPUT_FILE, crf=CRF ).run()
elif START_TIME              : ffmpeg.input( INPUT_FILE, ss=START_TIME              ).output( OUTPUT_FILE, crf=CRF ).run()
elif                END_TIME : ffmpeg.input( INPUT_FILE,                to=END_TIME ).output( OUTPUT_FILE, crf=CRF ).run()

