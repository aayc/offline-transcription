import argparse
import os
import speech_recognition as sr
import time
from os.path import splitext
from pydub import AudioSegment

def transcribe(infile):
    f, ext = splitext(infile)
    if ext != ".wav":
        tmp = AudioSegment.from_file(f + ext, ext.strip("."))
        tmp.export("tmp-transcript.wav", format="wav")
        infile = "tmp-transcript.wav"

    R = sr.Recognizer()
    start_time = time.time()
    with sr.AudioFile(infile) as src:
        audio = R.record(src)
        print("Transcribing...")
        print("Since this process is happening offline, it could take quite a while...")
        transcription = R.recognize_sphinx(audio)
        
        if os.path.exists("tmp-transcript.wav"):
            os.remove("tmp-transcript.wav")

        print("Elapsed (s): ", time.time() - start_time)
    return transcription

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="audio file to transcribe (mp3, wav, m4a, etc. supported)", type=str)
    parser.add_argument("--output", default="output.txt", help="output file name of transcription file (e.g., output.txt)", type=str)
    args = parser.parse_args()

    transcription = transcribe(args.input_file)
    with open(args.output, "w") as f:
        f.write(transcription)

    print("Successfully wrote transcription to", args.output)
