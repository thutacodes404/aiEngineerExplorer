import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


# =====================================
# 1. Embedding Model
# =====================================

embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


# =====================================
# 2. Connect to ChromaDB
# =====================================

client = chromadb.PersistentClient(
    path="./storage/chroma"
)


# =====================================
# 3. Create / Get Collection
# =====================================

collection = client.create_collection(
    name="recommendation",
    embedding_function=embedding_function
)


# =====================================
# 4. Documents
# =====================================

documents = [

    # -------- AI / Machine Learning --------

    "Artificial intelligence enables machines to perform tasks that normally require human intelligence.",

    "Machine learning is a branch of artificial intelligence where computers learn patterns from data.",

    "Supervised learning trains machine learning models using labeled datasets.",

    "Unsupervised learning discovers hidden patterns in data without labeled outputs.",

    "Reinforcement learning trains agents through rewards and penalties.",

    "Deep learning uses neural networks with multiple layers to learn complex patterns.",

    "Neural networks are computational models inspired by the structure of the human brain.",

    "Classification predicts discrete categories such as spam or not spam.",

    "Regression predicts continuous numerical values such as house prices.",

    "Clustering groups similar data points together without predefined labels.",

    "K-Means is a popular unsupervised learning algorithm used for clustering.",

    "Random Forest combines multiple decision trees to improve prediction accuracy.",

    "Support Vector Machines find an optimal boundary between different classes.",

    "Gradient boosting builds multiple weak learners sequentially to create a strong predictive model.",

    "Feature engineering transforms raw data into useful features for machine learning models.",

    "Overfitting happens when a model performs well on training data but poorly on unseen data.",

    "Cross-validation evaluates machine learning models using multiple train and validation splits.",

    "Precision measures how many predicted positive examples are actually positive.",

    "Recall measures how many actual positive examples were correctly identified.",

    "The F1 score combines precision and recall into a single evaluation metric.",


    # -------- Python --------

    "Python is one of the most popular programming languages for artificial intelligence and data science.",

    "Python lists are ordered and mutable collections of values.",

    "Python dictionaries store information using key-value pairs.",

    "Python functions allow developers to organize reusable pieces of code.",

    "NumPy provides efficient numerical computation using multidimensional arrays.",

    "Pandas is commonly used for data manipulation and data analysis in Python.",

    "Matplotlib is a Python library used for creating data visualizations.",

    "Scikit-learn provides machine learning algorithms and preprocessing tools.",

    "PyTorch is a deep learning framework commonly used for research and production.",

    "TensorFlow is an open-source machine learning framework developed for building neural networks.",


    # -------- NLP --------

    "Natural language processing allows computers to understand and process human language.",

    "Tokenization divides text into smaller units called tokens.",

    "Text embeddings represent words or sentences as numerical vectors.",

    "Semantic similarity measures how similar two pieces of text are based on their meanings.",

    "Transformers use attention mechanisms to process relationships between tokens.",

    "BERT is a transformer model designed to understand bidirectional context in text.",

    "Large language models are trained on massive amounts of text to understand and generate language.",

    "Prompt engineering involves designing effective instructions for large language models.",

    "Named entity recognition identifies entities such as people, organizations, and locations in text.",

    "Sentiment analysis determines whether text expresses positive, negative, or neutral sentiment.",


    # -------- RAG --------

    "RAG stands for Retrieval-Augmented Generation.",

    "Retrieval-Augmented Generation combines information retrieval with large language models.",

    "A RAG system retrieves relevant information before asking the language model to generate an answer.",

    "RAG systems can reduce hallucinations by providing relevant external knowledge to language models.",

    "Documents are usually divided into smaller chunks before being stored in a vector database.",

    "Each document chunk can be converted into an embedding before being stored.",

    "The user's question is converted into an embedding during the retrieval process.",

    "Similarity search compares the query embedding with stored document embeddings.",

    "The most relevant retrieved documents are added to the prompt as context.",

    "The language model generates an answer using the retrieved context and user question.",

    "Metadata can be stored with document chunks to identify their original source.",

    "Chunk size and chunk overlap can significantly affect RAG retrieval quality.",

    "Hybrid search combines semantic vector search with traditional keyword search.",

    "Reranking can improve RAG quality by reordering retrieved documents according to relevance.",


    # -------- Vector Databases --------

    "A vector database stores and searches high-dimensional numerical vectors.",

    "ChromaDB is an open-source vector database commonly used for AI applications.",

    "Vector databases enable semantic search based on meaning rather than exact keyword matching.",

    "Cosine similarity measures the angle between two vectors to estimate their similarity.",

    "Euclidean distance measures the straight-line distance between vectors.",

    "FAISS is a library developed for efficient similarity search over dense vectors.",

    "Pinecone provides managed vector database infrastructure for AI applications.",

    "Milvus is an open-source vector database designed for large-scale similarity search.",

    "Qdrant is a vector database designed for similarity search and AI applications.",


    # -------- Embeddings --------

    "An embedding is a numerical vector representation of data.",

    "Text embeddings capture semantic information about words, sentences, and documents.",

    "Similar sentences usually have embeddings located close together in vector space.",

    "Sentence Transformers can generate embeddings for sentences and documents.",

    "The all-MiniLM-L6-v2 model is a lightweight Sentence Transformer model.",

    "Embedding models are different from large language models used for text generation.",

    "The same embedding model should generally be used when indexing documents and embedding search queries.",


    # -------- LLM --------

    "Large language models predict and generate text based on patterns learned from large datasets.",

    "LLMs can perform tasks such as question answering, summarization, translation, and text generation.",

    "A context window determines how much information a language model can process at one time.",

    "Temperature controls the randomness of language model generation.",

    "Lower temperature values generally produce more deterministic responses.",

    "Hallucination occurs when a language model generates incorrect or unsupported information.",

    "System prompts can define instructions and behavior for language models.",


    # -------- Groq --------

    "Groq provides high-speed inference infrastructure for large language models.",

    "The Groq API can be used to send prompts to supported large language models.",

    "Groq provides an OpenAI-compatible API interface for many language model operations.",

    "Groq can be used as the generation component of a Retrieval-Augmented Generation system.",


    # -------- Databases --------

    "A database is a structured system for storing and retrieving information.",

    "SQL is a language used for querying relational databases.",

    "SQLite is a lightweight relational database stored in a single file.",

    "PostgreSQL is an open-source relational database management system.",

    "MongoDB is a NoSQL database that stores information using document-like structures.",

    "Relational databases organize information into tables containing rows and columns.",

    "Primary keys uniquely identify records in relational database tables.",


    # -------- APIs --------

    "An API allows different software applications to communicate with each other.",

    "REST APIs commonly communicate over HTTP using methods such as GET, POST, PUT, and DELETE.",

    "JSON is a common data format used for exchanging information between APIs.",

    "API keys are commonly used to authenticate requests to external services.",

    "Environment variables can be used to keep API keys outside application source code.",

    "FastAPI is a Python framework for building high-performance web APIs.",


    # -------- Cloud --------

    "Cloud computing provides computing resources such as servers, databases, and storage over the internet.",

    "Amazon Web Services is a major cloud computing platform.",

    "Amazon S3 provides object storage for files and datasets.",

    "AWS Lambda allows developers to execute code without managing servers.",

    "Amazon EC2 provides virtual machines in the AWS cloud.",

    "Cloud databases allow applications to store and access information remotely.",


    # -------- Data Engineering --------

    "Data engineering involves collecting, transforming, storing, and managing data.",

    "ETL stands for Extract, Transform, and Load.",

    "A data pipeline moves and transforms information between different systems.",

    "Apache Spark is a distributed processing engine designed for large datasets.",

    "PySpark provides a Python interface for Apache Spark.",

    "Databricks provides a platform for data engineering, analytics, and machine learning.",

    "Delta Lake adds reliability and transaction support to data lake architectures.",

    "The bronze layer commonly stores raw data in a medallion architecture.",

    "The silver layer commonly contains cleaned and transformed data.",

    "The gold layer commonly contains business-ready aggregated data.",


    # -------- Software Engineering --------

    "Git is a distributed version control system used to track source code changes.",

    "GitHub provides cloud hosting and collaboration tools for Git repositories.",

    "Docker packages applications and their dependencies into containers.",

    "Environment variables are useful for storing configuration values and secrets.",

    "Virtual environments isolate Python dependencies between different projects.",

    "Unit tests verify that individual components of an application behave correctly.",

    "Logging helps developers monitor application behavior and diagnose problems."
]


# =====================================
# 5. Generate IDs automatically
# =====================================

ids = [
    f"doc_{i}"
    for i in range(1, len(documents) + 1)
]


# =====================================
# 6. Store in ChromaDB
# =====================================

collection.upsert(
    ids=ids,
    documents=documents
)


# =====================================
# 7. Check Database
# =====================================

print("Data stored successfully!")
print("Total documents:", collection.count())