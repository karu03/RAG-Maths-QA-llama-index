# RAG-Maths-QA-llama-index
This repository contains a RAG Model. The model takes a text  question as input and generates the step-by-step solution and final answer by leveraging the capabilities of Claude, HaiKu, and llama-index.


Sure, here's a README file for the provided code:
Math Question Answering with Claude, HaiKu, and llama-index
This repository contains code for building a math question answering system using Claude (a large language model from Anthropic),
HaiKu (an open-source toolkit for building neural retrievers), and llama-index (a library for generating embeddings and indices over text data).
Overview
The system works as follows:

A knowledge base of math problem solutions is loaded and indexed using llama-index.

When a user asks a math question, HaiKu is used to retrieve the most relevant context from the indexed knowledge base.

The question and retrieved context are passed to Claude, which generates a step-by-step solution and final answer.

The system presents the generated solution to the user through a Gradio chat interface.

