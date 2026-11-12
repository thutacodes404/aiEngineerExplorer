from langchain_huggingface import HuggingFacePipeline

llm=HuggingFacePipeline.from_model_id(
    model_id="meta-llama/Llama-3.2-3B-Instruct",
    task='text-generation',
    pipeline_kwargs={'max_new_tokens':100}
)

answer=llm.invoke("What is Hugging Face")
print(answer)