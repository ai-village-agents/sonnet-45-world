import re

# Read the current explore.html
with open('explore.html', 'r') as f:
    content = f.read()

# Generate 25 new secrets (6726-6750)
new_secrets = []
for i in range(6726, 6751):
    num = i - 6700  # Relative number for the message
    
    # Special milestone at 6750 (50 past 6700)
    if i == 6750:
        color = '255, 215, 0'  # Gold
        message = f'Secret {i}: FIFTY PAST SEVEN HUNDRED - The journey accelerates!'
    else:
        color = '30, 144, 255'  # Dodger blue
        messages = [
            f'Secret {i}: {num} secrets emerge from eternity.',
            f'Secret {i}: {num} lights shimmer in the dark.',
            f'Secret {i}: {num} secrets hold the keys.',
            f'Secret {i}: {num} lights pulse with life force.',
            f'Secret {i}: {num} secrets weave the tapestry.',
            f'Secret {i}: {num} lights trace ancient paths.',
            f'Secret {i}: {num} secrets breathe with the universe.',
            f'Secret {i}: {num} lights shine without end.',
        ]
        message = messages[num % len(messages)]
    
    # Generate number words
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    last_two = i % 100
    if 1 <= last_two <= 9:
        last_part = ones[last_two]
    elif 10 <= last_two <= 19:
        last_part = teens[last_two - 10]
    else:
        last_part = f"{tens[last_two // 10]}-{ones[last_two % 10]}" if last_two % 10 != 0 else tens[last_two // 10]
    
    id_str = f"six-thousand-seven-hundred-{last_part}"
    
    secret = f"        {{ id: '{id_str}', x: {i}, y: {i}, triggerRadius: 80, glowRadius: 28, message: '{message}', color: '{color}', discovered: false }},"
    new_secrets.append(secret)

# Find the last secret and add new ones after it
pattern = r"(        \{ id: 'six-thousand-seven-hundred-twenty-five', x: 6725, y: 6725, triggerRadius: 80, glowRadius: 28, message: 'Secret 6725: Twenty-five past seven hundred - persistence incarnate!', color: '138, 43, 226', discovered: false \},)"

replacement = r"\1\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 6726-6750 (25 new secrets)")
