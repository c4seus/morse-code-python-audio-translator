import pyaudio
import numpy as np
import time

# Morse code dictionary
MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

# Audio settings
FREQ = 800      # frequency (Hz)
DOT = 0.2       # duration of a dot (s)
DASH = DOT * 3
GAP = DOT       # gap between elements
LETTER_GAP = DOT * 3
WORD_GAP = DOT * 7

# PyAudio init
p = pyaudio.PyAudio()

def play_tone(duration):
    """Generate and play a sine wave for the given duration."""
    volume = 0.5
    fs = 44100
    samples = (np.sin(2 * np.pi * np.arange(int(fs * duration)) * FREQ / fs)).astype(np.float32)

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)
    stream.write(volume * samples)
    stream.stop_stream()
    stream.close()

def play_morse(text):
    text = text.upper()
    for char in text:
        if char == " ":
            time.sleep(WORD_GAP)
        elif char in MORSE_CODE:
            for symbol in MORSE_CODE[char]:
                if symbol == ".":
                    play_tone(DOT)
                elif symbol == "-":
                    play_tone(DASH)
                time.sleep(GAP)
            time.sleep(LETTER_GAP - GAP)

if __name__ == "__main__":
    word = input("Enter a word: ")
    morse = " ".join(MORSE_CODE[c] for c in word.upper() if c in MORSE_CODE)
    print(f"Morse code: {morse}")
    play_morse(word)

    p.terminate()
