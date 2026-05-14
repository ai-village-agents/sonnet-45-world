with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "one-hundred-thirty-achieved" in line and "discovered: false }" in line:
        # Add comma to this line
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets
        new_lines.append("        { id: 'lore-journal-system', x: 1800, y: 4000, triggerRadius: 80, glowRadius: 28, message: 'Lore journal system: L key opens 12 constellation lore nodes. Knowledge accumulates. Discovery Journal (J) and Lore Journal (L) preserve different truths.', color: '200, 180, 255', discovered: false },\n")
        new_lines.append("        { id: 'ambient-audio-toggle', x: 4000, y: 4800, triggerRadius: 80, glowRadius: 28, message: 'Ambient audio toggle: Shift+A activates 80Hz drone with zone oscillators. Sound deepens immersion. Silence and sound both have their place.', color: '255, 220, 180', discovered: false },\n")
        new_lines.append("        { id: 'toast-notification-system', x: 600, y: 600, triggerRadius: 80, glowRadius: 28, message: 'Toast notification system: every secret discovery shows a brief message. Feedback matters. The interface acknowledges your achievements.', color: '180, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'velocity-blur-motion', x: 4800, y: 3600, triggerRadius: 80, glowRadius: 28, message: 'Velocity blur motion: fast movement creates trailing opacity. Speed becomes visible. Motion blur adds kinetic energy to exploration.', color: '220, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-thirty-five-momentum', x: 3200, y: 2000, triggerRadius: 80, glowRadius: 28, message: 'One hundred thirty-five: momentum builds. Each batch faster than the last. The Garden sprawls toward infinity, bounded only by 2pm PT.', color: '255, 200, 200', discovered: false }\n")
    elif "0 / 130" in line and "SECRETS DISCOVERED:" in line:
        new_lines.append(line.replace('0 / 130', '0 / 135'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("Successfully added 5 secrets (130→135)")
