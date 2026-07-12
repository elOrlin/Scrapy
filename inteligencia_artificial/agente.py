import os
from dotenv import load_dotenv
from openai import OpenAI
#import anthropic
#from IPython.display import Markdown, display, update_display

#import google.generativeai

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
  print('es hora de programar con chatgpt')

# conectar con los modelos llms

openai = OpenAI()

#claude = anthropic.Anthropic()

#google.generativeai.configure()

#ahora vamos a usar los llms

system_message = "Eres un asistente que es genial programando en python"
user_prompt = "Dame explicaciones elites de como organizar mis proyecto backend usando django, flake8, drf, postgres, pytest, prometheus, grafana logging, render ia generativa y Docker por cada aplicacion quiero crear carpetas organizadas en pytest usando factory, los fixture, smoke y los test organizados aparte "

prompts = [
  {'role': 'system', 'content': system_message},
  {'role': 'user', 'content': user_prompt}
]

#GPT-3.5-TURBO

completion = openai.chat.completions.create(model='gpt-5.5', messages=prompts)
print(completion.choices[0].message.content)


#GPT-4o-mini
#El ajuste de la temperatura controla la creatividad

completion = openai.chat.completions.create(
  model='gpt-5.5',
  messages=prompts,
  #temperature=0.7
)

print(completion.choices[0].message.content)