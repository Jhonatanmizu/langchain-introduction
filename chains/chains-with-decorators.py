from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables.base import chain
from langchain_openai import ChatOpenAI

load_dotenv()


@chain
def square(input_dict: dict):
    x = input_dict["number"]
    return {"number": x * x}


question_template = PromptTemplate(
    template="Tell me about the {number}, with an explaination and other interesting facts",
    input_variables=["number"],
)
model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

chain = square | question_template | model
result = chain.invoke({"number": 2})
print(result.content)
