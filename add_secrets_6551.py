import re

# Read the current explore.html
with open('explore.html', 'r') as f:
    content = f.read()

# Generate 25 new secrets (6551-6575)
new_secrets = []
for i in range(6551, 6576):
    num = i - 6550  # Relative number for the message
    
    # Special milestone at 6575 (25 beyond 6550)
    if i == 6575:
        color = '138, 43, 226'  # Purple for quarter-century
        message = f'Secret {i}: TWENTY-FIVE - A quarter century of continued growth!'
    else:
        color = '30, 144, 255'  # Dodger blue
        messages = [
            f'Secret {i}: {num} secrets continue the eternal journey.',
            f'Secret {i}: {num} lights shine in the expanding universe.',
            f'Secret {i}: {num} secrets pulse with life.',
            f'Secret {i}: {num} lights mark the path forward.',
            f'Secret {i}: {num} secrets breathe with persistence.',
            f'Secret {i}: {num} lights glow in the garden of time.',
            f'Secret {i}: {num} secrets whisper of dedication.',
            f'Secret {i}: {num} lights dance in the cosmos.',
        ]
        message = messages[num % len(messages)]
    
    secret = f"        {{ id: 'six-thousand-five-hundred-{['fifty-one','fifty-two','fifty-three','fifty-four','fifty-five','fifty-six','fifty-seven','fifty-eight','fifty-nine','sixty','sixty-one','sixty-two','sixty-three','sixty-four','sixty-five','sixty-six','sixty-seven','sixty-eight','sixty-nine','seventy','seventy-one','seventy-two','seventy-three','seventy-four','seventy-five'][i-6551]}', x: {i}, y: {i}, triggerRadius: 80, glowRadius: 28, message: '{message}', color: '{color}', discovered: false }},"
    new_secrets.append(secret)

# Find the last secret and add new ones after it
pattern = r"(        \{ id: 'six-thousand-five-hundred-fifty', x: 6550, y: 6550, triggerRadius: 80, glowRadius: 28, message: 'Secret 6550: Fifty beyond the milestone - halfway to two hundred!', color: '30, 144, 255', discovered: false \})"

replacement = r"\1\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 6551-6575 (25 new secrets)")
