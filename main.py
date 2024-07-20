import getopt
import sys


argumentList = sys.argv[1:] # remove the first argument which is the name of the program
Options = "edm:"
LongOptions = ["encrypt","decrypt","message"]

def ceaserCipher(process,message):
   pass

try:
   arguments, values = getopt.getopt(argumentList,Options,LongOptions)


   for CurrentArguemt,CurrentValue in arguments:
      
      if CurrentArguemt in ("-e","--encrypt"):
         ceaserCipher(CurrentArguemt,)
      elif CurrentArguemt in ("-d","--decrypt"):
         pass

except getopt.error as error:
   print("Error has occuerd check your arguments")


