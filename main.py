"""Write the entry for make.fun "Texts From Your Future Self".

The entry is a single text message from the entrant's future self,
under 200 characters (gate: 1-200). It is written to
$MAKEFUN_OUTPUT_DIR/entry.txt and is byte-identical on every run.
"""

import os
from pathlib import Path

ENTRY = (
    "Future you: the gym membership auto-renews for 20 years. "
    "You go twice. Cancel it now and buy the good chair "
    "\u2014 your back will thank me. It already does."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
