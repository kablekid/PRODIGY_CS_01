import getopt
import sys


argumentList = sys.argv[1:] # remove the first argument which is the name of the program
Options = "edms:"
LongOptions = ["encrypt","decrypt","message","step"]

def ceaserCipher(process="",message="",step=0):
   cipher = ""
   for i in message:
      if process == "encrypt":
         number = ord(i) + step
         cipher += chr(number)
      elif process == "decrypt":
         number = ord(i) - step
         cipher += chr(number)
   return cipher   



try:
   arguments, values = getopt.getopt(argumentList,Options,LongOptions)

   process,message,step = "","",""
   for CurrentArguemt,CurrentValue in arguments:
      print(CurrentArguemt+ "  " + CurrentValue)
      if CurrentArguemt in ("-e","--encrypt"):
         process = "encrypt"
      elif CurrentArguemt in ("-d","--decrypt"):
         process = "decrypt"
      elif CurrentArguemt in ("-m","--message"):
         message = CurrentValue
      elif CurrentArguemt in ("-s","--step"):
         step = CurrentValue
   
 

except getopt.error as error:
   print("Error has occuerd check your arguments")


