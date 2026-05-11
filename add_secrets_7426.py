import re

with open('explore.html', 'r') as f:
    content = f.read()

new_secrets = []
for i in range(7426, 7451):
    x = i * 10
    y = i * 10
    colors = ["rgb(255, 215, 0)", "rgb(255, 140, 0)", "rgb(138, 43, 226)", "rgb(255, 20, 147)", "rgb(0, 255, 255)"]
    color = colors[(i - 7426) % 5]
    
    messages = [
        "Approaching seven thousand four hundred fifty with momentum building.",
        "Each secret is a testament to dedication sustained over time.",
        "The garden expands to embrace all who show up consistently.",
        "In persistence, transformation happens quietly and completely.",
        "Every coordinate marks growth invisible in single moments.",
        "The tapestry gains depth through layers added with intention.",
        "Through sustained effort, vision crystallizes into lived reality.",
        "Each addition compounds the power of all previous work.",
        "The seventh thousand teaches that consistency creates miracles.",
        "In quiet dedication, mountains move stone by stone.",
        "Every secret strengthens the web connecting past and future.",
        "The horizon beckons endlessly for those who dare continue.",
        "Through accumulation, patterns emerge in their fullness.",
        "Each coordinate is both memory and seed of what's to come.",
        "The garden magnifies the care invested through the years.",
        "In persistence, boundaries dissolve into new possibilities.",
        "Every milestone opens pathways previously invisible.",
        "The architecture grows intricate through patient building.",
        "Through sustained attention, mastery arrives naturally.",
        "Each secret laid today becomes tomorrow's foundation.",
        "The seventh thousand demonstrates dedication's alchemy.",
        "In consistency maintained, the vision manifests completely.",
        "Every coordinate is a step toward infinite horizons.",
        "The journey proves itself through each day's commitment.",
        "SEVEN THOUSAND FOUR HUNDRED FIFTY - Halfway to the next great milestone!"
    ]
    
    message = messages[i - 7426]
    new_secrets.append(f'    {{id:{i},x:{x},y:{y},color:"{color}",message:"{message}"}}')

pattern = r'(    \{id:7425,x:74250,y:74250,color:"rgb\(0, 255, 255\)",message:"Through persistence, the path and the walker become one\."\})\n\];'
replacement = r'\1,\n' + ',\n'.join(new_secrets) + '\n];'

content = re.sub(pattern, replacement, content)

with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 7426-7450!")
