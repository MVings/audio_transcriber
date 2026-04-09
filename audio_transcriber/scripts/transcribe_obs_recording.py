"""
CLI wrapper for transcribing OBS recordings.
"""

from pathlib import Path
import sys

from audio_transcriber.transcribe import transcribe


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: transcribe_obs_recording.py <media_file>")

    media = Path(sys.argv[1]).resolve()

    transcribe(
        input_media=media,
        model="medium",
        language=None,   # auto-detect
    )


if __name__ == "__main__":
    main()