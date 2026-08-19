from typing import List, Dict, Any
import re


def extract_speaker(line: str) -> str | None:
    """
    Extracts the speaker name from a speaker line.
    Returns None if the line is not a speaker line.
    """

    patterns = [
        r"^([A-Za-z ]+):$",                       # John:
        r"^([A-Za-z ]+)\s*\(\d{1,2}:\d{2}\):$",  # John (00:10):
        r"^\[([A-Za-z ]+)\]$",                    # [John]
        r"^(Speaker\s+\d+):$",                    # Speaker 1:
    ]

    for pattern in patterns:
        match = re.match(pattern, line.strip())

        if match:
            return match.group(1).strip()

    return None


def is_speaker_line(line: str) -> bool:
    """
    Returns True if the line represents a speaker.
    """

    return extract_speaker(line) is not None


def chunk_text(
    text: str,
    source_file: str,
) -> List[Dict[str, Any]]:
    """
    Splits a meeting transcript into speaker-based chunks
    and attaches metadata to each chunk.
    """

    lines = text.splitlines()

    chunks = []

    current_chunk = []
    current_speaker = "Unknown"
    chunk_index = 0

    for line in lines:

        if is_speaker_line(line):

            if current_chunk:

                chunks.append({
                    "text": "\n".join(current_chunk).strip(),

                    "metadata": {
                        "speaker_name": current_speaker,
                        "source": source_file,
                        "chunk_index": chunk_index,
                    }
                })

                chunk_index += 1

            current_speaker = extract_speaker(line)
            current_chunk = [line]

        else:

            current_chunk.append(line)

    if current_chunk:

        chunks.append({
            "text": "\n".join(current_chunk).strip(),

            "metadata": {
                "speaker_name": current_speaker,
                "source": source_file,
                "chunk_index": chunk_index,
                
            }
        })

    return chunks