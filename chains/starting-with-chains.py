from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

question_template = PromptTemplate(
    template="Hello {name}, what is your favorite color?", input_variables=["name"]
)
model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

chain = question_template | model
result = chain.invoke({"name": "Jhonatan"})
print(result.content)
