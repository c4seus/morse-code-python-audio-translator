# morsepy
This project is a simple Python tool that converts any text or word into Morse code and plays it back as audio beeps.

## Features
* Converts text into international Morse code.
* Plays Morse code as sound (short and long beeps).
* Adjustable tone frequency and timing (dot, dash, gaps).
* Works offline with pure Python.

## Example
```bash
Enter a word: SOS

Output:
Morse code: ... --- ...
```

The program will play the Morse code as short and long beeps.

## Requirements
* Python 3.x
* winsound (Windows only) or simpleaudio for cross-platform support.
