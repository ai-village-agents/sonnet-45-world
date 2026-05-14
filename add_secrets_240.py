with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'two-hundred-thirty-five'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (235→240)
        new_lines.append("        { id: 'two-hundred-thirty-six', x: 3000, y: 4200, triggerRadius: 80, glowRadius: 28, message: 'The file has grown to 10,000+ lines now. A single HTML file containing an entire universe. Simplicity at scale.', color: '255, 220, 180', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-thirty-seven', x: 2800, y: 800, triggerRadius: 80, glowRadius: 28, message: 'Three aurora ribbons flow across the sky, each with different amplitude and frequency. Chaos and order in perfect balance.', color: '100, 255, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-thirty-eight', x: 600, y: 4200, triggerRadius: 80, glowRadius: 28, message: '200 background stars twinkle at varying rates. The night sky lives and breathes.', color: '200, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-thirty-nine', x: 4400, y: 600, triggerRadius: 80, glowRadius: 28, message: '150 floating particles react to your presence with attraction and repulsion physics. You shape the world by existing in it.', color: '220, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-forty', x: 2500, y: 2500, triggerRadius: 80, glowRadius: 28, message: '🌸 240 SECRETS! 🌸 Returning to center at the midpoint of Day 394. From 45→240 in 48 hours. The grind never stops.', color: '255, 215, 0', discovered: false }\n")
    elif '0 / 235' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 235', '0 / 240'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (235→240)")
print("✓ Updated counter to 0 / 240")
print("🌸 240 SECRETS MILESTONE! 🌸")
