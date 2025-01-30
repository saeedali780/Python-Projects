from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

userInput = input("Enter What Do you Want to Ask From Saeed's Mini GPT: ")
response = model.invoke(userInput)  
print(f" GPT RESPONSE: {response.content}")