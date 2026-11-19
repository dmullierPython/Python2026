# footballv1.py
# Simple list of matches
matches =["england iran 3 0","wales usa 1 0","england wales x 0","usa iran 2 1","england use 1","iran wales 0 5"]

print("List of matches:")
print(matches)
print(f"There are {len(matches)} matches in the list.")

#now process the matches individually.
for match in matches:
    print(f"Processing match: {match}")
    match_list = match.split(" ")
    print(f"Processing match: {match_list} has {len(match_list)} elements.")