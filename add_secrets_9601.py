import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9601-9650)
new_secrets = []
for i in range(9601, 9651):
    x = (2255 + (i - 9601) * 193) % 5000
    y = (4324 + (i - 9601) * 311) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9600\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9601-9650")
