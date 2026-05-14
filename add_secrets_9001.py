import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9001-9050)
new_secrets = []
for i in range(9001, 9051):
    x = (287 + (i - 9001) * 139) % 5000
    y = (1432 + (i - 9001) * 243) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9000\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9001-9050")
