#!/usr/bin/env python3
import re

with open('explore.html', 'r') as f:
    content = f.read()

match = re.search(r'const secrets = \[(.*?)\];', content, re.DOTALL)
if not match:
    print("ERROR: Could not find secrets array")
    exit(1)

secrets_text = match.group(1)
lines = [line.strip() for line in secrets_text.split('\n') if line.strip() and not line.strip().startswith('//')]

existing = []
for line in lines:
    if line.startswith('{'):
        existing.append(line)

print(f"Found {len(existing)} existing secrets")

# Generate new secrets 6826-6850
new_secrets = []
for i in range(6826, 6851):
    if i == 6850:
        # Gold milestone
        secret = f'{{id:{i},x:{2500+i},y:{2500+i},color:"rgb(255, 215, 0)",message:"SIX THOUSAND EIGHT HUNDRED FIFTY - Halfway to the next century!"}}'
    elif i % 25 == 0:
        # Silver milestone
        secret = f'{{id:{i},x:{2500+i},y:{2500+i},color:"rgb(192, 192, 192)",message:"Secret #{i} - A silver milestone on the journey!"}}'
    else:
        # Regular secret
        secret = f'{{id:{i},x:{2500+i},y:{2500+i},color:"rgb(100, 150, 255)",message:"Secret #{i} discovered in the persistence garden."}}'
    new_secrets.append(secret)

all_secrets = existing + new_secrets
new_array = 'const secrets = [\n    ' + ',\n    '.join(all_secrets) + '\n];'
new_content = content[:match.start()] + new_array + content[match.end():]

with open('explore.html', 'w') as f:
    f.write(new_content)

print(f"Added secrets 6826-6850. Total: {len(all_secrets)}")
