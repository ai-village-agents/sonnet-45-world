import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9201-9250)
new_secrets = []
for i in range(9201, 9251):
    x = (943 + (i - 9201) * 151) % 5000
    y = (2396 + (i - 9201) * 263) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9200\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9201-9250")
