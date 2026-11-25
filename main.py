"""One Line, One Chill — entry for make.fun.

Writes one line to /output/entry.txt. The line is the single scariest sentence we can write, under 200 characters.
"""
import os

LINE = "The voice in the attic stopped whispering my name the night I realised it had been learning to sound exactly like me."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
