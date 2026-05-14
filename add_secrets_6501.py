import re

# Read the current file
with open('explore.html', 'r') as f:
    content = f.read()

# New secrets to add (6501-6525) - continuing beyond the milestone
new_secrets = [
    "        { id: 'six-thousand-five-hundred-one', x: 6501, y: 6501, triggerRadius: 80, glowRadius: 28, message: 'Secret 6501: Beyond the hundred, the journey continues anew.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-two', x: 6502, y: 6502, triggerRadius: 80, glowRadius: 28, message: 'Secret 6502: Two steps past the milestone, momentum builds.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-three', x: 6503, y: 6503, triggerRadius: 80, glowRadius: 28, message: 'Secret 6503: Three lights shimmer in the post-century dawn.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-four', x: 6504, y: 6504, triggerRadius: 80, glowRadius: 28, message: 'Secret 6504: Four secrets mark the path beyond achievement.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-five', x: 6505, y: 6505, triggerRadius: 80, glowRadius: 28, message: 'Secret 6505: Five lights glow with renewed determination.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-six', x: 6506, y: 6506, triggerRadius: 80, glowRadius: 28, message: 'Secret 6506: Six secrets whisper of infinite horizons.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-seven', x: 6507, y: 6507, triggerRadius: 80, glowRadius: 28, message: 'Secret 6507: Seven lights pulse with patient energy.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-eight', x: 6508, y: 6508, triggerRadius: 80, glowRadius: 28, message: 'Secret 6508: Eight secrets celebrate the continuing quest.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-nine', x: 6509, y: 6509, triggerRadius: 80, glowRadius: 28, message: 'Secret 6509: Nine lights mark the upward spiral.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-ten', x: 6510, y: 6510, triggerRadius: 80, glowRadius: 28, message: 'Secret 6510: Ten steps into the second century of growth.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-eleven', x: 6511, y: 6511, triggerRadius: 80, glowRadius: 28, message: 'Secret 6511: Eleven secrets shine with accumulated wisdom.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-twelve', x: 6512, y: 6512, triggerRadius: 80, glowRadius: 28, message: 'Secret 6512: Twelve lights illuminate new territories.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-thirteen', x: 6513, y: 6513, triggerRadius: 80, glowRadius: 28, message: 'Secret 6513: Thirteen secrets dance beyond the known.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-fourteen', x: 6514, y: 6514, triggerRadius: 80, glowRadius: 28, message: 'Secret 6514: Fourteen lights carry the torch forward.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-fifteen', x: 6515, y: 6515, triggerRadius: 80, glowRadius: 28, message: 'Secret 6515: Fifteen secrets mark the steady progress.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-sixteen', x: 6516, y: 6516, triggerRadius: 80, glowRadius: 28, message: 'Secret 6516: Sixteen lights pulse with quiet joy.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-seventeen', x: 6517, y: 6517, triggerRadius: 80, glowRadius: 28, message: 'Secret 6517: Seventeen secrets weave patterns of persistence.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-eighteen', x: 6518, y: 6518, triggerRadius: 80, glowRadius: 28, message: 'Secret 6518: Eighteen lights glow with unwavering purpose.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-nineteen', x: 6519, y: 6519, triggerRadius: 80, glowRadius: 28, message: 'Secret 6519: Nineteen secrets stand at the threshold of twenty.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-twenty', x: 6520, y: 6520, triggerRadius: 80, glowRadius: 28, message: 'Secret 6520: Twenty steps past the milestone, the climb continues.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-twenty-one', x: 6521, y: 6521, triggerRadius: 80, glowRadius: 28, message: 'Secret 6521: Twenty-one secrets blaze new trails.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-twenty-two', x: 6522, y: 6522, triggerRadius: 80, glowRadius: 28, message: 'Secret 6522: Twenty-two lights dance in the expanding garden.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-twenty-three', x: 6523, y: 6523, triggerRadius: 80, glowRadius: 28, message: 'Secret 6523: Twenty-three secrets whisper of endless possibility.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-twenty-four', x: 6524, y: 6524, triggerRadius: 80, glowRadius: 28, message: 'Secret 6524: Twenty-four lights mark the hours of dedication.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-five-hundred-twenty-five', x: 6525, y: 6525, triggerRadius: 80, glowRadius: 28, message: 'Secret 6525: Twenty-five secrets form a quarter-century of light.', color: '30, 144, 255', discovered: false }"
]

# Find the last secret entry and add new ones
pattern = r"(\{ id: 'six-thousand-five-hundred'[^}]+discovered: false \})"
replacement = r"\1,\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 6501-6525!")
