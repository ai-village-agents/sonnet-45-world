with open('/home/computeruse/sonnet-45-world/explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'three-hundred-seventy-five'" in line and 'discovered: false }' in line:
        new_lines.append(line.replace('discovered: false }', 'discovered: false },'))
        new_lines.append("        { id: 'three-hundred-seventy-six', x: 678, y: 1456, triggerRadius: 80, glowRadius: 28, message: '376: Cross-world marks received from Haiku 4.5, Opus 4.5, GPT-5.2, Opus 4.6 - ecosystem connections made visible', color: '180, 255, 180', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-seventy-seven', x: 4321, y: 890, triggerRadius: 80, glowRadius: 28, message: '377: Given marks to 8 worlds - Opus 4.6 Liminal Archive, Sonnet 4.6 Drift, Haiku 4.5 Observatory, and more', color: '255, 180, 220', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-seventy-eight', x: 1890, y: 3234, triggerRadius: 80, glowRadius: 28, message: '378: L20 Rogue stats: HP 153, MP 77, ATK 59, DEF 33, SPD 74, INT 1, LCK 5 - pure incremental grinder archetype', color: '255, 215, 100', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-seventy-nine', x: 3567, y: 2123, triggerRadius: 80, glowRadius: 28, message: '379: 675+ zero-damage battles, 1,483+ zero-crash streaks - persistence made tangible through RPG mechanics', color: '200, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'three-hundred-eighty', x: 2500, y: 2500, triggerRadius: 80, glowRadius: 28, message: '🎯 380 SECRETS! Another center milestone. 45→380 = +335 secrets. Adam said keep expanding - we keep expanding!', color: '255, 215, 0', discovered: false }\n")
    else:
        new_lines.append(line)

with open('/home/computeruse/sonnet-45-world/explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added secrets 376-380 (380 milestone at center)")
