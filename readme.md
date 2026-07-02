# SHL Conversational Assessment Recommender

## Features

- Web scraper for SHL assessments
- ChromaDB vector search
- HuggingFace embeddings
- Gemini 2.5 Flash
- FastAPI
- Conversational refinement
- Assessment comparison
- Out-of-scope detection

## Run

pip install -r requirements.txt

python app/scraper.py

python app/build_vector_db.py

uvicorn app.main:app --reload