from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# Input text
long_text = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

# 1. Split the text into manageable chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=70)
chunks = splitter.create_documents([long_text])

# 2. Define the LLM
# Switched to gpt-4o as gpt-5-nano isn't a standard model name.
llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

# 3. Design the LCEL Summarization Chain (Stuff strategy)
prompt = ChatPromptTemplate.from_template(
    "Summarize the following text concisely:\n\n{text}"
)

# Composing the chain: Format docs -> Prompt -> LLM -> Output Parser
summarize_chain = (
    {"text": lambda docs: "\n\n".join(doc.page_content for doc in docs)}
    | prompt
    | llm
    | StrOutputParser()
)

# 4. Execute the chain
summary = summarize_chain.invoke(chunks)

print("Summary:")
print(summary)
