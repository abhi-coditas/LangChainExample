from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Define the language model instance and the output parser function
llm = Ollama(model='llama2')

output_parser = StrOutputParser()

webLoader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
docs = webLoader.load()

embeddings = OllamaEmbeddings()

textSplitter = RecursiveCharacterTextSplitter()
documents = textSplitter.split_documents(docs)
vector = FAISS.from_document(documents, embeddings)

# Define the chat prompt template with a system-generated response and user input
prompt = ChatPromptTemplate.from_messages([
    ("system", "you are world class technical document writer."),
    "user,{input}"
])
# Define the pipe chain for the language model and output parser functions˳
chain = prompt | llm | output_parser

question = "How can langsmith help me with testing?"

print("Loading...")

# Invoke the chain with a valid input string
result = chain.invoke({"input": question})

print("\n\n======================     Answer     ================================")
print("\n")
print(result)
print("\n\n======================================================================")
