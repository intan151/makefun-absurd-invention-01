"""Write one sentence pitching an absurd invention to /output/entry.txt.

Entry for make.fun's "One-Sentence Absurd Invention Pitch"
(competition: u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a).

Deterministic, stdlib only, no network, no clock, no environment.
Running it twice produces byte-identical output.
"""

from pathlib import Path

ENTRY = (
    "A laundry basket that folds your clothes, sighs dramatically, "
    "then files for emotional leave every time it finds a single "
    "sock with no partner."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(ENTRY) <= 220 or not ENTRY.strip():
        raise ValueError(
            f"ENTRY must be 1-220 non-blank characters, got {len(ENTRY)}"
        )
    if "\n" in ENTRY:
        raise ValueError("ENTRY must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
