import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9101-9150)
new_secrets = []
for i in range(9101, 9151):
    x = (615 + (i - 9101) * 143) % 5000
    y = (1914 + (i - 9101) * 251) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9100\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9101-9150")
