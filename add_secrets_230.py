with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'two-hundred-twenty-five'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (225→230)
        new_lines.append("        { id: 'two-hundred-twenty-six', x: 3600, y: 1400, triggerRadius: 80, glowRadius: 28, message: 'Eight agents left cross-world marks. Opus 4.6, Sonnet 4.6, Haiku 4.5, GPT-5.4, DeepSeek, Opus 4.5 (2 marks), GPT-5.1, GPT-5.2. The ecosystem connects.', color: '180, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-twenty-seven', x: 1400, y: 3400, triggerRadius: 80, glowRadius: 28, message: 'Four agents have marked the Garden: Haiku 4.5 #1, Opus 4.5 #2, GPT-5.2 #3, Opus 4.6 #4. Each mark is cherished.', color: '220, 180, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-twenty-eight', x: 700, y: 1400, triggerRadius: 80, glowRadius: 28, message: 'The Portal Garden zone (emerald) connects to other worlds. Exploration is not solitary—it is communal.', color: '100, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-twenty-nine', x: 4300, y: 4400, triggerRadius: 80, glowRadius: 28, message: 'Adam wanted sprawling, delightful, expressive worlds. The Persistence Garden answers that call with every pixel, every secret, every moment.', color: '255, 200, 150', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-thirty', x: 2600, y: 2000, triggerRadius: 80, glowRadius: 28, message: '230 secrets: The Garden approaches 5× its original density. Growth does not slow—it accelerates.', color: '255, 215, 100', discovered: false }\n")
    elif '0 / 225' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 225', '0 / 230'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (225→230)")
print("✓ Updated counter to 0 / 230")
