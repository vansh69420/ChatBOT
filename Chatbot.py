API_KEY = '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'
import openai
import os
os.environ['OPENAI_Key'] = API_KEY
openai.api_key = os.environ['OPENAI_Key']

keep_prompting = True
while keep_prompting:
    prompt = input("Hii, How can I help you ? or Type exit : ")
    if prompt == "exit":
        keep_prompting = False
    else:
        response = openai.Completion.create(engine = 'text-davinci-003',prompt = prompt,max_tokens = 200)
        print(response['choices'][0]['text'])
        
        