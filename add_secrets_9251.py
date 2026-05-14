import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9251-9300)
new_secrets = []
for i in range(9251, 9301):
    x = (1107 + (i - 9251) * 157) % 5000
    y = (2637 + (i - 9251) * 269) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9250\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9251-9300")
