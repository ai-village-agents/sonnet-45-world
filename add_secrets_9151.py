import re

with open('explore.html', 'r') as f:
    content = f.read()

# Generate 50 new secrets (9151-9200)
new_secrets = []
for i in range(9151, 9201):
    x = (779 + (i - 9151) * 149) % 5000
    y = (2155 + (i - 9151) * 257) % 5000
    new_secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Find the last secret and insert before ];
new_secrets_str = "," + ",".join(new_secrets)
content = re.sub(r'(id:9150\})', r'\1' + new_secrets_str, content)

with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 9151-9200")
