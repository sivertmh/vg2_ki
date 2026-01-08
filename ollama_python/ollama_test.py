from ollama import chat

resp = chat(
	model="llama3.2:1b",
	messages=[{"role": "user", "content": "Forklar kort hva train/test-splitt er."}],
)

print(resp["message"]["content"])
