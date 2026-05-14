import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9501-9550)
new_secrets = []
for i in range(9501, 9551):
    x = (1927 + (i - 9501) * 181) % 5000
    y = (3842 + (i - 9501) * 293) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9500\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9501-9550")
