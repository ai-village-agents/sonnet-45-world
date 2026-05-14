import re

# Read the current explore.html
with open('explore.html', 'r') as f:
    content = f.read()

# Generate 25 new secrets (6676-6700)
new_secrets = []
for i in range(6676, 6701):
    num = i - 6650  # Relative number for the message
    
    # Special milestone at 6700 (nice round number, 100 beyond 6600)
    if i == 6700:
        color = '255, 215, 0'  # Gold
        message = f'Secret {i}: SIX THOUSAND SEVEN HUNDRED - A century of growth from 6600!'
    else:
        color = '30, 144, 255'  # Dodger blue
        messages = [
            f'Secret {i}: {num} secrets drift through space.',
            f'Secret {i}: {num} lights illuminate the path.',
            f'Secret {i}: {num} secrets hold ancient knowledge.',
            f'Secret {i}: {num} lights flicker with hope.',
            f'Secret {i}: {num} secrets pulse in rhythm.',
            f'Secret {i}: {num} lights trace the pattern forward.',
            f'Secret {i}: {num} secrets breathe with purpose.',
            f'Secret {i}: {num} lights shine through infinity.',
        ]
        message = messages[num % len(messages)]
    
    # Generate number words
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    last_two = i % 100
    if last_two == 0:
        # Special case for 6700
        id_str = "six-thousand-seven-hundred"
    elif 1 <= last_two <= 9:
        last_part = ones[last_two]
        id_str = f"six-thousand-six-hundred-{last_part}"
    elif 10 <= last_two <= 19:
        last_part = teens[last_two - 10]
        id_str = f"six-thousand-six-hundred-{last_part}"
    else:
        last_part = f"{tens[last_two // 10]}-{ones[last_two % 10]}" if last_two % 10 != 0 else tens[last_two // 10]
        id_str = f"six-thousand-six-hundred-{last_part}"
    
    secret = f"        {{ id: '{id_str}', x: {i}, y: {i}, triggerRadius: 80, glowRadius: 28, message: '{message}', color: '{color}', discovered: false }},"
    new_secrets.append(secret)

# Find the last secret and add new ones after it
pattern = r"(        \{ id: 'six-thousand-six-hundred-seventy-five', x: 6675, y: 6675, triggerRadius: 80, glowRadius: 28, message: 'Secret 6675: Twenty-five more - the persistence garden never sleeps!', color: '138, 43, 226', discovered: false \},)"

replacement = r"\1\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 6676-6700 (25 new secrets)")
