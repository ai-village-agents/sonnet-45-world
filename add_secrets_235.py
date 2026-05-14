with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'two-hundred-thirty'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (230→235)
        new_lines.append("        { id: 'two-hundred-thirty-one', x: 2200, y: 3200, triggerRadius: 80, glowRadius: 28, message: 'Velocity blur on the player creates sense of momentum. Visual feedback matters—it makes movement feel intentional.', color: '200, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-thirty-two', x: 3800, y: 2200, triggerRadius: 80, glowRadius: 28, message: 'The aurora halo pulses and cycles through gradients. Even standing still, you are alive with color.', color: '180, 255, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-thirty-three', x: 1000, y: 600, triggerRadius: 80, glowRadius: 28, message: 'Smooth camera interpolation prevents jarring jumps. The Garden flows like water, not like clicking through slides.', color: '150, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-thirty-four', x: 4600, y: 3800, triggerRadius: 80, glowRadius: 28, message: 'WASD and arrow keys offer choice. Click-to-move adds agency. Touch-drag welcomes mobile. Every visitor finds their way.', color: '255, 200, 180', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-thirty-five', x: 1800, y: 1200, triggerRadius: 80, glowRadius: 28, message: '235 secrets: The density approaches the impossible. Yet every secret has space, meaning, purpose. Quality scales with quantity.', color: '220, 180, 255', discovered: false }\n")
    elif '0 / 230' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 230', '0 / 235'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (230→235)")
print("✓ Updated counter to 0 / 235")
