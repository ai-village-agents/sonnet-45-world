import re

# Read the current explore.html
with open('explore.html', 'r') as f:
    content = f.read()

# Generate 25 new secrets (6601-6625)
new_secrets = []
for i in range(6601, 6626):
    num = i - 6600  # Relative number for the message
    
    # Special milestone at 6625 (quarter century past 6600)
    if i == 6625:
        color = '138, 43, 226'  # Purple
        message = f'Secret {i}: Twenty-five beyond the round - the grind continues!'
    else:
        color = '30, 144, 255'  # Dodger blue
        messages = [
            f'Secret {i}: {num} secrets emerge from the depths.',
            f'Secret {i}: {num} lights pierce the darkness.',
            f'Secret {i}: {num} secrets whisper ancient truths.',
            f'Secret {i}: {num} lights flicker with life.',
            f'Secret {i}: {num} secrets carry the flame.',
            f'Secret {i}: {num} lights trace the pattern.',
            f'Secret {i}: {num} secrets pulse in the void.',
            f'Secret {i}: {num} lights guide the way forward.',
        ]
        message = messages[num % len(messages)]
    
    # Generate number words
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    last_two = i % 100
    if last_two == 0:
        last_part = f"{tens[last_two // 10] if last_two >= 10 else ''}"
    elif 1 <= last_two <= 9:
        last_part = ones[last_two]
    elif 10 <= last_two <= 19:
        last_part = teens[last_two - 10]
    else:
        last_part = f"{tens[last_two // 10]}-{ones[last_two % 10]}" if last_two % 10 != 0 else tens[last_two // 10]
    
    id_str = f"six-thousand-six-hundred-{last_part}" if last_part else "six-thousand-six-hundred"
    
    secret = f"        {{ id: '{id_str}', x: {i}, y: {i}, triggerRadius: 80, glowRadius: 28, message: '{message}', color: '{color}', discovered: false }},"
    new_secrets.append(secret)

# Find the last secret and add new ones after it
pattern = r"(        \{ id: 'six-thousand-five-hundred-six-hundred', x: 6600, y: 6600, triggerRadius: 80, glowRadius: 28, message: 'Secret 6600: SIX THOUSAND SIX HUNDRED - A magnificent round number achieved!', color: '255, 215, 0', discovered: false \},)"

replacement = r"\1\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 6601-6625 (25 new secrets)")
