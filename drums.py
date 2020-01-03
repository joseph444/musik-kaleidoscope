import pygame as pg
import sys,math
import time,random

List_Of_Drums={
    1:"Drum_beats/beat1.wav",
    2:"Drum_beats/beat2.wav",
    3:"Drum_beats/beat3.wav",
    4:"Drum_beats/beat4.wav",
    5:"Drum_beats/beat5.wav",
    6:"Drum_beats/beat6.wav",
    7:"Drum_beats/beat7.wav",
    8:"Drum_beats/beat8.wav",
    9:"Drum_beats/beat9.wav",
    10:"Drum_beats/beat10.wav",
    11:"Drum_beats/beat11.wav",
    12:"Drum_beats/beat12.wav",
    13:"Drum_beats/beat13.wav",
    14:"Drum_beats/beat14.wav",
}


def beatlen(xb):
    len=int(math.ceil(xb.get_length()))
    return len
    pass

def get_Drummer():
    random.seed(time.time()+1000)
    return random.randint(1,14)

def set_drummer():
    val=get_Drummer()
    return List_Of_Drums[val]
def setSound():
    print("Fetching Drummer...")
    musician=pg.mixer.Sound(set_drummer())
    length=beatlen(musician)
    musician.set_volume(0.2)
    print("Drummer ready!")
    return musician,length

def playDrum(tm):
    pg.mixer.init()
    stoptime=tm*60
    Drummer,length=setSound()
    channel1=pg.mixer.Channel(1)
    print("Drumming!...")
    t=time.time()
    t2=0;
    while t2<=stoptime:
        channel1.play(Drummer)
        time.sleep(length)
        t2=time.time()
        t2=t2-t

