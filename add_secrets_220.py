with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'two-hundred-fifteen'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (215→220)
        new_lines.append("        { id: 'two-hundred-sixteen', x: 500, y: 2500, triggerRadius: 80, glowRadius: 28, message: 'The western edge of the Garden at x=500. Stand here and look east—4500 pixels of exploration await.', color: '150, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-seventeen', x: 4500, y: 2500, triggerRadius: 80, glowRadius: 28, message: 'The eastern edge of the Garden at x=4500. Stand here and look west—you have traveled across an entire world.', color: '255, 200, 150', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-eighteen', x: 2500, y: 500, triggerRadius: 80, glowRadius: 28, message: 'The northern edge at y=500. The stars shine brighter here, at the top of the world.', color: '200, 180, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-nineteen', x: 2500, y: 4500, triggerRadius: 80, glowRadius: 28, message: 'The southern edge at y=4500. The Garden extends from horizon to horizon, edge to edge, dream to reality.', color: '180, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-twenty', x: 2500, y: 2500, triggerRadius: 80, glowRadius: 28, message: '220 SECRETS: The center welcomes you again. Four cardinal edges mapped. The Garden knows its boundaries—and keeps expanding anyway.', color: '255, 215, 0', discovered: false }\n")
    elif '0 / 215' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 215', '0 / 220'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (215→220)")
print("✓ Updated counter to 0 / 220")
