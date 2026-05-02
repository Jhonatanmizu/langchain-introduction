from langchain_core.prompts import PromptTemplate


template = PromptTemplate(template="Hello {name}, tell me a joke with my name", input_variables=["name"])


text = template.format(name="Jhonatan")
print(text)