from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
from dotenv import load_dotenv

load_dotenv()
model: ChatOpenAI = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

message: AIMessage = model.invoke("Hello world")

print(message.content)