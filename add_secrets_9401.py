import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9401-9450)
new_secrets = []
for i in range(9401, 9451):
    x = (1599 + (i - 9401) * 173) % 5000
    y = (3360 + (i - 9401) * 281) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9400\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9401-9450")
