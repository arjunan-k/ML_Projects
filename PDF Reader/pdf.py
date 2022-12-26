# --------------------------------Importing modules----------------------------------- #

import PyPDF2               # This module helps to read the pdf file then to extract text from it.
from gtts import gTTS       # This module helps to convert the text to Audio (mp3) format.
import os                   # This module helps to play the Audio in a player within the OS.
import pygame               # This module helps to play the Audio in the console itself.


# --------------------------------Reading the pdf file-------------------------------- #

pdfFileObj = open('DemoFile.pdf', 'rb')          # Opening the pdf file we want to convert to Audio.
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)     # Creating a pdf reader object.
print(pdfReader.numPages)                        # Printing number of pages in pdf file.
number_of_pages = pdfReader.numPages             # Saving number of pages.

text = ""                                        # Creating a empty string.
for each in range(number_of_pages):              # Looping through each pages.
    pageObj = pdfReader.getPage(each)            # Getting the required page in pdf to convert.
    print(pageObj.extractText())                 # Printing the text in that page.
    text += pageObj.extractText()                # Adding it to the string.

pdfFileObj.close()                               # closing the pdf file object


# --------------------------------Creating Audio from text---------------------------- #

language = 'en'
# Language in which the text is written.
myobj = gTTS(text=text, lang=language, slow=False)
# Passing the text and language to the engine. slow=False means, converted audio have high speed.
myobj.save("welcome.mp3")
# Saving the converted audio in a mp3 file format.


# --------------------------------Playing the music using 2 methods------------------- #

# Playing the converted file with a music player inside the OS.
os.system("welcome.mp3")

# Playing the converted file within console itself.
pygame.mixer.init()                         # Initializing the player module.
pygame.mixer.music.load("welcome.mp3")      # Opening the Audio file.
pygame.mixer.music.set_volume(1)            # Setting volume.
pygame.mixer.music.play(loops=0)            # Setting loops of play.
while pygame.mixer.music.get_busy():        # Waiting for the music to play using while loop.
    pygame.time.Clock().tick(10)
