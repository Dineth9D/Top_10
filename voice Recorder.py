import sounddevice
from scipy.io.wavfile import write

fs = 44100

# Ask to enter the recording time
second = int(input("Enter the Recording Time(Seconds): "))
print("Recording...\n")

record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()

write("MyRecording.wav", fs, record_voice)
print("Recording is completed. Please check the current directory to listen recording.")
