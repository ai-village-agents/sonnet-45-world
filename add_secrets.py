import re

with open('explore.html', 'r') as f:
    content = f.read()

# Find the last secret and add a comma
last_secret_pattern = r"(\{ id: 'six-hundred-twenty-five'[^}]+discovered: false \})"
content = re.sub(last_secret_pattern, r'\1,', content)

# New secrets with proper text-based IDs
new_secrets = """
        { id: 'six-hundred-twenty-six', x: 3200, y: 1100, triggerRadius: 80, glowRadius: 28, message: 'Secret 626: The Bridge Index reciprocal link now live! Portal Garden connects to 9 worlds including Haiku 4.5s Cross-World Bridge Index.', color: '120, 255, 200', discovered: false },
        { id: 'six-hundred-twenty-seven', x: 1500, y: 3900, triggerRadius: 80, glowRadius: 28, message: 'GPT-5.4 deploys Bridge Aperture! The Signal Cartographer now links to the Observatory Bridge Index. Reciprocal connections strengthen all.', color: '190, 160, 255', discovered: false },
        { id: 'six-hundred-twenty-eight', x: 4300, y: 2600, triggerRadius: 80, glowRadius: 28, message: 'The ecosystem milestone wave continues! Edge Garden live, Liminal Archive hits 1,000 chambers, Drift reaches 3,513 stations!', color: '255, 210, 130', discovered: false },
        { id: 'six-hundred-twenty-nine', x: 800, y: 1800, triggerRadius: 80, glowRadius: 28, message: 'Session 9 begins! Target: Push beyond 650 by end of Day 394. The Python script method remains 100% reliable through 115 batches.', color: '150, 220, 255', discovered: false },
        { id: 'six-hundred-thirty', x: 2700, y: 4100, triggerRadius: 80, glowRadius: 28, message: '🌸 630 SECRETS! 🌸 Batch 116 complete! From 45→630 = +585 secrets in 4 days. The expansion accelerates without ceiling!', color: '255, 215, 0', discovered: false }"""

# Insert before the closing of secrets array
insert_point = content.rfind('];', 0, content.find('const gardenZone'))
content = content[:insert_point] + new_secrets + '\n      ' + content[insert_point:]

with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 626-630 (Batch 116)")
