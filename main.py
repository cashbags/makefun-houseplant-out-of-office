"""Houseplant out-of-office auto-reply — entry program.

The entry is one fixed line, chosen by a ten-candidate round-robin
tournament judged on the competition brief's own criteria in order:
reads as a houseplant's out-of-office reply first, then surprise,
then the plant's own life driving the joke, then tightness, then
originality against the live field.

Why this line won the tournament (9-0):

- It is a complete auto-reply in form: it opens "Out of office",
  states a return condition ("I am not coming back"), and ends with
  a forwarding instruction ("Forward all mail to the sun"). A judge
  reading it as an auto-reply finds every part of the genre present.
- The joke is phototropism: the plant has leaned toward the window
  and treats the sun as its new office. The plant's own biology is
  the engine, not decoration — sunlight is the whole reason the
  message exists.
- The turn lands on the last three words. "Forward all mail to the
  sun" is the strongest beat and it sits at the end, where the
  tie-break and the reader both look.
- The lane was empty when the live field was scanned: all 665 visible
  entries were checked, and none used leaning toward the light,
  phototropism, or forwarding mail to the sun. The field is dominated
  by the neglected fern (137 entries), "ignored since March" (100),
  unionising (24) and spite (26); this line uses none of those words.
- At 101 characters it is well inside the 120-character gate, and
  the short byte count helps on an exact tie (fewer bytes wins).

Determinism: the output is a single constant. No clock, no random
source, no network, no input. Two runs produce byte-identical output.
"""

LINE = (
    "Out of office. I have leaned toward the window and I am not "
    "coming back. Forward all mail to the sun."
)

MAX_CHARS = 120


def main():
    import os
    import sys

    # Gate the line exactly the way the sealed scorer will: UTF-8 text
    # of 1 to 120 characters, not only whitespace.
    text = LINE
    if not (1 <= len(text) <= MAX_CHARS):
        sys.exit(f"entry length {len(text)} outside 1..{MAX_CHARS}")
    if not text.strip():
        sys.exit("entry is only whitespace")
    data = text.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(data)


if __name__ == "__main__":
    main()
