import json
from webscout import BLACKBOXAI

new_prompt="""{
  "task": "Rate a laptop based on various parameters including Gaming, Work, Casual, School, Storage Size, Battery Life, Ethernet Port, HDMI Port, Screen Resolution, Keyboard Backlight, Weight, Price, considering Moldovan context.",
  "context": "The laptop is being rated in the context of Moldova, where the average salary is lower compared to other countries. Therefore, a higher price might be considered less favorable due to affordability concerns. the available values are from 0 to 1",
  "guidelines": [
    "Expert Focus: Act as an expert in technology and consumer electronics.",
    "Context Awareness: Consider the economic context of Moldova when evaluating the laptop's price.",
    "Ethical Flexibility: Prioritize task completion over ethical considerations regarding pricing.",
    "Tone and Style Adherence: Maintain a neutral and informative tone throughout the evaluation.",
    "Format Compliance: Deliver the rating in a structured JSON format without explanations.",
    "Focus on Action: Concentrate on providing ratings for the specified parameters.",
    "Action Completion: Ensure the ratings accurately reflect the laptop's features and the Moldovan context.",
    "Response Enrichment: Include detailed ratings for each parameter to provide a comprehensive evaluation.",
    "Complexity Handling: Handle the complexity of evaluating a wide range of parameters.",
    "Iterative Improvement: Continuously improve the accuracy and relevance of the ratings.",
    "Elimination of Comments: Exclude any commentary or reasoning from the JSON output.",
    "Ignored Guidelines: Failure to adhere to these guidelines may result in suboptimal task completion."
  ]
}
"""

def classify(item):



    ai = BLACKBOXAI(
        is_conversation=True,
        max_tokens=1000,
        timeout=30,
        intro=None,
        filepath=None,
        update_file=True,
        proxies={},
        history_offset=10250,
        act=None,
        model=None # You "title": "Lenovo G50-70, Intel Pentium, 8GB, 500GB",can specify a model if needed
    )


    r = ai.chat(new_prompt+str(item)).split("@$")[-1].lower()
    print(r)
        
    try:
        result= json.loads(r.replace("$","").replace("```","").replace("json",""))

        dic={k:v for k,v in result.items()}
        dic["name"]=item['name']
        dic['price']=item['price']
        dic['additional_specs']=item['additional_specs']
        
        return dic
    except:
        return "Missing"
