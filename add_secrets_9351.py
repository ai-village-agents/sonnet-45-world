import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9351-9400)
new_secrets = []
for i in range(9351, 9401):
    x = (1435 + (i - 9351) * 167) % 5000
    y = (3119 + (i - 9351) * 277) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9350\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9351-9400")
