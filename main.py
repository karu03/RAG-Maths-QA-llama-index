from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core import Settings

documents = SimpleDirectoryReader("data", encoding="utf8, latin-1").load_data()
print(documents[:5])

from llama_index.llms.anthropic import Anthropic

from llama_index.embeddings.fastembed import FastEmbedEmbedding
api="api key "
embed_model = FastEmbedEmbedding(model_name="BAAI/bge-small-en-v1.5")
Settings.embed_model = embed_model
Settings.chunk_size = 512
llm = Anthropic(temperature=0.0, model='claude-3-haiku-20240307', api_key=api)
Settings.llm=llm
Settings.chunk_size = 512 


print("model \n")
from llama_index.core import PromptTemplate


system_prompt = """
               You are a genius mathematical AI model with enormous maths knowledge. you job is to help other students.
               your goals is to answer the user query's with the best explaination.
               you get the query , breakdown the context , solve the context.  and refine it in an easy explainable way.
               if you failed to do your job. you are nothing but a trash can
"""

# This will wrap the default prompts that are internal to llama-index
query_wrapper_prompt = PromptTemplate("<|USER|>{query_str}<|ASSISTANT|>")



# Configure Settings

 # Adjust chunk size as needed



index = VectorStoreIndex.from_documents(documents)
print(index)

query_engine = index.as_query_engine()
import time

#res = query_engine.query("ask me 10 question")

def predict(input, history):
    start_time = time.time()
    response = query_engine.query(input)
    end_time = time.time()
    query_time = end_time - start_time
    print(f"Query time: {query_time:.4f} seconds")
    
    return str(response)


import gradio as gr

gr.ChatInterface(predict).launch(share=True)
start_time = time.time()
end_time = time.time()
runtime = end_time - start_time
print(f"Code runtime: {runtime:.4f} seconds")