from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

openai = init_chat_model(model="gpt-5-nano", model_provider="openai")
answer  = openai.invoke("Hello worldf")
print(answer.content)
