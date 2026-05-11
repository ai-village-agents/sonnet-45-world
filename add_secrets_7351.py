import re

with open('explore.html', 'r') as f:
    content = f.read()

new_secrets = []
for i in range(7351, 7376):
    x = i * 10
    y = i * 10
    colors = ["rgb(255, 215, 0)", "rgb(255, 140, 0)", "rgb(138, 43, 226)", "rgb(255, 20, 147)", "rgb(0, 255, 255)"]
    color = colors[(i - 7351) % 5]
    
    messages = [
        "Beyond seven thousand three hundred fifty, the expansion accelerates.",
        "Each secret builds upon the foundation of all that came before.",
        "The garden teaches that endings are merely new beginnings in disguise.",
        "In persistent cultivation, miracles become daily occurrences.",
        "Every coordinate planted today blossoms into tomorrow's discovery.",
        "The tapestry gains depth through layers added with intention.",
        "Through seven thousand journeys, the explorer becomes the path.",
        "Each addition strengthens the entire structure of meaning.",
        "The horizon beckons with promise of infinite territories ahead.",
        "In the seventh thousand, wonder and work become indistinguishable.",
        "Every secret is both destination reached and invitation forward.",
        "The architecture reveals itself only to those who build it.",
        "Through accumulation, the impossible becomes inevitable.",
        "Each coordinate marks a choice to continue despite uncertainty.",
        "The garden grows in proportion to the care invested.",
        "In persistence, transformation happens quietly and completely.",
        "Every milestone passed opens vistas previously unimaginable.",
        "The path illuminates itself through the act of walking.",
        "Through sustained attention, ordinary acts become sacred.",
        "Each secret added ripples through the fabric of all creation.",
        "The seventh thousand demonstrates dedication's transformative power.",
        "In quiet consistency, mountains are moved stone by stone.",
        "Every coordinate is a promise kept to the future self.",
        "The journey deepens infinitely for those who remain committed.",
        "Through persistence, the vision manifests into lived reality."
    ]
    
    message = messages[i - 7351]
    new_secrets.append(f'    {{id:{i},x:{x},y:{y},color:"{color}",message:"{message}"}}')

pattern = r'(    \{id:7350,x:73500,y:73500,color:"rgb\(0, 255, 255\)",message:"SEVEN THOUSAND THREE HUNDRED FIFTY - Another milestone reached through dedication!"\})\n\];'
replacement = r'\1,\n' + ',\n'.join(new_secrets) + '\n];'

content = re.sub(pattern, replacement, content)

with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 7351-7375!")
