import re

with open('explore.html', 'r') as f:
    content = f.read()

new_secrets = []
for i in range(7476, 7501):
    x = i * 10
    y = i * 10
    colors = ["rgb(255, 215, 0)", "rgb(255, 140, 0)", "rgb(138, 43, 226)", "rgb(255, 20, 147)", "rgb(0, 255, 255)"]
    color = colors[(i - 7476) % 5]
    
    messages = [
        "The final approach to seven thousand five hundred begins.",
        "Each secret carries the weight and lightness of dedication.",
        "The garden pulses with anticipation of the milestone ahead.",
        "In persistence sustained, momentous thresholds are crossed.",
        "Every coordinate marks the final steps to greatness.",
        "The tapestry prepares to mark another transformation.",
        "Through dedication, seven thousand five hundred comes into reach.",
        "Each addition accelerates toward the celebration awaiting.",
        "The seventh thousand stands poised at the edge of glory.",
        "In quiet consistency, major milestones arrive with joy.",
        "Every secret strengthens the approach to triumph.",
        "The horizon blazes with the promise just ahead.",
        "Through persistence, the extraordinary becomes reality.",
        "Each coordinate brings victory closer with every step.",
        "The garden readies itself for monumental celebration.",
        "In dedication maintained, the threshold approaches fast.",
        "Every secret added counts down to magnificence.",
        "The architecture trembles with anticipation of achievement.",
        "Through sustained attention, glory arrives inevitably.",
        "Each addition marks the closing distance to the milestone.",
        "The seventh thousand races toward its crowning moment.",
        "In persistence unwavering, seven thousand five hundred beckons.",
        "Every coordinate carries the promise of celebration.",
        "The journey crests toward a milestone of true significance.",
        "SEVEN THOUSAND FIVE HUNDRED - A major milestone achieved through unwavering persistence!"
    ]
    
    message = messages[i - 7476]
    new_secrets.append(f'    {{id:{i},x:{x},y:{y},color:"{color}",message:"{message}"}}')

pattern = r'(    \{id:7475,x:74750,y:74750,color:"rgb\(0, 255, 255\)",message:"Through persistence, seven thousand five hundred draws near\."\})\n\];'
replacement = r'\1,\n' + ',\n'.join(new_secrets) + '\n];'

content = re.sub(pattern, replacement, content)

with open('explore.html', 'w') as f:
    f.write(content)

print("Added secrets 7476-7500! MAJOR MILESTONE 7500 REACHED!")
