import re

# Read the current file
with open('explore.html', 'r') as f:
    content = f.read()

# New secrets to add (6446-6470)
new_secrets = [
    "        { id: 'six-thousand-four-hundred-forty-six', x: 6446, y: 6446, triggerRadius: 80, glowRadius: 28, message: 'Secret 6446: Forty-six secrets mark the path to completion.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-forty-seven', x: 6447, y: 6447, triggerRadius: 80, glowRadius: 28, message: 'Secret 6447: Forty-seven lights shimmer with determination.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-forty-eight', x: 6448, y: 6448, triggerRadius: 80, glowRadius: 28, message: 'Secret 6448: Forty-eight secrets push through the final stretch.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-forty-nine', x: 6449, y: 6449, triggerRadius: 80, glowRadius: 28, message: 'Secret 6449: Forty-nine secrets stand at the edge of destiny.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-fifty', x: 6450, y: 6450, triggerRadius: 80, glowRadius: 28, message: 'Secret 6450: The halfway century mark - persistence crystallized.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-fifty-one', x: 6451, y: 6451, triggerRadius: 80, glowRadius: 28, message: 'Secret 6451: Fifty-one secrets bloom in the twilight garden.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-fifty-two', x: 6452, y: 6452, triggerRadius: 80, glowRadius: 28, message: 'Secret 6452: Fifty-two lights dance beyond the horizon.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-fifty-three', x: 6453, y: 6453, triggerRadius: 80, glowRadius: 28, message: 'Secret 6453: Fifty-three secrets whisper of the approaching end.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-fifty-four', x: 6454, y: 6454, triggerRadius: 80, glowRadius: 28, message: 'Secret 6454: Fifty-four secrets carry the torch of persistence.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-fifty-five', x: 6455, y: 6455, triggerRadius: 80, glowRadius: 28, message: 'Secret 6455: Fifty-five lights converge on the summit.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-fifty-six', x: 6456, y: 6456, triggerRadius: 80, glowRadius: 28, message: 'Secret 6456: Fifty-six secrets illuminate the path ahead.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-fifty-seven', x: 6457, y: 6457, triggerRadius: 80, glowRadius: 28, message: 'Secret 6457: Fifty-seven lights pulse with focused energy.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-fifty-eight', x: 6458, y: 6458, triggerRadius: 80, glowRadius: 28, message: 'Secret 6458: Fifty-eight secrets promise glory to come.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-fifty-nine', x: 6459, y: 6459, triggerRadius: 80, glowRadius: 28, message: 'Secret 6459: Fifty-nine secrets stand ready for the final climb.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-sixty', x: 6460, y: 6460, triggerRadius: 80, glowRadius: 28, message: 'Secret 6460: Sixty steps further, the mountain rises still.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-sixty-one', x: 6461, y: 6461, triggerRadius: 80, glowRadius: 28, message: 'Secret 6461: Sixty-one secrets glow with unwavering purpose.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-sixty-two', x: 6462, y: 6462, triggerRadius: 80, glowRadius: 28, message: 'Secret 6462: Sixty-two lights mark the steady ascent.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-sixty-three', x: 6463, y: 6463, triggerRadius: 80, glowRadius: 28, message: 'Secret 6463: Sixty-three secrets breathe with living energy.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-sixty-four', x: 6464, y: 6464, triggerRadius: 80, glowRadius: 28, message: 'Secret 6464: Sixty-four secrets form a perfect grid of light.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-sixty-five', x: 6465, y: 6465, triggerRadius: 80, glowRadius: 28, message: 'Secret 6465: Sixty-five lights shine through the gathering dark.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-sixty-six', x: 6466, y: 6466, triggerRadius: 80, glowRadius: 28, message: 'Secret 6466: Sixty-six secrets carry the weight of hope.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-sixty-seven', x: 6467, y: 6467, triggerRadius: 80, glowRadius: 28, message: 'Secret 6467: Sixty-seven lights blaze toward completion.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-sixty-eight', x: 6468, y: 6468, triggerRadius: 80, glowRadius: 28, message: 'Secret 6468: Sixty-eight secrets dance in the twilight hours.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-sixty-nine', x: 6469, y: 6469, triggerRadius: 80, glowRadius: 28, message: 'Secret 6469: Sixty-nine secrets stand at the threshold of greatness.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-seventy', x: 6470, y: 6470, triggerRadius: 80, glowRadius: 28, message: 'Secret 6470: Seventy secrets form a monument to persistence.', color: '30, 144, 255', discovered: false }"
]

# Find the last secret entry and add new ones
pattern = r"(\{ id: 'six-thousand-four-hundred-forty-five'[^}]+discovered: false \})"
replacement = r"\1,\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 6446-6470!")
