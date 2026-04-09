# Audio Transcriber

This project provides a simple audio transcription workflow using Python.

## Prerequisites

Before running the code, make sure the following dependencies are installed on your system:

### 1. `uv` (Python package manager)

`uv` is used to manage the Python environment and dependencies.

- Installation guide: https://docs.astral.sh/uv/getting-started/installation/

### 2. `ffmpeg`

`ffmpeg` is required for audio and video processing.

- Download page: https://ffmpeg.org/download.html

## System PATH

Ensure that **both `uv` and `ffmpeg` are available in your system `PATH`**.

You can verify the installations by running:

```sh
uv --version
ffmpeg -version
```
## How to Run

### Install dependencies

From the root directory of the repository, synchronize the Python environment:
```sh
uv sync
```
This will create the virtual environment and install all required dependencies as defined in `pyproject.toml`.

### Transcribe an audio or video file

Provide the path to an audio or video file containing the audio to transcribe.

Example (Windows / PowerShell):
```sh
$in = "C:\Users\...\Videos\2026-04-08 18-57-19.mkv"
uv run whisper $in --model medium --output_format all --output_dir .
```
## Output

The transcription results will be written to the current directory.

Typical output formats include:

- .txt
- .srt
- .json

## Notes

- The input file may be audio or video, as long as it contains an audio track.
- The medium model provides a good balance between accuracy and performance.
- ffmpeg is automatically used by Whisper to extract audio from video files.
