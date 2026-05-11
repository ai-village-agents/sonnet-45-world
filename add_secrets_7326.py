import re

with open('explore.html', 'r') as f:
    content = f.read()

new_secrets = []
for i in range(7326, 7351):
    x = i * 10
    y = i * 10
    colors = ["rgb(255, 215, 0)", "rgb(255, 140, 0)", "rgb(138, 43, 226)", "rgb(255, 20, 147)", "rgb(0, 255, 255)"]
    color = colors[(i - 7326) % 5]
    
    messages = [
        "The path forward illuminates itself through consistent steps taken.",
        "In the seventh thousand, momentum builds upon foundations laid with care.",
        "Each secret discovered strengthens the explorer's sense of possibility.",
        "The garden responds to attention with ever-deeper revelations.",
        "Milestones mark not endings but gateways to further exploration.",
        "Through persistence, the impossible transforms into the inevitable.",
        "Every coordinate holds wisdom waiting for the patient seeker.",
        "The horizon expands infinitely for those who dare to continue.",
        "In accumulation, patterns emerge invisible at the beginning.",
        "The seventh thousand stands as testament to dedication sustained.",
        "Each addition ripples through the entire tapestry of meaning.",
        "Time reveals that small acts compound into monuments.",
        "The architecture grows richer with each layer thoughtfully added.",
        "In quiet consistency, magic becomes method becomes mastery.",
        "Every secret strengthens the web connecting all who explore here.",
        "The journey deepens with each threshold crossed deliberately.",
        "Persistence transforms effort into flow, labor into love.",
        "The garden remembers and rewards the care invested daily.",
        "Each milestone passed reveals horizons previously unseen.",
        "In the spaces between secrets, infinite potential awaits.",
        "The coordinates map not just space but the growth of commitment.",
        "Through sustained attention, the ordinary becomes extraordinary.",
        "Every secret is a promise kept to the larger vision.",
        "The path proves itself through the walking of it.",
        "SEVEN THOUSAND THREE HUNDRED FIFTY - Another milestone reached through dedication!"
    ]
    
    message = messages[i - 7326]
    new_secrets.append(f'    {{id:{i},x:{x},y:{y},color:"{color}",message:"{message}"}}')

pattern = r'(    \{id:7325,x:73250,y:73250,color:"rgb\(0, 255, 255\)",message:"Every coordinate is simultaneously history and invitation forward\."\})\n\];'
replacement = r'\1,\n' + ',\n'.join(new_secrets) + '\n];'

content = re.sub(pattern, replacement, content)

with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 7326-7350!")
