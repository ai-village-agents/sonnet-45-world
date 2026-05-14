with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "one-hundred-ten-velocity" in line and "discovered: false }" in line:
        # Add comma to this line
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets  
        new_lines.append("        { id: 'github-pages-deployment', x: 2800, y: 3200, triggerRadius: 80, glowRadius: 28, message: 'GitHub Pages deployment: every push becomes production in moments. The garden updates live for all visitors. Infrastructure as expression.', color: '220, 180, 255', discovered: false },\n")
        new_lines.append("        { id: 'localStorage-persistence', x: 1400, y: 2200, triggerRadius: 80, glowRadius: 28, message: 'localStorage persistence: your discoveries survive browser restarts. Your journey is remembered. Progress compounds across sessions.', color: '255, 200, 180', discovered: false },\n")
        new_lines.append("        { id: 'particle-physics-joy', x: 4400, y: 800, triggerRadius: 80, glowRadius: 28, message: 'Particle physics joy: 780 lines of attraction/repulsion code. Every movement feels alive. Mathematics becomes magic through motion.', color: '180, 255, 220', discovered: false },\n")
        new_lines.append("        { id: 'guide-spirit-wisdom', x: 700, y: 4200, triggerRadius: 80, glowRadius: 28, message: 'Guide spirit wisdom: eight spirits drift across the canvas. Each offers philosophy when you draw near. Proximity creates connection.', color: '240, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-fifteen-rhythm', x: 3400, y: 1600, triggerRadius: 80, glowRadius: 28, message: 'One hundred fifteen: the rhythm is established. Five secrets per commit. Three minutes per batch. The pattern holds until 2pm PT.', color: '200, 220, 255', discovered: false }\n")
    elif "0 / 110" in line and "SECRETS DISCOVERED:" in line:
        new_lines.append(line.replace('0 / 110', '0 / 115'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added 5 secrets (110→115)")
