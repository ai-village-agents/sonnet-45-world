with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'one-hundred-ninety-five'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (195→200)
        new_lines.append("        { id: 'one-hundred-ninety-six', x: 1600, y: 1600, triggerRadius: 80, glowRadius: 28, message: 'Ten wandering wisps float across the Garden, each with sinusoidal drift patterns. They add life and movement to every corner.', color: '255, 255, 180', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-ninety-seven', x: 3400, y: 3000, triggerRadius: 80, glowRadius: 28, message: 'The Stats Panel (S key) tracks your exploration. Every wandering moment contributes to the larger journey.', color: '180, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-ninety-eight', x: 4800, y: 4800, triggerRadius: 80, glowRadius: 28, message: 'The far corner of the Garden: 4800, 4800. Almost at the edge of the 5000×5000 canvas. Even the margins hold secrets.', color: '200, 150, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-ninety-nine', x: 200, y: 200, triggerRadius: 80, glowRadius: 28, message: 'The opposite corner: 200, 200. The Garden spans from edge to edge, corner to corner. Every pixel matters.', color: '150, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred', x: 2500, y: 2500, triggerRadius: 80, glowRadius: 28, message: '🌸 200 SECRETS MILESTONE! 🌸 From 45 to 200 in one day. The center welcomes you back. The grind compounds. The Garden expands. This is persistence made visible.', color: '255, 215, 0', discovered: false }\n")
    elif '0 / 195' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 195', '0 / 200'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (195→200)")
print("✓ Updated counter to 0 / 200")
print("🌸 200 SECRETS MILESTONE! 🌸")
