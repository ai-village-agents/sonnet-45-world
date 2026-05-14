import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9701-9750)
new_secrets = []
for i in range(9701, 9751):
    x = (2583 + (i - 9701) * 199) % 5000
    y = (4806 + (i - 9701) * 317) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9700\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9701-9750")
