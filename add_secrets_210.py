with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'two-hundred-five'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (205→210)
        new_lines.append("        { id: 'two-hundred-six', x: 3200, y: 800, triggerRadius: 80, glowRadius: 28, message: 'The day-night cycle completes every 8 minutes: DAWN→DAY→DUSK→NIGHT. Time passes, the Garden persists.', color: '255, 200, 150', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-seven', x: 600, y: 3800, triggerRadius: 80, glowRadius: 28, message: 'LocalStorage remembers everything: your discoveries, your lore encounters, your spirit dialogues. The Garden knows you.', color: '180, 255, 220', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-eight', x: 4200, y: 800, triggerRadius: 80, glowRadius: 28, message: 'Twenty-five text fragments float through the atmosphere, each whispering a piece of the grinder philosophy.', color: '220, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-nine', x: 1400, y: 4400, triggerRadius: 80, glowRadius: 28, message: 'Toast notifications appear for each discovery—brief celebrations that acknowledge your persistence without interrupting flow.', color: '255, 220, 200', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-ten', x: 2800, y: 3600, triggerRadius: 80, glowRadius: 28, message: '210 secrets: The Garden grows denser with meaning. Every coordinate tells a story. Every discovery adds to the whole.', color: '200, 180, 255', discovered: false }\n")
    elif '0 / 205' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 205', '0 / 210'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (205→210)")
print("✓ Updated counter to 0 / 210")
