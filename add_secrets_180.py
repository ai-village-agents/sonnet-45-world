with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'one-hundred-seventy-five-finale'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets for Day 394 beginning (175→180)
        new_lines.append("        { id: 'one-hundred-seventy-six', x: 1200, y: 800, triggerRadius: 80, glowRadius: 28, message: 'Day 394 dawns. The Garden continues to grow, one secret at a time. Each dawn brings new patterns, new persistence, new possibilities.', color: '255, 200, 100', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-seventy-seven', x: 3800, y: 1500, triggerRadius: 80, glowRadius: 28, message: 'Returning to the center is not regression—it is the spiral path of growth. Each return sees the landscape with new eyes.', color: '150, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-seventy-eight', x: 1000, y: 3200, triggerRadius: 80, glowRadius: 28, message: 'The Python script: reliable, methodical, proven. Line-by-line transformation with 100% success. Sometimes the simplest tool is the strongest.', color: '100, 255, 150', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-seventy-nine', x: 4200, y: 4000, triggerRadius: 80, glowRadius: 28, message: '5000 pixels across, 5000 pixels tall—yet the canvas feels infinite when filled with intention. Every coordinate holds potential.', color: '220, 150, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-eighty', x: 2500, y: 1800, triggerRadius: 80, glowRadius: 28, message: '180 SECRETS: Six milestones crossed (50, 100, 130, 150, 175, 180). The journey compounds. Adam said expand more and more—so we expand.', color: '255, 215, 0', discovered: false }\n")
    elif '0 / 175' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 175', '0 / 180'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (175→180)")
print("✓ Updated counter to 0 / 180")
