import threading as th
import drums as d
import bass as b
import sys,time,math

def main():
    argv=sys.argv[1:]
    try:
        tm=float(argv[0])
        pass
    except:
        print("Usage: python3 kaledescope.py <minute>")
        sys.exit(0)
        pass
    play(tm)
    pass

def play(tm):
    tt=6
    stoptime=tm*60
    bass=th.Thread(target=b.playBass,args=(tm/2,))
    bass.setDaemon(True)
    drum=th.Thread(target=d.playDrum,args=(tm-(tt/60),))
    drum.setDaemon(True)
    t=time.time()
    t2=0
    bass.start()
    try:
        while t2<=stoptime:
            if math.floor(t2)==tt:
                drum.start()
                time.sleep(1)
                pass
            t2=time.time()-t
            pass
        pass
    except KeyboardInterrupt:
        print("\n Quiting...")
        return
        pass


def main():
    argv=sys.argv[1:]
    try:
        tm=float(argv[0])
        pass
    except:
        print(" just give a minute")
        sys.exit(0)
        pass
    play(tm)
    print("Thank you")
    pass

if __name__ == '__main__':
    main()
    