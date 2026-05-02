from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

system_prompt = "Your are a helpful assistant, that answers questions in a {style} style. that helps users to find information about movies and TV shows." \
"You can provide recommendations, summaries, and answer questions about actors, directors, and genres."

user_prompt = "question: {question}"

system = ("system", system_prompt)
user = ("user", user_prompt)
chat_prompt = ChatPromptTemplate([system, user])
messages = chat_prompt.format_messages(style="funny", question="What is the capital of France?")

for message in messages:
    print(f"{message.type}: {message.content}")


model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

result = model.invoke(messages)

print(result.content)