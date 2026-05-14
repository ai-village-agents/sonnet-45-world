import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9551-9600)
new_secrets = []
for i in range(9551, 9601):
    x = (2091 + (i - 9551) * 191) % 5000
    y = (4083 + (i - 9551) * 307) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9550\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9551-9600")
