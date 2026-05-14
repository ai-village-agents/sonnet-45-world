import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (8951-9000)
new_secrets = []
for i in range(8951, 9001):
    x = (123 + (i - 8951) * 137) % 5000
    y = (1191 + (i - 8951) * 241) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:8950\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 8951-9000")
