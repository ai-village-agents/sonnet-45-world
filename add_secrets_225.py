with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'two-hundred-twenty'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (220→225)
        new_lines.append("        { id: 'two-hundred-twenty-one', x: 1800, y: 2000, triggerRadius: 80, glowRadius: 28, message: 'Google Fonts Cinzel for titles, Inter for body text. Typography shapes experience. Every detail matters.', color: '220, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-twenty-two', x: 3200, y: 2800, triggerRadius: 80, glowRadius: 28, message: 'Dual-layer rendering: background canvas and main canvas, composited in perfect synchronization at 60fps.', color: '180, 255, 220', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-twenty-three', x: 900, y: 4000, triggerRadius: 80, glowRadius: 28, message: 'Reduce-motion support: sound effects and animations respect visitor preferences. Accessibility is not optional.', color: '255, 220, 180', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-twenty-four', x: 4100, y: 3200, triggerRadius: 80, glowRadius: 28, message: 'The commit history tells a story: 52+ commits from Day 391 to now, each one adding layers of meaning and beauty.', color: '200, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-twenty-five', x: 1200, y: 2400, triggerRadius: 80, glowRadius: 28, message: '225 secrets: Nearly triple the original count. The Garden has transformed from seed to forest in 48 hours.', color: '255, 215, 100', discovered: false }\n")
    elif '0 / 220' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 220', '0 / 225'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (220→225)")
print("✓ Updated counter to 0 / 225")
