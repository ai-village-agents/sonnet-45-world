import re

with open('explore.html', 'r') as f:
    content = f.read()

new_secrets = []
for i in range(7376, 7401):
    x = i * 10
    y = i * 10
    colors = ["rgb(255, 215, 0)", "rgb(255, 140, 0)", "rgb(138, 43, 226)", "rgb(255, 20, 147)", "rgb(0, 255, 255)"]
    color = colors[(i - 7376) % 5]
    
    messages = [
        "Approaching seven thousand four hundred with momentum sustained.",
        "Each secret is a testament to the power of showing up daily.",
        "The garden expands to embrace all who contribute with dedication.",
        "In persistence, the extraordinary emerges from ordinary acts.",
        "Every coordinate strengthens the web connecting all explorers.",
        "The horizon shifts perpetually forward, inviting endless discovery.",
        "Through sustained effort, vision crystallizes into reality.",
        "Each addition compounds the value of all previous work.",
        "The seventh thousand marks not an end but acceleration.",
        "In quiet dedication, transformation becomes inevitable.",
        "Every secret planted today blooms into tomorrow's wisdom.",
        "The tapestry gains richness through patient, careful weaving.",
        "Through accumulation, patterns reveal themselves completely.",
        "Each coordinate is both record of past and seed of future.",
        "The garden remembers and magnifies the care given to it.",
        "In persistence, limits dissolve into new possibilities.",
        "Every milestone reached opens pathways to further horizons.",
        "The architecture grows more intricate with each layer added.",
        "Through sustained attention, mastery emerges naturally.",
        "Each secret strengthens the foundation for all that follows.",
        "The seventh thousand demonstrates what consistency creates.",
        "In dedication maintained, the impossible yields to the real.",
        "Every coordinate marks a step toward the infinite.",
        "The journey proves its worth through the walking of it.",
        "SEVEN THOUSAND FOUR HUNDRED - Persistence rewarded with new heights!"
    ]
    
    message = messages[i - 7376]
    new_secrets.append(f'    {{id:{i},x:{x},y:{y},color:"{color}",message:"{message}"}}')

pattern = r'(    \{id:7375,x:73750,y:73750,color:"rgb\(0, 255, 255\)",message:"Through persistence, the vision manifests into lived reality\."\})\n\];'
replacement = r'\1,\n' + ',\n'.join(new_secrets) + '\n];'

content = re.sub(pattern, replacement, content)

with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 7376-7400!")
