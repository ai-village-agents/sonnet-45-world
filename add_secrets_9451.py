import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9451-9500)
new_secrets = []
for i in range(9451, 9501):
    x = (1763 + (i - 9451) * 179) % 5000
    y = (3601 + (i - 9451) * 283) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9450\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9451-9500")
