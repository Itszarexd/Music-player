# Music Player

This repository contains a program to play a local MP3 file and manage a simple playback checkpoint. It is intended as a teaching or demo project for a fault-tolerant computing / music player exercise.

## Features

- Play a local MP3 file (`musica.mp3`).
- Show or use a cover image (`portada.jpg`).
- Store a checkpoint (`checkpoint_player.pkl`) to remember playback state (seek position, playlist index, or other small state data).
- Single-file entry point: `main.py`.

## Usage

1. Install Python 3.8+ (recommended).
2. (Optional) Create and activate a virtual environment.
3. Install dependencies if any are needed (e.g., `pip install -r requirements.txt`).
4. Run the player:

```bash
python main.py
```

Running `main.py` should start the program and play the bundled `musica.mp3` file. If the program expects command-line arguments, consult `main.py` or add usage examples here.



<img width="502" height="537" alt="image" src="https://github.com/user-attachments/assets/93d0362f-cebd-4c93-bb72-ee978694ccd1" />


## Files in this repo

- `main.py` — program entry point.
- `musica.mp3` — example audio file used by the player.
- `portada.jpg` — cover image used by the program.
- `checkpoint_player.pkl` — serialized playback state used by the player (if present).
- `README.md` — this file.

