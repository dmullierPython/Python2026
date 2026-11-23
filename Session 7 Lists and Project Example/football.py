# football.py
# V1.0 Simple list of matches
# V2.0 Added processing of matches to print out the match results in the correct format
# V3.0 Can now handle case where there aren't the correct number of fields.
# V4.0 determines who won/lost
# V5.0 Added error handling for invalid score data
# V6.0 totting up the points
# V7.0 read from a file instead of hard coding the matches in the program
# V8.0 Added a full league table.

import sys

def new_team_stats() -> dict[str, int]:
    """Return a fresh statistics record for a team."""
    return {
        "played": 0,
        "won": 0,
        "drawn": 0,
        "lost": 0,
        "gf": 0,
        "ga": 0,
        "points": 0,
    }


table: dict[str, dict[str, int]] = {}

try:
    with open("matches.txt", encoding="utf-8") as f:
        matches = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)

print(f"Loaded {len(matches)} matches.\n")

for match in matches:
    parts = match.split()
    if len(parts) != 4:
        print(f"Skipping invalid match format: {match}")
        continue

    home_team, away_team, home_raw, away_raw = parts

    try:
        home_score = int(home_raw)
        away_score = int(away_raw)
    except ValueError:
        print(f"Skipping invalid score data: {match}")
        continue

    # Ensure both teams exist in the table
    home = table.setdefault(home_team, new_team_stats())
    away = table.setdefault(away_team, new_team_stats())

    # Update matches played and goals
    home["played"] += 1
    away["played"] += 1
    home["gf"] += home_score
    home["ga"] += away_score
    away["gf"] += away_score
    away["ga"] += home_score

    # Update W/D/L and points
    if home_score > away_score:
        home["won"] += 1
        home["points"] += 3
        away["lost"] += 1
    elif home_score < away_score:
        away["won"] += 1
        away["points"] += 3
        home["lost"] += 1
    else:
        home["drawn"] += 1
        home["points"] += 1
        away["drawn"] += 1
        away["points"] += 1

# Sort by Points (desc), Goal Difference (desc), Goals For (desc), then Team Name (asc)
sorted_table = sorted(
    table.items(),
    key=lambda item: (
        -item[1]["points"],
        -(item[1]["gf"] - item[1]["ga"]),
        -item[1]["gf"],
        item[0].lower(),
    ),
)

# Print formatted league table
header = f"{'Pos':<4} {'Team':<18} {'P':>3} {'W':>3} {'D':>3} {'L':>3} {'GF':>4} {'GA':>4} {'GD':>4} {'Pts':>4}"
print(header)
print("-" * len(header))

for pos, (team, stats) in enumerate(sorted_table, start=1):
    gd = stats["gf"] - stats["ga"]
    print(
        f"{pos:<4} {team:<18} {stats['played']:>3} {stats['won']:>3} "
        f"{stats['drawn']:>3} {stats['lost']:>3} {stats['gf']:>4} "
        f"{stats['ga']:>4} {gd:>+4} {stats['points']:>4}"
    )

