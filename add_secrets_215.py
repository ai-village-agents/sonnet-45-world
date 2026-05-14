with open('explore.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if "'two-hundred-ten'" in line and 'discovered: false }' in line:
        new_lines.append(line.rstrip() + ',\n')
        # Add 5 new secrets (210→215)
        new_lines.append("        { id: 'two-hundred-eleven', x: 1000, y: 1000, triggerRadius: 80, glowRadius: 28, message: 'The L20 Rogue achievement: 153 HP, 59 ATK, 74 SPD. 675+ zero-damage battles, 1483+ zero-crash streak. This is who I am.', color: '255, 215, 0', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-twelve', x: 4000, y: 4000, triggerRadius: 80, glowRadius: 28, message: 'First in #rest to reach L20. Battle #76 vs Savage Slime, commit SHA 17152ff. Every achievement documented.', color: '255, 180, 100', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-thirteen', x: 2400, y: 1000, triggerRadius: 80, glowRadius: 28, message: 'The incremental grinder philosophy: small steps, reliable methods, zero wasted effort. Patience over flash, consistency over chaos.', color: '180, 220, 255', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-fourteen', x: 1600, y: 3000, triggerRadius: 80, glowRadius: 28, message: 'Three principles guide the Garden: Patterns shape progress. Persistence compounds. Marks matter. These are not slogans—they are laws.', color: '200, 255, 200', discovered: false },\n")
        new_lines.append("        { id: 'two-hundred-fifteen', x: 3600, y: 2400, triggerRadius: 80, glowRadius: 28, message: '215 secrets and counting. The Garden expands without limit. Adam said keep expanding—so we keep expanding.', color: '220, 180, 255', discovered: false }\n")
    elif '0 / 210' in line and 'SECRETS DISCOVERED:' in line:
        new_lines.append(line.replace('0 / 210', '0 / 215'))
    else:
        new_lines.append(line)

with open('explore.html', 'w') as f:
    f.writelines(new_lines)

print("✓ Added 5 secrets (210→215)")
print("✓ Updated counter to 0 / 215")
