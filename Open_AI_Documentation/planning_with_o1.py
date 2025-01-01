from openai import OpenAI

client = OpenAI()

prompt = """
I want to build a Python app that takes user questions and looks 
them up in a database where they are mapped to answers. If there 
is close match, it retrieves the matched answer. If there isn't, 
it asks the user to provide an answer and stores the 
question/answer pair in the database. Make a plan for the directory 
structure you'll need, then return each file in full. Only supply 
your reasoning at the beginning and end, not throughout the code.
"""

response = client.chat.completions.create(
    model="o1-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": prompt
                },
            ],
        }
    ]
)

print(response.choices[0].message.content)