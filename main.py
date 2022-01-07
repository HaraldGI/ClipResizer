from moviepy.editor import *
import os

# Imports the moviepy module.
rawclips = "rawclips/"
directory = os.listdir(rawclips)
print("""
Video Resizer V1.0
av Harald Gimse

Dette programmet konverterer alle filer du har lagt inn i mappen "rawclips" til 800x800
slik at tegn du har laget for Milla Says ikke klippes unødig. Alle klipp blir lagt ferdig i
mappen /editedclips.
   
Det anbefales at man velger høyde på 800 og bredde på 800 for best resultat, men om ønskelig
kan dette endres.
     
Skriv ønskede parametre nedenfor:

""")

height = int(input("Høyde: "))
width = int(input("Bredde: "))
input("Trykk ENTER tasten for å starte.")
for clips in range(len(directory)):
    clip = VideoFileClip("rawclips/" + directory[clips])
    clipEdit = clip.resize((height, width))
    clipEdit.write_videofile("editedclips/rez_" + directory[clips])

input()