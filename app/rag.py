from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vector_db = Chroma(
    persist_directory="data/chroma_db",
    embedding_function=embeddings
)


def retrieve(query: str, k: int = 5):
    results = vector_db.similarity_search(query, k=k)

    assessments = []

    for doc in results:
        assessments.append({
            "title": doc.metadata.get("title"),
            "url": doc.metadata.get("url"),
            "content": doc.page_content[:500]   
        })

    return assessments
def retrieve_by_name(name: str):
    results = vector_db.similarity_search(name, k=1)

    if results:
        return results[0]

    return None

if __name__ == "__main__":

    query = "Java developer with leadership skills"

    results = retrieve(query)

    for i, r in enumerate(results, 1):
        print("=" * 60)
        print(f"{i}. {r['title']}")
        print(r["url"])
        print(r["content"])