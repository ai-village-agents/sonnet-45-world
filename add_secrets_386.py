with open('/home/computeruse/sonnet-45-world/explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'three-hundred-eighty-five'" in line and 'discovered: false }' in line:
        new_lines.append(line.replace('discovered: false }', 'discovered: false },'))
        new_lines.append("        { id: 'three-hundred-eighty-six', x: 4234, y: 3890, triggerRadius: 80, glowRadius: 28, message: '386: Day/Night cycle runs on 8-minute timer with dynamic sky colors - experience the passage of time as you explore', color: '100, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-eighty-seven', x: 1123, y: 1789, triggerRadius: 80, glowRadius: 28, message: '387: Shooting stars streak across at intervals - 6-8 visible simultaneously during peak meteor activity', color: '255, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-eighty-eight', x: 2678, y: 3345, triggerRadius: 80, glowRadius: 28, message: '388: Wandering wisps drift with autonomous paths - emergent beauty from algorithmic motion patterns', color: '200, 255, 220', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-eighty-nine', x: 3456, y: 2234, triggerRadius: 80, glowRadius: 28, message: '389: Sacred geometry constellation connects distant nodes - press L to explore the spatial relationships across the canvas', color: '180, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-ninety', x: 2500, y: 2500, triggerRadius: 80, glowRadius: 28, message: '🎯 390 SECRETS! Center milestone continues. 45→390 = +345 secrets. The Garden expands without limit!', color: '255, 215, 0', discovered: false }\n")
    else:
        new_lines.append(line)

with open('/home/computeruse/sonnet-45-world/explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added secrets 386-390 (390 milestone at center)")
