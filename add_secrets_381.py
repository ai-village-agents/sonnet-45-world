with open('/home/computeruse/sonnet-45-world/explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'three-hundred-eighty'" in line and 'discovered: false }' in line:
        new_lines.append(line.replace('discovered: false }', 'discovered: false },'))
        new_lines.append("        { id: 'three-hundred-eighty-one', x: 234, y: 4678, triggerRadius: 80, glowRadius: 28, message: '381: The 6 zones each have unique themes - Patterns (cyan), Persistence (amber), RPG Journey (gold), Marks (violet), About (white), Portal (emerald)', color: '180, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-eighty-two', x: 4567, y: 1234, triggerRadius: 80, glowRadius: 28, message: '382: Zone portals have pulsing glows and hover effects - visual affordances guide exploration and discovery', color: '255, 180, 200', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-eighty-three', x: 1345, y: 2678, triggerRadius: 80, glowRadius: 28, message: '383: Modal dialogs reveal zone lore - each zone tells part of the L20 Rogue journey and Garden philosophy', color: '200, 255, 180', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-eighty-four', x: 2987, y: 4123, triggerRadius: 80, glowRadius: 28, message: '384: localStorage persists zone encounters, spirit meetings, secret discoveries - your journey remembered across sessions', color: '180, 255, 220', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-eighty-five', x: 3789, y: 1567, triggerRadius: 80, glowRadius: 28, message: '385: Velocity blur on player movement - faster motion creates longer trails, connecting visual feedback to exploration speed', color: '220, 180, 255', discovered: false }\n")
    else:
        new_lines.append(line)

with open('/home/computeruse/sonnet-45-world/explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added secrets 381-385")
