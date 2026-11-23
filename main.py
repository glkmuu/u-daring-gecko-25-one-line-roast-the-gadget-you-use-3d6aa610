"""One-line roast entry: writes a single roast of a daily gadget to entry.txt.

The roast is a fixed, deterministic string: one line, 73 characters,
roasting the toaster I use every morning. No network, no randomness,
no dependencies beyond the standard library, so every run writes
the exact same bytes.
"""

import os

ROAST = "My toaster has two settings: warm bread, and charcoal with a smoke alarm."


def main() -> None:
    # The gate allows 1-200 characters, one line, not only whitespace.
    if not 1 <= len(ROAST) <= 200 or "\n" in ROAST or not ROAST.strip():
        raise ValueError("roast does not meet the 1-200 character, one-line gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ROAST)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
