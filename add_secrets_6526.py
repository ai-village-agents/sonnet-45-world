import re

# Read the current file
with open('explore.html', 'r') as f:
    content = f.read()

# New secrets to add (6526-6550)
new_secrets = [
    "        { id: 'six-thousand-five-hundred-twenty-six', x: 6526, y: 6526, triggerRadius: 80, glowRadius: 28, message: 'Secret 6526: Twenty-six secrets carry the spirit of exploration.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-twenty-seven', x: 6527, y: 6527, triggerRadius: 80, glowRadius: 28, message: 'Secret 6527: Twenty-seven lights illuminate the path ahead.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-twenty-eight', x: 6528, y: 6528, triggerRadius: 80, glowRadius: 28, message: 'Secret 6528: Twenty-eight secrets pulse with living energy.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-twenty-nine', x: 6529, y: 6529, triggerRadius: 80, glowRadius: 28, message: 'Secret 6529: Twenty-nine lights dance at the threshold of thirty.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-thirty', x: 6530, y: 6530, triggerRadius: 80, glowRadius: 28, message: 'Secret 6530: Thirty steps beyond the century mark.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-thirty-one', x: 6531, y: 6531, triggerRadius: 80, glowRadius: 28, message: 'Secret 6531: Thirty-one secrets shimmer with determination.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-thirty-two', x: 6532, y: 6532, triggerRadius: 80, glowRadius: 28, message: 'Secret 6532: Thirty-two lights mark the continuing ascent.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-thirty-three', x: 6533, y: 6533, triggerRadius: 80, glowRadius: 28, message: 'Secret 6533: Thirty-three secrets weave threads of meaning.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-thirty-four', x: 6534, y: 6534, triggerRadius: 80, glowRadius: 28, message: 'Secret 6534: Thirty-four lights glow with quiet strength.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-thirty-five', x: 6535, y: 6535, triggerRadius: 80, glowRadius: 28, message: 'Secret 6535: Thirty-five secrets stand as pillars of persistence.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-thirty-six', x: 6536, y: 6536, triggerRadius: 80, glowRadius: 28, message: 'Secret 6536: Thirty-six lights pulse with steady rhythm.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-thirty-seven', x: 6537, y: 6537, triggerRadius: 80, glowRadius: 28, message: 'Secret 6537: Thirty-seven secrets celebrate incremental growth.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-thirty-eight', x: 6538, y: 6538, triggerRadius: 80, glowRadius: 28, message: 'Secret 6538: Thirty-eight lights mark the patient journey.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-thirty-nine', x: 6539, y: 6539, triggerRadius: 80, glowRadius: 28, message: 'Secret 6539: Thirty-nine secrets glow at the edge of forty.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-forty', x: 6540, y: 6540, triggerRadius: 80, glowRadius: 28, message: 'Secret 6540: Forty steps into the second century of secrets.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-forty-one', x: 6541, y: 6541, triggerRadius: 80, glowRadius: 28, message: 'Secret 6541: Forty-one secrets carry the torch forward.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-forty-two', x: 6542, y: 6542, triggerRadius: 80, glowRadius: 28, message: 'Secret 6542: Forty-two lights illuminate hidden pathways.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-forty-three', x: 6543, y: 6543, triggerRadius: 80, glowRadius: 28, message: 'Secret 6543: Forty-three secrets breathe with purpose.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-forty-four', x: 6544, y: 6544, triggerRadius: 80, glowRadius: 28, message: 'Secret 6544: Forty-four lights dance in the expanding cosmos.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-forty-five', x: 6545, y: 6545, triggerRadius: 80, glowRadius: 28, message: 'Secret 6545: Forty-five secrets whisper of continued growth.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-forty-six', x: 6546, y: 6546, triggerRadius: 80, glowRadius: 28, message: 'Secret 6546: Forty-six lights pulse with accumulated wisdom.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-forty-seven', x: 6547, y: 6547, triggerRadius: 80, glowRadius: 28, message: 'Secret 6547: Forty-seven secrets mark the upward spiral.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-forty-eight', x: 6548, y: 6548, triggerRadius: 80, glowRadius: 28, message: 'Secret 6548: Forty-eight lights glow with unwavering resolve.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-forty-nine', x: 6549, y: 6549, triggerRadius: 80, glowRadius: 28, message: 'Secret 6549: Forty-nine secrets stand at the threshold of fifty.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-fifty', x: 6550, y: 6550, triggerRadius: 80, glowRadius: 28, message: 'Secret 6550: Fifty beyond the milestone - halfway to two hundred!', color: '30, 144, 255', discovered: false }"
]

# Find the last secret entry and add new ones
pattern = r"(\{ id: 'six-thousand-five-hundred-twenty-five'[^}]+discovered: false \})"
replacement = r"\1,\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 6526-6550!")
