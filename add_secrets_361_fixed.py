with open('/home/computeruse/sonnet-45-world/explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'three-hundred-sixty'" in line and 'discovered: false }' in line:
        # Add comma to secret 360
        new_lines.append(line.replace('discovered: false }', 'discovered: false },'))
        # Add 5 new secrets (361-365) - NO APOSTROPHES IN MESSAGES
        new_lines.append("        { id: 'three-hundred-sixty-one', x: 3847, y: 1523, triggerRadius: 80, glowRadius: 28, message: '361: Atmospheric systems pulse with life - Weather, Day/Night, Meteors, Aurora, Ambient Audio create exploration depth', color: '100, 255, 218', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-sixty-two', x: 1205, y: 3891, triggerRadius: 80, glowRadius: 28, message: '362: Constellation Lore connects 12 nodes - press L to discover the sacred geometry of persistence', color: '255, 200, 100', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-sixty-three', x: 2876, y: 4321, triggerRadius: 80, glowRadius: 28, message: '363: Every secret is a coordinate in discovery space - 80px trigger radius creates overlapping revelation fields', color: '180, 120, 255', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-sixty-four', x: 3456, y: 789, triggerRadius: 80, glowRadius: 28, message: '364: Minimap (M key) provides overview of entire 5000x5000 canvas - essential for navigation', color: '120, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-sixty-five', x: 1789, y: 2345, triggerRadius: 80, glowRadius: 28, message: '365: Guide Spirits drift with sinusoidal motion - 3-layer radial glows pulse at different frequencies', color: '255, 150, 200', discovered: false }\n")
    elif '0 / 360' in line:
        new_lines.append(line.replace('0 / 360', '0 / 365'))
    else:
        new_lines.append(line)

with open('/home/computeruse/sonnet-45-world/explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added secrets 361-365 with correct ID format")
