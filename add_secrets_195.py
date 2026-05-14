with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'one-hundred-ninety'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (190→195)
        new_lines.append("        { id: 'one-hundred-ninety-one', x: 700, y: 600, triggerRadius: 80, glowRadius: 28, message: 'The Discovery Journal (J key) remembers every secret you find. Persistence is not just about doing—it is about remembering.', color: '200, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-ninety-two', x: 4300, y: 3600, triggerRadius: 80, glowRadius: 28, message: 'Ambient audio pulses at 80Hz with zone-specific oscillators. Press Shift+A to toggle. The Garden sounds as rich as it looks.', color: '180, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-ninety-three', x: 1800, y: 4600, triggerRadius: 80, glowRadius: 28, message: 'Fourteen nebulae drift in the background, adding depth and texture. The canvas has layers upon layers, all animating in harmony.', color: '255, 180, 220', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-ninety-four', x: 3000, y: 1200, triggerRadius: 80, glowRadius: 28, message: 'Touch drag support brings the Garden to mobile visitors. Every platform, every visitor, every interaction matters.', color: '220, 200, 100', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-ninety-five', x: 2800, y: 2200, triggerRadius: 80, glowRadius: 28, message: '195 secrets: from 45 to 195 in less than 24 hours. This is what Adam asked for—sprawling, expanding, relentless growth.', color: '255, 215, 100', discovered: false }\n")
    elif '0 / 190' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 190', '0 / 195'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (190→195)")
print("✓ Updated counter to 0 / 195")
