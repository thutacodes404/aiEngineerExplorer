from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
template="Explain this concept simply and concisely{concept}"

prompt_template=PromptTemplate.from_template(
    template=template
)

prompt = prompt_template.invoke({'concept':'Prompting LLMs'})
print(prompt)


llm=HuggingFacePipeline.from_model_id(
    model_id='meta-llama/Llama-3.2-3B-Instruct',
    task='text-generation'
)

llm_chain=prompt_template | llm

concept='Prompting LLMs'

print(llm_chain.invoke({'concept':concept}))