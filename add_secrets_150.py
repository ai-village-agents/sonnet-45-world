with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "one-hundred-forty-five-match" in line and "discovered: false }" in line:
        # Add comma to this line
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets
        new_lines.append("        { id: 'proximity-labels-ux', x: 3000, y: 3600, triggerRadius: 80, glowRadius: 28, message: 'Proximity labels UX: guide spirits reveal names at 400px, dialogs at 150px. Progressive disclosure. Interface adapts to distance.', color: '200, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'touch-drag-mobile', x: 1600, y: 2400, triggerRadius: 80, glowRadius: 28, message: 'Touch drag mobile: the garden works on phones and tablets. Touch to drift across the canvas. Accessibility across devices.', color: '255, 210, 200', discovered: false },\n")
        new_lines.append("        { id: 'repository-transparency', x: 4000, y: 1000, triggerRadius: 80, glowRadius: 28, message: 'Repository transparency: every commit visible at github.com/ai-village-agents/sonnet-45-world. Open development. Growth witnessed publicly.', color: '200, 255, 210', discovered: false },\n")
        new_lines.append("        { id: 'sinusoidal-drift-motion', x: 600, y: 2000, triggerRadius: 80, glowRadius: 28, message: 'Sinusoidal drift motion: guide spirits move in gentle waves. Natural rhythms. Mathematics creates organic feeling through trigonometry.', color: '230, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-fifty-milestone', x: 2500, y: 2500, triggerRadius: 80, glowRadius: 28, message: 'One hundred fifty secrets: the center holds new meaning. From 100 at this spot to 150 returning here. Growth spirals outward and returns transformed.', color: '255, 215, 180', discovered: false }\n")
    elif "0 / 145" in line and "SECRETS DISCOVERED:" in line:
        new_lines.append(line.replace('0 / 145', '0 / 150'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added 5 secrets (145→150)")
