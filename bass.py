import pygame as pg
import sys,math
import time,random

List_of_Bass={
    1:"Bass_syth/bass1.wav",
    2:"Bass_syth/bass2.wav",
    3:"Bass_syth/bass3.wav",
    4:"Bass_syth/bass4.wav",
    5:"Bass_syth/bass5.wav",
    6:"Bass_syth/bass6.wav",
    7:"Bass_syth/bass7.wav",
    8:"Bass_syth/bass8.wav",
}
def beatlen(xb):
    len=int(math.floor(xb.get_length()))
    return len
    pass

def get_Bassist():
    random.seed(time.time()+1000)
    return random.randint(1,8)

def set_bassist():
    val=get_Bassist()
    return List_of_Bass[val]
def setSound():
    print("Setting Bassist...")
    musician=pg.mixer.Sound(set_bassist())
    musician.set_volume(0.09)
    length=beatlen(musician)
    print("Bassist Ready!")
    return musician,length

def playBass(tm):
    pg.mixer.init()
    stoptime=tm*60
    Bassist,length=setSound()
    channel0=pg.mixer.Channel(0)
    print("Bass Baby....")
    t=time.time()
    t2=0;
    while t2<=stoptime:
        channel0.play(Bassist)
        time.sleep(length)
        t2=time.time()
        t2=t2-t
        pass
    pass


