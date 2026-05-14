with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "one-hundred-thirty-five-momentum" in line and "discovered: false }" in line:
        # Add comma to this line
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets
        new_lines.append("        { id: 'nebulae-backgrounds', x: 2600, y: 4200, triggerRadius: 80, glowRadius: 28, message: 'Fourteen nebulae backgrounds: radial gradients create cosmic depth. Layered atmosphere builds immersion. The canvas breathes with color.', color: '200, 210, 255', discovered: false },\n")
        new_lines.append("        { id: 'text-fragment-poetry', x: 1400, y: 1400, triggerRadius: 80, glowRadius: 28, message: 'Twenty-five text fragments: philosophical whispers scattered across the world. Environmental storytelling. Words drift like thoughts through space.', color: '255, 210, 190', discovered: false },\n")
        new_lines.append("        { id: 'coordinate-hud-orientation', x: 3400, y: 4000, triggerRadius: 80, glowRadius: 28, message: 'Coordinate HUD orientation: X and Y always visible. Never lost. The interface serves explorers without overwhelming them.', color: '190, 255, 220', discovered: false },\n")
        new_lines.append("        { id: 'stats-panel-transparency', x: 4400, y: 1600, triggerRadius: 80, glowRadius: 28, message: 'Stats panel transparency: S key reveals journey metrics without obscuring the world. Information when needed, invisible when not.', color: '230, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-forty-surpass', x: 2500, y: 1500, triggerRadius: 80, glowRadius: 28, message: 'One hundred forty: surpassing the Edge Garden now. Each world grows at its own pace. Competition inspires, but the Garden grows for itself.', color: '255, 190, 200', discovered: false }\n")
    elif "0 / 135" in line and "SECRETS DISCOVERED:" in line:
        new_lines.append(line.replace('0 / 135', '0 / 140'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added 5 secrets (135→140)")
