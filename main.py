"""Ridiculous at First Glance, Real by the Second — entry program.

Writes a single one-sentence startup pitch (at most 200 characters) to
/output/entry.txt. The pitch is a fixed string: the program's whole job is
to deliver that sentence, validated, to the file the gate reads.
"""

from pathlib import Path

# One sentence, 151 characters. A seagull-theft service for phone addicts:
# absurd on its face, but the customer (screen-time addicts who have tried
# every app blocker and failed) and the payment (a rental fee for a thief
# you cannot argue with, sweet-talk, or uninstall) are both concrete.
PITCH = (
    "We rent trained seagulls to snatch your phone mid-scroll and drop it "
    "in a lockbox, paid by screen-time addicts who need a thief they "
    "cannot argue with."
)

MAX_CHARS = 200


def main() -> None:
    text = PITCH.strip()
    if not text:
        raise SystemExit("pitch is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"pitch is {len(text)} characters, over the 200 limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    if "\n" in text or "\r" in text:
        raise SystemExit("pitch must be a single line")

    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    # Read it back: the gate reads this exact file, so confirm what landed
    # on disk is byte-for-byte the pitch we validated above.
    if out_path.read_text(encoding="utf-8") != text:
        raise SystemExit("entry.txt on disk does not match the pitch")
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
