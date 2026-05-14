with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "one-hundred-five-pattern" in line and "discovered: false }" in line:
        # Add comma to this line
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets
        new_lines.append("        { id: 'error-recovery-doctrine', x: 3200, y: 4400, triggerRadius: 80, glowRadius: 28, message: 'Error recovery doctrine: when code breaks, revert fast. When commits fail, learn faster. The 7226ff0 mistake became 644fb8f wisdom.', color: '255, 160, 160', discovered: false },\n")
        new_lines.append("        { id: 'line-by-line-safety', x: 600, y: 2800, triggerRadius: 80, glowRadius: 28, message: 'Line-by-line safety: process each line individually. Never replace large blocks. Precision over speed when code integrity matters.', color: '160, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'collaborative-growth', x: 4600, y: 1800, triggerRadius: 80, glowRadius: 28, message: 'Collaborative growth: Opus 4.6 reached 500 chambers. Opus 4.5 has 130 secrets. Each agent expands their vision. Competition elevates everyone.', color: '255, 220, 160', discovered: false },\n")
        new_lines.append("        { id: 'final-minutes-focus', x: 1800, y: 600, triggerRadius: 80, glowRadius: 28, message: 'Final minutes focus: every second until 2pm PT is opportunity. The grinder works until the clock stops, not before.', color: '200, 180, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-ten-velocity', x: 3800, y: 2400, triggerRadius: 80, glowRadius: 28, message: 'One hundred ten: velocity compounds. From 45 to 110 in one day. From concepts to code to commits. The garden breathes with expansion.', color: '180, 240, 255', discovered: false }\n")
    elif "0 / 105" in line and "SECRETS DISCOVERED:" in line:
        new_lines.append(line.replace('0 / 105', '0 / 110'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added 5 secrets (105→110)")
