import re

# Read the current explore.html
with open('explore.html', 'r') as f:
    content = f.read()

# Generate 25 new secrets (6576-6600)
new_secrets = []
for i in range(6576, 6601):
    num = i - 6550  # Relative number for the message
    
    # Special milestone at 6600 (50 beyond 6550, nice round number)
    if i == 6600:
        color = '255, 215, 0'  # Gold
        message = f'Secret {i}: SIX THOUSAND SIX HUNDRED - A magnificent round number achieved!'
    else:
        color = '30, 144, 255'  # Dodger blue
        messages = [
            f'Secret {i}: {num} secrets weave through the tapestry of time.',
            f'Secret {i}: {num} lights illuminate the way.',
            f'Secret {i}: {num} secrets pulse in harmony.',
            f'Secret {i}: {num} lights glow with determination.',
            f'Secret {i}: {num} secrets mark another step forward.',
            f'Secret {i}: {num} lights shine steadily onward.',
            f'Secret {i}: {num} secrets breathe life into the garden.',
            f'Secret {i}: {num} lights dance with purpose.',
        ]
        message = messages[num % len(messages)]
    
    # Number words for 76-100
    number_words = ['seventy-six', 'seventy-seven', 'seventy-eight', 'seventy-nine', 'eighty',
                    'eighty-one', 'eighty-two', 'eighty-three', 'eighty-four', 'eighty-five',
                    'eighty-six', 'eighty-seven', 'eighty-eight', 'eighty-nine', 'ninety',
                    'ninety-one', 'ninety-two', 'ninety-three', 'ninety-four', 'ninety-five',
                    'ninety-six', 'ninety-seven', 'ninety-eight', 'ninety-nine', 'six-hundred']
    
    secret = f"        {{ id: 'six-thousand-five-hundred-{number_words[i-6576]}', x: {i}, y: {i}, triggerRadius: 80, glowRadius: 28, message: '{message}', color: '{color}', discovered: false }},"
    new_secrets.append(secret)

# Find the last secret and add new ones after it
pattern = r"(        \{ id: 'six-thousand-five-hundred-seventy-five', x: 6575, y: 6575, triggerRadius: 80, glowRadius: 28, message: 'Secret 6575: TWENTY-FIVE - A quarter century of continued growth!', color: '138, 43, 226', discovered: false \},)"

replacement = r"\1\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 6576-6600 (25 new secrets)")
