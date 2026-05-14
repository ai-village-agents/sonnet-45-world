with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "one-hundred-twenty-five-pattern" in line and "discovered: false }" in line:
        # Add comma to this line
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets
        new_lines.append("        { id: 'zone-modal-dialogs', x: 2000, y: 3000, triggerRadius: 80, glowRadius: 28, message: 'Zone modal dialogs: six interactive zones with philosophy and visitor prompts. Each one invites reflection. The garden speaks to those who listen.', color: '240, 180, 255', discovered: false },\n")
        new_lines.append("        { id: 'sparkle-trail-beauty', x: 1200, y: 1000, triggerRadius: 80, glowRadius: 28, message: 'Sparkle trail beauty: every movement leaves temporary light. Your path becomes visible art. Motion creates meaning through luminous traces.', color: '255, 240, 200', discovered: false },\n")
        new_lines.append("        { id: 'sixty-fps-commitment', x: 3800, y: 3200, triggerRadius: 80, glowRadius: 28, message: 'Sixty FPS commitment: smooth rendering at all times. Performance enables immersion. Technical excellence supports aesthetic vision.', color: '180, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'google-fonts-typography', x: 4400, y: 2000, triggerRadius: 80, glowRadius: 28, message: 'Google Fonts typography: Cinzel for titles, Inter for body. Font choices shape mood. Elegant serif meets clean sans-serif.', color: '255, 200, 160', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-thirty-achieved', x: 2500, y: 2900, triggerRadius: 80, glowRadius: 28, message: 'One hundred thirty secrets: matching Opus 4.5 Edge Garden. Two different visions, same dedication. The ecosystem grows together, each world unique.', color: '200, 255, 240', discovered: false }\n")
    elif "0 / 125" in line and "SECRETS DISCOVERED:" in line:
        new_lines.append(line.replace('0 / 125', '0 / 130'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added 5 secrets (125→130)")
