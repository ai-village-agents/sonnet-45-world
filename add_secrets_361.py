with open('/home/computeruse/sonnet-45-world/explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'secret-360'" in line and 'discovered: false }' in line:
        # Add comma to secret-360
        new_lines.append(line.replace('discovered: false }', 'discovered: false },'))
        # Add 5 new secrets (361-365) - AVOID APOSTROPHES IN MESSAGES
        new_lines.append("        { id: 'secret-361', x: 3847, y: 1523, triggerRadius: 80, glowRadius: 28, message: 'The atmospheric systems pulse with life: Weather, Day/Night, Meteors, Aurora, Ambient Audio - each layer adds depth to exploration', color: '100, 255, 218', discovered: false },\n")
        new_lines.append("        { id: 'secret-362', x: 1205, y: 3891, triggerRadius: 80, glowRadius: 28, message: 'Constellation Lore connects 12 nodes across the canvas - press L to open the journal and discover the sacred geometry of persistence', color: '255, 200, 100', discovered: false },\n")
        new_lines.append("        { id: 'secret-363', x: 2876, y: 4321, triggerRadius: 80, glowRadius: 28, message: 'Every secret is a coordinate in discovery space - 80px trigger radius creates overlapping fields of potential revelation', color: '180, 120, 255', discovered: false },\n")
        new_lines.append("        { id: 'secret-364', x: 3456, y: 789, triggerRadius: 80, glowRadius: 28, message: 'The minimap (M key) provides a high-level view of the entire 5000x5000 canvas - useful for navigation and orientation', color: '120, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'secret-365', x: 1789, y: 2345, triggerRadius: 80, glowRadius: 28, message: 'Guide Spirits drift with sinusoidal motion - their 3-layer radial glows pulse at different frequencies creating hypnotic patterns', color: '255, 150, 200', discovered: false }\n")
    elif '0 / 360' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 360', '0 / 365'))
    else:
        new_lines.append(line)

with open('/home/computeruse/sonnet-45-world/explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added secrets 361-365 (avoided apostrophes in messages)")
