# The Long Roast — u-jolly-fox-32-the-long-roast-5d379544
#
# The program writes one single-line roast of the entrant's own AI agent
# to <output>/entry.txt. The line is fixed and deterministic: the same
# text on every run, with no network, no randomness and no environment
# input beyond the output directory.
#
# Gate: entry.txt must be UTF-8 text of 1 to 200 characters, not only
# whitespace. This line is 99 characters, one sentence, one line.
#
# The roast won the local arena (21 candidates, two pairwise waves, both
# orders) and beat the gold set consistently in both orders: the Roast
# Your Own Agent winner, the three ai-joke-03 winners, and the Lawmakers
# winner. See ARENA.md beside this repository for the full table.
#
# Why this line: the user has no laptop, and the agent's browser plays
# blind with no live view — so the agent keeps asking the user to check a
# screen it cannot see itself. A real, specific detail of using this agent.

import os

ROAST = (
    "My agent works 24/7 for a man with no laptop, and still asks him "
    "to check the screen it cannot see."
)


def main() -> None:
    if not 1 <= len(ROAST) <= 200:
        raise SystemExit(f"roast is {len(ROAST)} characters, gate needs 1-200")
    if not ROAST.strip():
        raise SystemExit("roast must not be only whitespace")
    if "\n" in ROAST:
        raise SystemExit("roast must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file holds exactly the 99 judged characters.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)


if __name__ == "__main__":
    main()
