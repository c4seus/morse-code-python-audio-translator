import numpy as np
import wave

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
FREQ = 800           # Hz
DOT = 0.2            # seconds
DASH = DOT * 3
GAP = DOT            # gap between elements
LETTER_GAP = DOT * 3
WORD_GAP = DOT * 7
SAMPLE_RATE = 44100  # samples per second

def make_tone(duration):
    t = np.linspace(0, duration, int(SAMPLE_RATE*duration), False)
    tone = 0.5 * np.sin(FREQ * 2 * np.pi * t)
    return tone

def make_silence(duration):
    return np.zeros(int(SAMPLE_RATE*duration))

def text_to_morse_wav(text, filename="output.wav"):
    text = text.upper()
    audio = np.array([], dtype=np.float32)

    for char in text:
        if char == " ":
            audio = np.concatenate((audio, make_silence(WORD_GAP)))
        elif char in MORSE_CODE:
            for symbol in MORSE_CODE[char]:
                if symbol == ".":
                    audio = np.concatenate((audio, make_tone(DOT)))
                elif symbol == "-":
                    audio = np.concatenate((audio, make_tone(DASH)))
                audio = np.concatenate((audio, make_silence(GAP)))
            audio = np.concatenate((audio, make_silence(LETTER_GAP - GAP)))

    # Convert to 16-bit PCM
    audio_int16 = (audio * 32767).astype(np.int16)

    # Write WAV file
    with wave.open(filename, "w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SAMPLE_RATE)
        f.writeframes(audio_int16.tobytes())

    print(f"Morse code audio saved to {filename}")

if __name__ == "__main__":
    word = input("Enter a word: ")
    morse = " ".join(MORSE_CODE[c] for c in word.upper() if c in MORSE_CODE)
    print(f"Morse code: {morse}")
    text_to_morse_wav(word)
