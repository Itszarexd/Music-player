# Music Player

A small local music player project written in Python.

This repository contains a minimal program to play a local MP3 file and manage a simple playback checkpoint. It is intended as a teaching or demo project for a fault-tolerant computing / music player exercise.

## Features

- Play a local MP3 file (`musica.mp3`).
- Show or use a cover image (`portada.jpg`).
- Store a checkpoint (`checkpoint_player.pkl`) to remember playback state (seek position, playlist index, or other small state data).
- Single-file entry point: `main.py`.

## Assumptions

- The project uses plain Python (no explicit dependency file provided). The code may rely on standard libraries or lightweight audio libraries (for example, `pygame`, `playsound`, or `pydub`). If dependencies are required, they should be listed in `requirements.txt`.
- `main.py` is the program entry point and will attempt to load `musica.mp3` and `portada.jpg` from the repository root.

If any of these assumptions are wrong, update this README or add a `requirements.txt` with the exact dependencies.

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

## Next steps / Recommendations

- Add a `requirements.txt` listing runtime dependencies.
- Add a `.gitignore` to exclude `__pycache__/`, virtualenv directories, and large media files if you prefer not to store them in Git.
- Run `git init` and push to a remote GitHub repository (e.g., `https://github.com/Itszarexd/Music-player.git`).
- Consider adding a short CONTRIBUTING guide or usage examples in `README.md` showing CLI options or a GUI description if applicable.

## License

Specify a license (for example, MIT) in a `LICENSE` file if you intend to reuse or publish this code.
