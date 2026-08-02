import os

from groq import Groq

client = Groq(api_key="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",)

    

def generate(prompt):

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt ,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return(chat_completion.choices[0].message.content)
    