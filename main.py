import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

sample_file = genai.upload_file(path='bill.png', display_name='Bills')

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

response = model.generate_content([sample_file, "Scan the image and list all the components present in the image"])

print(response.text)