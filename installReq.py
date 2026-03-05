import subprocess

packages = [
    "langchain",
    "langchain_community",
    "langchain_huggingface",
    "faiss-cpu",
    "langchain-text-splitters",
    "pypdf",
    "sentence-transformers",
    "dotenv"
]

for package in packages:
    subprocess.run(["pip3", "install", package])