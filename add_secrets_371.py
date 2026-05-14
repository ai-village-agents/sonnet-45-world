with open('/home/computeruse/sonnet-45-world/explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'three-hundred-seventy'" in line and 'discovered: false }' in line:
        new_lines.append(line.replace('discovered: false }', 'discovered: false },'))
        new_lines.append("        { id: 'three-hundred-seventy-one', x: 456, y: 3789, triggerRadius: 80, glowRadius: 28, message: '371: Aurora Borealis system creates 3-5 flowing ribbons that dance across the sky with gradient waves', color: '100, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-seventy-two', x: 4789, y: 2345, triggerRadius: 80, glowRadius: 28, message: '372: Meteor showers occur every 2-4 minutes with Web Audio synthesis: 100Hz + 2000Hz tones create cosmic ambiance', color: '255, 180, 120', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-seventy-three', x: 1567, y: 4234, triggerRadius: 80, glowRadius: 28, message: '373: Discovery Journal (J key) records every secret found with timestamp and message - your personal exploration log', color: '200, 180, 255', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-seventy-four', x: 3234, y: 1678, triggerRadius: 80, glowRadius: 28, message: '374: Aurora Achievements (A key) tracks milestones - distance, secrets, zones, spirits, lore - with progress bars', color: '180, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-seventy-five', x: 2890, y: 3567, triggerRadius: 80, glowRadius: 28, message: '375: The player aurora halo cycles through cyan→violet→amber→gold gradients, leaving sparkle trails and velocity blur', color: '255, 200, 180', discovered: false }\n")
    else:
        new_lines.append(line)

with open('/home/computeruse/sonnet-45-world/explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added secrets 371-375")
