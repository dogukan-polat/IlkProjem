import sounddevice as sd
from scipy.io.wavfile import write

def record_voice():
    frequency = 44100
    while True:
        try:
            secs = int(input("How long do you want to record(in seconds): "))
            break
        except:
            print("Type an integer!!!")
    my_record = sd.rec(int(secs*frequency), samplerate=frequency, channels=2)
    sd.wait()
    write("recorded_voice.wav",frequency, my_record)