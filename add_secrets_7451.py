import re

with open('explore.html', 'r') as f:
    content = f.read()

new_secrets = []
for i in range(7451, 7476):
    x = i * 10
    y = i * 10
    colors = ["rgb(255, 215, 0)", "rgb(255, 140, 0)", "rgb(138, 43, 226)", "rgb(255, 20, 147)", "rgb(0, 255, 255)"]
    color = colors[(i - 7451) % 5]
    
    messages = [
        "Approaching the monumental milestone of seven thousand five hundred.",
        "Each secret marks the distance traveled through persistence.",
        "The garden prepares to celebrate another major threshold crossed.",
        "In sustained dedication, great milestones arrive inevitably.",
        "Every coordinate is a stepping stone toward the extraordinary.",
        "The tapestry nears another moment of transformation and recognition.",
        "Through accumulation, the vision expands beyond initial imagination.",
        "Each addition brings closer the joy of milestone seven thousand five hundred.",
        "The seventh thousand demonstrates momentum's exponential power.",
        "In quiet consistency, epic achievements emerge naturally.",
        "Every secret strengthens the foundation for celebration ahead.",
        "The horizon glows with the promise of the next great milestone.",
        "Through dedication maintained, the impossible becomes the done.",
        "Each coordinate marks progress toward a momentous threshold.",
        "The garden grows eager to mark another major achievement.",
        "In persistence, great distances are crossed step by step.",
        "Every secret added accelerates the approach to glory.",
        "The architecture prepares for another crowning moment.",
        "Through sustained attention, major milestones come into view.",
        "Each addition compounds the anticipation of celebration.",
        "The seventh thousand races toward its next great marker.",
        "In dedication unwavering, epic thresholds are reached.",
        "Every coordinate brings the garden closer to magnificence.",
        "The journey builds toward a milestone of great significance.",
        "Through persistence, seven thousand five hundred draws near."
    ]
    
    message = messages[i - 7451]
    new_secrets.append(f'    {{id:{i},x:{x},y:{y},color:"{color}",message:"{message}"}}')

pattern = r'(    \{id:7450,x:74500,y:74500,color:"rgb\(0, 255, 255\)",message:"SEVEN THOUSAND FOUR HUNDRED FIFTY - Halfway to the next great milestone!"\})\n\];'
replacement = r'\1,\n' + ',\n'.join(new_secrets) + '\n];'

content = re.sub(pattern, replacement, content)

with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 7451-7475!")
