import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

if not groq_api_key:
    raise ValueError("Set GROQ_API_KEY to use Groq for answer generation.")
if not openai_api_key:
    raise ValueError("Set OPENAI_API_KEY to use OpenAI for embeddings.")

docs: list[Document] = []

if not docs:
    raise ValueError("Add at least one LangChain Document to docs before indexing.")

embedding_function = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=openai_api_key,
)

vectorstore = Chroma.from_documents(
    docs,
    embedding=embedding_function,
    persist_directory="./chroma_db",
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2},
)

llm = ChatOpenAI(
    model="openai/gpt-oss-20b",
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)

rag_chain = (
    ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Answer the question using only the provided context. "
                "If the context does not contain the answer, say you do not know.",
            ),
            ("human", "Context:\n{context}\n\nQuestion: {question}"),
        ]
    )
    | llm
    | StrOutputParser()
)


def answer_question(question: str) -> str:
    retrieved_documents = retriever.invoke(question)
    if not retrieved_documents:
        raise ValueError("No documents were retrieved for the question.")

    context = "\n\n".join(document.page_content for document in retrieved_documents)
    return rag_chain.invoke({"context": context, "question": question})
