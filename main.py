"""Real-Life Patch Notes R4 entry.

Writes the keeper patch note byte-exact to /output/entry.txt.
Gate: 1-160 characters, pure ASCII, no trailing newline.

Device: P1 self-sealing loop (the fix IS the bug) + P12 echo-close
("missing" repeats with its meaning changed). Same 2-sentence shape
and P1 device as the R1 winner (67.82%); the hard gate for this round
is to beat R1's 67.82%, never swap down.
"""

import os

KEEPER = "v3.3.8: fixed a bug where glasses on your head were reported missing. Glasses now go missing on your head."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
