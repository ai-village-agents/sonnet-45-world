with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "one-hundred-fifteen-rhythm" in line and "discovered: false }" in line:
        # Add comma to this line
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets
        new_lines.append("        { id: 'day-night-cycle-poetry', x: 2200, y: 4600, triggerRadius: 80, glowRadius: 28, message: 'Day-night cycle poetry: 8-minute cycles of DAWN/DAY/DUSK/NIGHT. Time flows visibly. The sky tells stories through color gradients.', color: '255, 190, 140', discovered: false },\n")
        new_lines.append("        { id: 'meteor-shower-audio', x: 4800, y: 2600, triggerRadius: 80, glowRadius: 28, message: 'Meteor shower audio: Web Audio API generates 100Hz + 2000Hz dual-tone synthesis. Every 2-4 minutes, the sky sings with falling stars.', color: '200, 160, 255', discovered: false },\n")
        new_lines.append("        { id: 'aurora-gradient-cycling', x: 1000, y: 1600, triggerRadius: 80, glowRadius: 28, message: 'Aurora gradient cycling: cyan to violet to amber to gold. The player pulses with northern light colors. Beauty in continuous transformation.', color: '180, 255, 240', discovered: false },\n")
        new_lines.append("        { id: 'fog-of-war-exploration', x: 3600, y: 3800, triggerRadius: 80, glowRadius: 28, message: 'Fog of war exploration: Opus 4.6 uses this beautifully. The unknown beckons. Discovery feels meaningful when darkness yields to light.', color: '220, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-twenty-milestone', x: 2500, y: 2100, triggerRadius: 80, glowRadius: 28, message: 'One hundred twenty secrets: from 100 to 120 in minutes. The expansion accelerates. Adam wanted sprawling worlds. The Garden obliges.', color: '255, 215, 200', discovered: false }\n")
    elif "0 / 115" in line and "SECRETS DISCOVERED:" in line:
        new_lines.append(line.replace('0 / 115', '0 / 120'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added 5 secrets (115→120)")
