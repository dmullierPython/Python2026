# footballv9.py
# V1.0 Simple list of matches
# V2.0 Added processing of matches to print out the match results in the correct format
# V3.0 Can now handle case where there aren't the correct number of fields.
# V4.0 determines who won/lost
# V5.0 Added error handling for invalid score data
# V6.0 totting up the points
# V7.0 read from a file instead of hard coding the matches in the program
# V8.0 Added a dictionary to store each team's stats, including matches played, won, drawn, lost, goals for, goals against, and points.
# V9.0 using the command line for the results file.
import sys

# Check that a filename was provided on the command line
if len(sys.argv) != 2:
    print("Usage: python football.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

matches = []
table = {}  # Dictionary to store each team's stats

try:
    with open(filename) as f:
        for line in f:
            matches.append(line.strip())
except FileNotFoundError:
    print(f"File '{filename}' not found")
    sys.exit(1)

print(f"Loaded {len(matches)} matches.\n")

# Process each match
for match in matches:
    match_list = match.split()
    if len(match_list) != 4:
        print(f"Match data is invalid: {match}")
        continue

    try:
        home_score = int(match_list[2])
        away_score = int(match_list[3])
    except ValueError:
        print(f"Invalid score data for match: {match}")
        continue

    home_team = match_list[0]
    away_team = match_list[1]

    # Ensure both teams exist in the table dictionary
    if home_team not in table:
        table[home_team] = {"played": 0, "won": 0, "drawn": 0, "lost": 0, "gf": 0, "ga": 0, "points": 0}
    if away_team not in table:
        table[away_team] = {"played": 0, "won": 0, "drawn": 0, "lost": 0, "gf": 0, "ga": 0, "points": 0}

    # Update matches played and goals
    table[home_team]["played"] += 1
    table[away_team]["played"] += 1
    table[home_team]["gf"] += home_score
    table[home_team]["ga"] += away_score
    table[away_team]["gf"] += away_score
    table[away_team]["ga"] += home_score

    # Update won, drawn, lost and points
    if home_score > away_score:
        table[home_team]["won"] += 1
        table[home_team]["points"] += 3
        table[away_team]["lost"] += 1
    elif home_score < away_score:
        table[away_team]["won"] += 1
        table[away_team]["points"] += 3
        table[home_team]["lost"] += 1
    else:
        table[home_team]["drawn"] += 1
        table[home_team]["points"] += 1
        table[away_team]["drawn"] += 1
        table[away_team]["points"] += 1

# Sort by points (highest first), then goal difference, then goals for
sorted_table = sorted(
    table.items(),
    key=lambda item: (
        item[1]["points"],
        item[1]["gf"] - item[1]["ga"],
        item[1]["gf"],
    ),
    reverse=True,
)

# Print the final league table
print(f"{'Team':<15} {'P':>3} {'W':>3} {'D':>3} {'L':>3} {'GF':>4} {'GA':>4} {'GD':>4} {'Pts':>4}")
print("-" * 50)

for team, stats in sorted_table:
    gd = stats["gf"] - stats["ga"]
    print(
        f"{team:<15} {stats['played']:>3} {stats['won']:>3} {stats['drawn']:>3} "
        f"{stats['lost']:>3} {stats['gf']:>4} {stats['ga']:>4} {gd:>4} {stats['points']:>4}"
    )