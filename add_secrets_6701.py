import re

# Read the current explore.html
with open('explore.html', 'r') as f:
    content = f.read()

# Generate 25 new secrets (6701-6725)
new_secrets = []
for i in range(6701, 6726):
    num = i - 6700  # Relative number for the message
    
    # Special milestone at 6725 (quarter century past 6700)
    if i == 6725:
        color = '138, 43, 226'  # Purple
        message = f'Secret {i}: Twenty-five past seven hundred - persistence incarnate!'
    else:
        color = '30, 144, 255'  # Dodger blue
        messages = [
            f'Secret {i}: {num} secrets unfold in the void.',
            f'Secret {i}: {num} lights pierce the cosmic veil.',
            f'Secret {i}: {num} secrets whisper eternal truths.',
            f'Secret {i}: {num} lights glow with steady resolve.',
            f'Secret {i}: {num} secrets mark the endless journey.',
            f'Secret {i}: {num} lights dance through dimensions.',
            f'Secret {i}: {num} secrets breathe in the silence.',
            f'Secret {i}: {num} lights guide the way home.',
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
pattern = r"(        \{ id: 'six-thousand-seven-hundred', x: 6700, y: 6700, triggerRadius: 80, glowRadius: 28, message: 'Secret 6700: SIX THOUSAND SEVEN HUNDRED - A century of growth from 6600!', color: '255, 215, 0', discovered: false \},)"

replacement = r"\1\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 6701-6725 (25 new secrets)")
