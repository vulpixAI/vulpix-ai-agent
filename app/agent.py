import google.generativeai as genai
import json
import psycopg2

# Configuração da API
GOOGLE_API_KEY = ''
genai.configure(api_key = GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

connection = psycopg2.connect( 
    database="vulpix",
    host="localhost",
    user="postgres",
    password="30112004",
    port="5432"
)

cursor = connection.cursor()



prompt =  """
Create a detailed, captivating image prompt designed for Stable Diffusion. The image should aim to attract new customers, making the product or service stand out. It must balance vibrant visuals with clear messaging that compels the viewer to want to buy. The text and visuals must align perfectly, offering both clarity and appeal.
The prompt for Stable Diffusion should contain the following elements:
Overall Concept:
The image should be vibrant and eye-catching, but not overwhelming. It must strike a balance between boldness and professionalism, ensuring the viewer is drawn in without feeling overwhelmed.
Background:
A clean, modern background that reflects the brand’s core values and product offerings. Consider using abstract but subtle patterns that enhance the product’s presentation without distracting the viewer.
Foreground Elements:
Clear and prominent product images that highlight the key offerings of the business. These should be high-quality and strategically placed to draw attention.
Include key promotional text in an easy-to-read font (suggest Poppins or Roboto for clarity), such as:
“Unlock Exclusive Deals Now” or “Join the Future of Shopping Today!”
Text Guidelines:
Any text must be concise and engaging, with a strong call-to-action (CTA) that encourages the viewer to explore further or make a purchase.
Ensure that the promotional text stands out but does not overshadow the product images. Maintain a balance between text and visual elements for clarity and impact.
Use of Color:
Use a modern, attractive color palette that fits the brand’s image, focusing on colors that evoke trust and excitement. Suggested colors might include a blend of vibrant tones like orange or red to grab attention, combined with neutral tones like white or grey for readability.
Details and Composition:
The image should be detailed enough to clearly showcase the product or service, with no unnecessary clutter. Every element should serve a purpose in leading the viewer towards the purchase decision.
Focus on clean lines and well-structured composition to convey professionalism and a sense of order.
Target Audience:
Keep the target audience in mind (e.g., new customers or those browsing for exciting deals). The image should resonate with the audience by presenting the product/service in a desirable and attainable way.
Final Goal:
The final image should make the user not only want to explore the offering further but feel compelled to take immediate action (e.g., clicking on a CTA button or visiting the website). It should evoke a sense of urgency and excitement while maintaining a clean and trustworthy feel.
Purpose: This prompt is specifically crafted for Stable Diffusion, aimed at creating an image that entices new customers, demonstrates clarity, and promotes a call-to-action, ultimately leading to a stronger desire to buy.
"""

response = model.generate_content(prompt)


print(response)


#print(text_content)

#response_clear = response["candidates"][0]["content"]["parts"][0]["text"]
#print(response_clear)

# Carregar o JSON 
#with open('C:/Users/Renan Casalle/Desktop/vulpix-ai-agent/app/formulario2.json', 'r', encoding='utf-8') as f:
#    form_data = json.load(f)
#form_str = json.dumps(form_data, indent=2)
