from pydub import AudioSegment

##########
# Inputs #
##########

# Times are in milliseconds (ex: 12000 == 12 seconds)
# Set to START_TIME to False to trim from beginning
# Set to   END_TIME to False to trim to the end
START_TIME = 1000
END_TIME   = False # 20000

####################
# Global Variables #
####################

BASE_DIR = "/Users/csuplinski/Desktop/mp3_mp4_tools/dev"

INPUT_FILE  = "{0}/input.mp3".format(  BASE_DIR )
OUTPUT_FILE = "{0}/trimmed.mp3".format( BASE_DIR )

############
# Trim mp3 #
############

audio = AudioSegment.from_file( INPUT_FILE, format="mp3" )

trimmed_audio = audio
if   END_TIME is not False : trimmed_audio = trimmed_audio[ : END_TIME ]
if START_TIME is not False : trimmed_audio = trimmed_audio[ START_TIME : ]

trimmed_audio.export( OUTPUT_FILE, format="mp3" )

