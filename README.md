# RAG System

## Description
This is a simple RAG system that allows users to create, read, update and delete RAG statuses for a project. The system is built using Haystack, FastAPI.

## Installation

### Requirements
- Python 3.12
- Poetry

### Steps
1. Clone the repository
2. Run `poetry install` to install the dependencies
3. Run `poetry run uvicorn API.main:app --reload` to start the server
3. Run `poetry run python Rag/app.py` to start the RAG system for training
4. Visit `http://0.0.0.0:8000/docs` to view the API documentation

## API Endpoints
- POST `/query/` - Get query results

## TODO
- [ ] Complete RAG CRUD operations
- [ ] Add more training data
- [ ] Abstract the RAG model
- [ ] Add tests
