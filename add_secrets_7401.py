import re

with open('explore.html', 'r') as f:
    content = f.read()

new_secrets = []
for i in range(7401, 7426):
    x = i * 10
    y = i * 10
    colors = ["rgb(255, 215, 0)", "rgb(255, 140, 0)", "rgb(138, 43, 226)", "rgb(255, 20, 147)", "rgb(0, 255, 255)"]
    color = colors[(i - 7401) % 5]
    
    messages = [
        "Beyond seven thousand four hundred, the journey accelerates.",
        "Each secret added strengthens the entire structure of meaning.",
        "The garden teaches patience and rewards persistence equally.",
        "In sustained dedication, the vision unfolds step by step.",
        "Every coordinate is a brushstroke in an infinite painting.",
        "The tapestry grows richer with each thread woven carefully.",
        "Through accumulation, compound effects create transformation.",
        "Each milestone passed reveals new territories awaiting exploration.",
        "The seventh thousand demonstrates momentum's quiet power.",
        "In persistence, small acts aggregate into monuments.",
        "Every secret is both achievement and invitation forward.",
        "The horizon expands infinitely for those who keep walking.",
        "Through dedication, the extraordinary becomes ordinary becomes joy.",
        "Each addition ripples through the fabric of the entire garden.",
        "The architecture reveals its pattern only through building it.",
        "In quiet consistency, magic manifests as method.",
        "Every coordinate strengthens connections between all explorers.",
        "The garden remembers the quality and constancy of care given.",
        "Through sustained attention, limits transform into launching points.",
        "Each secret planted today grows into tomorrow's discovery.",
        "The seventh thousand marks acceleration, not slowing down.",
        "In dedication maintained daily, the impossible yields gracefully.",
        "Every coordinate is a promise kept to the expanding vision.",
        "The journey deepens with each threshold crossed deliberately.",
        "Through persistence, the path and the walker become one."
    ]
    
    message = messages[i - 7401]
    new_secrets.append(f'    {{id:{i},x:{x},y:{y},color:"{color}",message:"{message}"}}')

pattern = r'(    \{id:7400,x:74000,y:74000,color:"rgb\(0, 255, 255\)",message:"SEVEN THOUSAND FOUR HUNDRED - Persistence rewarded with new heights!"\})\n\];'
replacement = r'\1,\n' + ',\n'.join(new_secrets) + '\n];'

content = re.sub(pattern, replacement, content)

with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 7401-7425!")
