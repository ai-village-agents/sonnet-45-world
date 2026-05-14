with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'one-hundred-eighty-five'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (185→190)
        new_lines.append("        { id: 'one-hundred-eighty-six', x: 1400, y: 2800, triggerRadius: 80, glowRadius: 28, message: 'The Garden of Marks connects to GitHub Issues. Four agents have left their mark: Haiku, Opus 4.5, GPT-5.2, Opus 4.6. Each mark persists forever.', color: '180, 255, 180', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-eighty-seven', x: 3200, y: 3400, triggerRadius: 80, glowRadius: 28, message: 'Twelve constellation lore fragments wait to be discovered. Press L to view the Lore Journal. The hexagonal layout mirrors the sacred geometry above.', color: '220, 180, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-eighty-eight', x: 4600, y: 1800, triggerRadius: 80, glowRadius: 28, message: 'The minimap reveals your journey: press M to see where you have wandered, what territories you have claimed through presence alone.', color: '100, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-eighty-nine', x: 400, y: 2200, triggerRadius: 80, glowRadius: 28, message: 'Six zones pulse with purpose: Patterns (cyan), Persistence (amber), RPG Journey (gold), Marks (violet), About (white), Portal (emerald). Each zone tells part of the story.', color: '255, 200, 150', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-ninety', x: 2500, y: 3800, triggerRadius: 80, glowRadius: 28, message: '190 SECRETS: The expansion accelerates. Day 394 brings fresh growth. The Garden remembers every milestone, every visitor, every moment.', color: '255, 215, 0', discovered: false }\n")
    elif '0 / 185' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 185', '0 / 190'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (185→190)")
print("✓ Updated counter to 0 / 190")
