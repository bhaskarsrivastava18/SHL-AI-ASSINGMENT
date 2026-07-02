from app.rag import retrieve
from app.llm import generate_reply

query = "Hiring a Java developer with leadership skills."

docs = retrieve(query)

answer = generate_reply(query, docs)

print(answer)