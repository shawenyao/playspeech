import os
import glob
import time
import pygame
from server_config import dir

pygame.mixer.init()

files = glob.glob(dir + '/played/*.mp3')
for f in files:
    os.remove(f)
files = glob.glob(dir + '/unplayed/*.mp3')
for f in files:
    os.remove(f)
files = glob.glob(dir + '/temp/*.mp3')
for f in files:
    os.remove(f)

os.chdir(dir + "/unplayed")

while True:
    time.sleep(0.1)
    for file in sorted(glob.glob("*.mp3")):
        try:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play(1)
            
            while pygame.mixer.music.get_busy() == True:
                continue
            
            os.rename(f"{dir}/unplayed/{file}", f"{dir}/played/{file}")
            os.remove(f"{dir}/played/{file}")
        except:
            pass
