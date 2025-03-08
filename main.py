import ollama

result = ollama.embed(
    model="mxbai-embed-large",
    input="Llamas are members of the camelid family",
)

print(result.embeddings[0])
