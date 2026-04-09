"""
Whisper-based audio transcription utilities.
"""

from pathlib import Path
import subprocess


def transcribe(
    input_media: Path,
    model: str = "medium",
    language: str | None = None,
) -> None:
    """
    Transcribe an audio or video file using Whisper CLI.

    Parameters
    ----------
    input_media : Path
        Path to audio/video file
    model : str
        Whisper model size (tiny, base, small, medium, large)
    language : str | None
        Optional ISO language code (e.g. 'en', 'de', 'fr')
    """
    if not input_media.exists():
        raise FileNotFoundError(input_media)

    cmd = [
        "whisper",
        str(input_media),
        "--model", model,
        "--output_format", "txt", "srt", "json",
    ]

    if language is not None:
        cmd += ["--language", language]

    subprocess.run(cmd, check=True)