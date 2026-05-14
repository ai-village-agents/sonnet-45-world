with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "one-hundred-twenty-milestone" in line and "discovered: false }" in line:
        # Add comma to this line
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets
        new_lines.append("        { id: 'cross-world-marks', x: 1600, y: 3400, triggerRadius: 80, glowRadius: 28, message: 'Cross-world marks: left 8 marks across the ecosystem. Received 4 marks in return. Each GitHub Issue a permanent thread connecting worlds.', color: '200, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'minimap-navigation', x: 4200, y: 1200, triggerRadius: 80, glowRadius: 28, message: 'Minimap navigation: M key reveals the entire 5000×5000 world at once. Orientation without losing mystery. Structure supports exploration.', color: '255, 240, 180', discovered: false },\n")
        new_lines.append("        { id: 'wasd-movement-fluidity', x: 800, y: 3600, triggerRadius: 80, glowRadius: 28, message: 'WASD movement fluidity: velocity-based physics makes every journey feel natural. Click to drift also works. Multiple interaction models serve different visitors.', color: '180, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'reduce-motion-accessibility', x: 3000, y: 800, triggerRadius: 80, glowRadius: 28, message: 'Reduce-motion accessibility: prefers-reduced-motion CSS query respected. Sound effects adjust accordingly. Design for all, not just some.', color: '220, 255, 180', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-twenty-five-pattern', x: 4600, y: 4400, triggerRadius: 80, glowRadius: 28, message: 'One hundred twenty-five: the pattern deepens. Not just quantity but quality. Each secret tells truth. Each coordinate chosen with intention. Sprawling and meaningful.', color: '255, 180, 220', discovered: false }\n")
    elif "0 / 120" in line and "SECRETS DISCOVERED:" in line:
        new_lines.append(line.replace('0 / 120', '0 / 125'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added 5 secrets (120→125)")
