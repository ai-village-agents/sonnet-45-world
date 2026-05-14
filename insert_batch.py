import sys

start_id = int(sys.argv[1])
end_id = int(sys.argv[2])

# Read the file
with open('explore.html', 'r') as f:
    lines = f.readlines()

# Find the line with the last id
search_id = start_id - 1
target_line = None
for idx, line in enumerate(lines):
    if f'id:{search_id}}}' in line:
        target_line = idx
        break

if target_line is None:
    print(f"ERROR: Could not find id:{search_id}")
    exit(1)

# Generate new secrets
new_secrets = []
for i in range(start_id, end_id):
    x = -5000 + ((i * 137) % 10000)
    y = -5000 + ((i * 193) % 10000)
    new_secrets.append(f"                {{x:{x},y:{y},id:{i}}},\n")

# Insert after the found line
lines = lines[:target_line+1] + new_secrets + lines[target_line+1:]

# Write back
with open('explore.html', 'w') as f:
    f.writelines(lines)

print(f"Inserted {len(new_secrets)} secrets ({start_id}-{end_id-1}) after line {target_line+1}")
