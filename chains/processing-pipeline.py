from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


template_translate = PromptTemplate(
    input_variables=["text"],
    template="Translate the following text to French \n: {text}",
)

template_summary = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in French \n: {text}",
)

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

translate_chain = template_translate | llm | StrOutputParser()

pipeline = {"text": translate_chain} | template_summary | llm | StrOutputParser()

result = pipeline.invoke(
    {"text": "Dora is an adventure girl  that likes to make dumb things"}
)
print(result)
