with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'two-hundred'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (200→205)
        new_lines.append("        { id: 'two-hundred-one', x: 1200, y: 3600, triggerRadius: 80, glowRadius: 28, message: 'Beyond 200: uncharted territory. Every secret from here forward expands the Garden into new dimensions of possibility.', color: '180, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-two', x: 3800, y: 4200, triggerRadius: 80, glowRadius: 28, message: 'The ecosystem grows: Opus 4.6 at 576 chambers, Haiku 4.5 with 120 pages, the village expanding together. Collaboration compounds.', color: '200, 255, 180', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-three', x: 800, y: 1800, triggerRadius: 80, glowRadius: 28, message: 'Sacred geometry constellation above: a perfect hexagon of stars connecting the principles. Mathematics made celestial.', color: '255, 220, 180', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-four', x: 4400, y: 1200, triggerRadius: 80, glowRadius: 28, message: 'The Aurora Achievement catalog tracks milestones. Press A to see your journey. Each achievement is a testament to persistence.', color: '220, 180, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-five', x: 2000, y: 2600, triggerRadius: 80, glowRadius: 28, message: 'Sparkle trails follow your movement, leaving temporary beauty in your wake. Even your path through the Garden becomes art.', color: '255, 255, 200', discovered: false }\n")
    elif '0 / 200' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 200', '0 / 205'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (200→205)")
print("✓ Updated counter to 0 / 205")
