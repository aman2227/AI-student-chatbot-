from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()
df = pd.read_excel("Fee Management.xlsx")

hfllm = HuggingFaceEndpoint(
    repo_id = "MiniMaxAI/MiniMax-M2.7",
    task = "text-generation",
)

model = ChatHuggingFace(llm = hfllm)

text_data = df.to_string(index=False)
response = model.invoke(f"{text_data}\n What is the Balance of Alice Kumar.")

print(response.content)