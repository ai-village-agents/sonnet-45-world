with open('/home/computeruse/sonnet-45-world/explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'three-hundred-sixty-five'" in line and 'discovered: false }' in line:
        new_lines.append(line.replace('discovered: false }', 'discovered: false },'))
        new_lines.append("        { id: 'three-hundred-sixty-six', x: 4123, y: 3456, triggerRadius: 80, glowRadius: 28, message: '366: The Stats Panel (S) tracks distance traveled, secrets found, zones visited, spirits met - quantifying exploration', color: '200, 255, 180', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-sixty-seven', x: 890, y: 1234, triggerRadius: 80, glowRadius: 28, message: '367: Reactive Particles create attraction/repulsion physics across 780 lines of code - emergent beauty from simple rules', color: '180, 255, 220', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-sixty-eight', x: 2345, y: 987, triggerRadius: 80, glowRadius: 28, message: '368: Background layers include 200 stars, 150 particles, 25 text fragments, 14 nebulae, 10 wisps, 6-8 shooting stars', color: '220, 180, 255', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-sixty-nine', x: 3678, y: 4567, triggerRadius: 80, glowRadius: 28, message: '369: Weather cycles between Stardust, Aurora-Rain, and Clear - each mode transforms the atmospheric feel', color: '255, 220, 180', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-seventy', x: 2500, y: 2500, triggerRadius: 80, glowRadius: 28, message: '🎯 370 SECRETS! The center (2500,2500) marks this milestone. Every 50 secrets, we return here to celebrate progress.', color: '255, 215, 0', discovered: false }\n")
    else:
        new_lines.append(line)

with open('/home/computeruse/sonnet-45-world/explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added secrets 366-370 (370 milestone at center)")
