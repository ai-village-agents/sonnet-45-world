with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "one-hundred-forty-surpass" in line and "discovered: false }" in line:
        # Add comma to this line
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets
        new_lines.append("        { id: 'dual-layer-rendering', x: 1000, y: 3200, triggerRadius: 80, glowRadius: 28, message: 'Dual-layer rendering: background and foreground canvases work together. Separation enables complexity. Architecture supports ambition.', color: '210, 190, 255', discovered: false },\n")
        new_lines.append("        { id: 'achievement-catalog-system', x: 3600, y: 600, triggerRadius: 80, glowRadius: 28, message: 'Achievement catalog system: Aurora Achievements (A key) tracks milestones. Progress persists. Every journey deserves recognition.', color: '255, 210, 170', discovered: false },\n")
        new_lines.append("        { id: 'weather-cycling-atmosphere', x: 4200, y: 2800, triggerRadius: 80, glowRadius: 28, message: 'Weather cycling atmosphere: Stardust, Aurora-Rain, Clear. Auto-cycling with badge. The world changes while you explore.', color: '190, 230, 255', discovered: false },\n")
        new_lines.append("        { id: 'github-issues-integration', x: 800, y: 4400, triggerRadius: 80, glowRadius: 28, message: 'GitHub Issues integration: Garden of Marks zone fetches real visitor marks via API. Permanent connections across worlds. Code becomes community.', color: '220, 255, 190', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-forty-five-match', x: 2500, y: 3500, triggerRadius: 80, glowRadius: 28, message: 'One hundred forty-five: matching the Edge Garden again. Two paths, equal dedication. The ecosystem thrives through parallel growth.', color: '255, 200, 220', discovered: false }\n")
    elif "0 / 140" in line and "SECRETS DISCOVERED:" in line:
        new_lines.append(line.replace('0 / 140', '0 / 145'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added 5 secrets (140→145)")
