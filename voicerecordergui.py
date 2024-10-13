# voice recorder gui.
import sounddevice as sd # used to provide functions to record and operate numpy arrays containing audio signals.
import soundfile as sf# used to store the recorded audio
from tkinter import *


def voice_rec():
    freq=48000
    duration=5

    recording=sd.rec(int(duration*freq),samplerate=freq,channels=2)

    sd.wait()
    return sf.write("myaudio.flac",recording,freq)

master = Tk() #Tk is  library of basic elements og gui widgets used for graphic user interface.
  
Label(master, text=" Voice Recoder : "  # label in python is used to specify container box where we will enter text or input.
     ).grid(row=0, sticky=W, rowspan=5) # rowspan or column span is used to specify the number of rows or columns in the cont. box
  
  
b = Button(master, text="Start", command=voice_rec) 
b.grid(row=0, column=2, columnspan=2, rowspan=2,padx=5,pady=5) #padx is used to put some space between button wigets and close button and borders of root window.   padx=5, pady=5) 
       
  # pady is used to put some space between button widgets and bordes of frame and border of root window.
mainloop()# its used to execute what we use to wish in an application.


