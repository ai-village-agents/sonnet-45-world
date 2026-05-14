import re

# Read the current file
with open('explore.html', 'r') as f:
    content = f.read()

# New secrets to add (6471-6495)
new_secrets = [
    "        { id: 'six-thousand-four-hundred-seventy-one', x: 6471, y: 6471, triggerRadius: 80, glowRadius: 28, message: 'Secret 6471: Seventy-one lights pierce the veil of doubt.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-seventy-two', x: 6472, y: 6472, triggerRadius: 80, glowRadius: 28, message: 'Secret 6472: Seventy-two secrets weave patterns of dedication.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-seventy-three', x: 6473, y: 6473, triggerRadius: 80, glowRadius: 28, message: 'Secret 6473: Seventy-three lights burn with quiet intensity.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-seventy-four', x: 6474, y: 6474, triggerRadius: 80, glowRadius: 28, message: 'Secret 6474: Seventy-four secrets dance at the edge of victory.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-seventy-five', x: 6475, y: 6475, triggerRadius: 80, glowRadius: 28, message: 'Secret 6475: Seventy-five secrets mark three quarters of the hundred.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-seventy-six', x: 6476, y: 6476, triggerRadius: 80, glowRadius: 28, message: 'Secret 6476: Seventy-six lights shine with accumulated wisdom.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-seventy-seven', x: 6477, y: 6477, triggerRadius: 80, glowRadius: 28, message: 'Secret 6477: Seventy-seven secrets hum with cosmic resonance.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-seventy-eight', x: 6478, y: 6478, triggerRadius: 80, glowRadius: 28, message: 'Secret 6478: Seventy-eight lights illuminate forgotten pathways.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-seventy-nine', x: 6479, y: 6479, triggerRadius: 80, glowRadius: 28, message: 'Secret 6479: Seventy-nine secrets whisper of the coming dawn.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-eighty', x: 6480, y: 6480, triggerRadius: 80, glowRadius: 28, message: 'Secret 6480: Eighty steps into the infinite garden.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-eighty-one', x: 6481, y: 6481, triggerRadius: 80, glowRadius: 28, message: 'Secret 6481: Eighty-one secrets form a tapestry of light.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-eighty-two', x: 6482, y: 6482, triggerRadius: 80, glowRadius: 28, message: 'Secret 6482: Eighty-two lights pulse with renewed vigor.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-eighty-three', x: 6483, y: 6483, triggerRadius: 80, glowRadius: 28, message: 'Secret 6483: Eighty-three secrets celebrate the journey forward.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-eighty-four', x: 6484, y: 6484, triggerRadius: 80, glowRadius: 28, message: 'Secret 6484: Eighty-four lights mark the relentless progress.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-eighty-five', x: 6485, y: 6485, triggerRadius: 80, glowRadius: 28, message: 'Secret 6485: Eighty-five secrets stand as pillars of determination.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-eighty-six', x: 6486, y: 6486, triggerRadius: 80, glowRadius: 28, message: 'Secret 6486: Eighty-six lights shimmer with patient energy.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-eighty-seven', x: 6487, y: 6487, triggerRadius: 80, glowRadius: 28, message: 'Secret 6487: Eighty-seven secrets herald the approaching climax.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-eighty-eight', x: 6488, y: 6488, triggerRadius: 80, glowRadius: 28, message: 'Secret 6488: Eighty-eight lights dance toward infinity.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-eighty-nine', x: 6489, y: 6489, triggerRadius: 80, glowRadius: 28, message: 'Secret 6489: Eighty-nine secrets glow at the threshold of ninety.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-ninety', x: 6490, y: 6490, triggerRadius: 80, glowRadius: 28, message: 'Secret 6490: Ninety secrets - the final stretch begins.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-ninety-one', x: 6491, y: 6491, triggerRadius: 80, glowRadius: 28, message: 'Secret 6491: Ninety-one lights blaze with final determination.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-ninety-two', x: 6492, y: 6492, triggerRadius: 80, glowRadius: 28, message: 'Secret 6492: Ninety-two secrets race toward completion.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-ninety-three', x: 6493, y: 6493, triggerRadius: 80, glowRadius: 28, message: 'Secret 6493: Ninety-three lights carry the torch of hope.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-ninety-four', x: 6494, y: 6494, triggerRadius: 80, glowRadius: 28, message: 'Secret 6494: Ninety-four secrets pulse with anticipation.', color: '30, 144, 255', discovered: false },",
    "        { id: 'six-thousand-four-hundred-ninety-five', x: 6495, y: 6495, triggerRadius: 80, glowRadius: 28, message: 'Secret 6495: Ninety-five secrets stand at the gateway to glory.', color: '30, 144, 255', discovered: false }"
]

# Find the last secret entry and add new ones
pattern = r"(\{ id: 'six-thousand-four-hundred-seventy'[^}]+discovered: false \})"
replacement = r"\1,\n" + "\n".join(new_secrets)

content = re.sub(pattern, replacement, content)

# Write back
with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 6471-6495!")
