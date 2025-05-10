import os
from groq import Groq

client = Groq(api_key="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")

chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "Hello, Groq!"}],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)


from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

llm = ChatGroq(
    groq_api_key="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",
    model_name="llama3-70b-8192"
)

response = llm.invoke([HumanMessage(content="Tell me a joke about lawyers.")])
print(response.content)
