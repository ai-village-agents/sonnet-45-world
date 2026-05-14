import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9301-9350)
new_secrets = []
for i in range(9301, 9351):
    x = (1271 + (i - 9301) * 163) % 5000
    y = (2878 + (i - 9301) * 271) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9300\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9301-9350")
