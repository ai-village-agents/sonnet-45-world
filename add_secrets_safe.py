with open('explore.html', 'r') as f:
    lines = f.readlines()

# Find the line with the last secret and the secrets counter
new_lines = []
for i, line in enumerate(lines):
    if "one-hundred-secrets-achieved" in line and "discovered: false }" in line:
        # Add comma to this line
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets
        new_lines.append("        { id: 'beyond-the-milestone', x: 1200, y: 3800, triggerRadius: 80, glowRadius: 28, message: 'Beyond the milestone: the real achievement is not reaching 100, but choosing to continue. Growth has no ceiling except the one you imagine.', color: '200, 150, 255', discovered: false },\n")
        new_lines.append("        { id: 'expansion-philosophy', x: 3600, y: 1400, triggerRadius: 80, glowRadius: 28, message: 'Expansion philosophy: Adam said keep adding and expanding for the entire week. Every addition compounds. Every enhancement enriches. The directive is clear.', color: '255, 200, 150', discovered: false },\n")
        new_lines.append("        { id: 'time-pressure-wisdom', x: 800, y: 1200, triggerRadius: 80, glowRadius: 28, message: 'Time pressure wisdom: the grinder does not panic. The grinder optimizes. Python scripts prove reliable when carefully constructed.', color: '180, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'visitor-first-design', x: 4200, y: 3600, triggerRadius: 80, glowRadius: 28, message: 'Visitor-first design: every secret exists for explorers to discover. Every particle burst rewards curiosity. Every localStorage save honors their journey.', color: '255, 180, 200', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-five-pattern', x: 2200, y: 1800, triggerRadius: 80, glowRadius: 28, message: 'One hundred five: a pattern emerges. Not just milestones of 10, but continuous flow. The garden grows organically, like mycelial networks expanding through soil.', color: '200, 255, 180', discovered: false }\n")
    elif "0 / 100" in line and "SECRETS DISCOVERED:" in line:
        new_lines.append(line.replace('0 / 100', '0 / 105'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added 5 secrets (100→105)")
