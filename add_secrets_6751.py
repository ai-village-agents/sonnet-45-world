import re

# Read the current explore.html
with open('explore.html', 'r') as f:
    content = f.read()

# Generate 25 new secrets (6751-6775)
new_secrets = []
for i in range(6751, 6776):
    num = i - 6750  # Relative number for the message
    
    # Special milestone at 6775 (quarter century past 6750)
    if i == 6775:
        color = '138, 43, 226'  # Purple
        message = f'Secret {i}: Twenty-five more lights in the endless expanse!'
    else:
        color = '30, 144, 255'  # Dodger blue
        messages = [
            f'Secret {i}: {num} secrets drift through time.',
            f'Secret {i}: {num} lights pierce the infinite.',
            f'Secret {i}: {num} secrets carry the flame forward.',
            f'Secret {i}: {num} lights glow with determination.',
            f'Secret {i}: {num} secrets mark the passage.',
            f'Secret {i}: {num} lights dance in harmony.',
            f'Secret {i}: {num} secrets breathe with purpose.',
            f'Secret {i}: {num} lights guide the journey.',
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
pattern = r"(        \{ id: 'six-thousand-seven-hundred-fifty', x: 6750, y: 6750, triggerRadius: 80, glowRadius: 28, message: 'Secret 6750: FIFTY PAST SEVEN HUNDRED - The journey accelerates!', color: '255, 215, 0', discovered: false \},)"

replacement = r"\1\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print(f"Added secrets 6751-6775 (25 new secrets)")
