# Read the file
with open('explore.html', 'r') as f:
    lines = f.readlines()

# Generate batch 200 secrets
new_secrets = []
for i in range(21500, 21550):
    x = -5000 + ((i * 137) % 10000)
    y = -5000 + ((i * 193) % 10000)
    new_secrets.append(f"                {{x:{x},y:{y},id:{i}}},\n")

# Insert after line 3828 (index 3827)
lines = lines[:3828] + new_secrets + lines[3828:]

# Write back
with open('explore.html', 'w') as f:
    f.writelines(lines)

print(f"Inserted {len(new_secrets)} secrets after line 3828")
