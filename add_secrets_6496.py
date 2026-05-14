import re

# Read the current file
with open('explore.html', 'r') as f:
    content = f.read()

# New secrets to add (6496-6500) - special milestone messages
new_secrets = [
    "        { id: 'six-thousand-four-hundred-ninety-six', x: 6496, y: 6496, triggerRadius: 80, glowRadius: 28, message: 'Secret 6496: Ninety-six secrets count down to the century mark.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-ninety-seven', x: 6497, y: 6497, triggerRadius: 80, glowRadius: 28, message: 'Secret 6497: Ninety-seven lights shimmer with mounting excitement.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-ninety-eight', x: 6498, y: 6498, triggerRadius: 80, glowRadius: 28, message: 'Secret 6498: Ninety-eight secrets breathe at the edge of completion.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-ninety-nine', x: 6499, y: 6499, triggerRadius: 80, glowRadius: 28, message: 'Secret 6499: Ninety-nine secrets - one step from the milestone.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred', x: 6500, y: 6500, triggerRadius: 80, glowRadius: 28, message: 'Secret 6500: ONE HUNDRED - The century milestone achieved! The garden grows ever richer.', color: '255, 215, 0', discovered: false }"
]

# Find the last secret entry and add new ones
pattern = r"(\{ id: 'six-thousand-four-hundred-ninety-five'[^}]+discovered: false \})"
replacement = r"\1,\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 6496-6500! Reached the 6500 milestone!")
