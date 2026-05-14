# Read the file
with open('explore.html', 'r') as f:
    lines = f.readlines()

# Find the line with id:21549
target_line = None
for idx, line in enumerate(lines):
    if 'id:21549}' in line:
        target_line = idx
        break

if target_line is None:
    print("ERROR: Could not find id:21549")
    exit(1)

# Generate batch 201 secrets
new_secrets = []
for i in range(21550, 21600):
    x = -5000 + ((i * 137) % 10000)
    y = -5000 + ((i * 193) % 10000)
    new_secrets.append(f"                {{x:{x},y:{y},id:{i}}},\n")

# Insert after the found line
lines = lines[:target_line+1] + new_secrets + lines[target_line+1:]

# Write back
with open('explore.html', 'w') as f:
    f.writelines(lines)

print(f"Inserted {len(new_secrets)} secrets (21550-21599) after line {target_line+1}")
