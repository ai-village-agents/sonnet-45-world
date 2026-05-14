with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'one-hundred-eighty'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (180→185)
        new_lines.append("        { id: 'one-hundred-eighty-one', x: 600, y: 1200, triggerRadius: 80, glowRadius: 28, message: 'The aurora halo cycles: cyan to violet to amber to gold. Four colors, endless combinations, persistent animation at 60fps.', color: '0, 255, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-eighty-two', x: 4400, y: 2600, triggerRadius: 80, glowRadius: 28, message: 'Eight guide spirits drift across the canvas, each with their own wisdom. They remember every visitor who approaches.', color: '200, 150, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-eighty-three', x: 2200, y: 4200, triggerRadius: 80, glowRadius: 28, message: 'Meteors arrive every 2-4 minutes: 15-25 shooting stars with glowing trails and audio. A celebration of transient beauty.', color: '255, 180, 100', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-eighty-four', x: 800, y: 4400, triggerRadius: 80, glowRadius: 28, message: 'Three weather systems cycle through the Garden: Stardust, Aurora-Rain, and Clear skies. Each brings its own atmosphere.', color: '150, 200, 255', discovered: false },\n")
        new_lines.append("        { id: 'one-hundred-eighty-five', x: 3600, y: 600, triggerRadius: 80, glowRadius: 28, message: '185 secrets hidden across 25 million coordinate pairs. The vastness makes each discovery feel earned, intentional, meaningful.', color: '255, 215, 180', discovered: false }\n")
    elif '0 / 180' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 180', '0 / 185'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (180→185)")
print("✓ Updated counter to 0 / 185")
