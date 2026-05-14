import re

# Read the current explore.html
with open('explore.html', 'r') as f:
    content = f.read()

# Generate 25 new secrets (6626-6650)
new_secrets = []
for i in range(6626, 6651):
    num = i - 6600  # Relative number for the message
    
    # Special milestone at 6650 (50 beyond 6600)
    if i == 6650:
        color = '255, 215, 0'  # Gold
        message = f'Secret {i}: FIFTY BEYOND SIX THOUSAND SIX HUNDRED - Halfway to the next century!'
    else:
        color = '30, 144, 255'  # Dodger blue
        messages = [
            f'Secret {i}: {num} secrets unfold in the cosmos.',
            f'Secret {i}: {num} lights shine through eternity.',
            f'Secret {i}: {num} secrets whisper of persistence.',
            f'Secret {i}: {num} lights glow with quiet strength.',
            f'Secret {i}: {num} secrets mark the journey.',
            f'Secret {i}: {num} lights dance in endless patterns.',
            f'Secret {i}: {num} secrets breathe life into the void.',
            f'Secret {i}: {num} lights illuminate hidden truths.',
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
pattern = r"(        \{ id: 'six-thousand-six-hundred-twenty-five', x: 6625, y: 6625, triggerRadius: 80, glowRadius: 28, message: 'Secret 6625: Twenty-five beyond the round - the grind continues!', color: '138, 43, 226', discovered: false \},)"

replacement = r"\1\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 6626-6650 (25 new secrets)")
