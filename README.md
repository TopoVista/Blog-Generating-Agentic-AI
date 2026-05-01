# Blog Generating Agentic AI

`BlogAgentic` is a Python-based agentic AI project that generates blog titles and full blog content from a user-provided topic. It combines `FastAPI` for the API layer, `LangGraph` for workflow orchestration, and `Groq` via `LangChain` for LLM-powered generation.

The current workflow is intentionally simple and modular: a topic enters the system, the graph generates an SEO-friendly title, then generates the blog body, and finally returns the structured result as JSON.

## Features

- Topic-based blog generation through a FastAPI endpoint
- LangGraph workflow with separate title and content generation nodes
- Modular project structure for nodes, state, graphs, and LLM setup
- Groq LLM integration using `langchain-groq`
- JSON API response suitable for UI, automation, or future extensions

## Tech Stack

- Python
- FastAPI
- Uvicorn
- LangChain
- LangGraph
- Groq LLM
- Pydantic

## Project Structure

```text
BlogAgentic/
|-- main.py
|-- pyproject.toml
|-- requirements.txt
|-- uv.lock
|-- src/
|   |-- graphs/
|   |   |-- graph_builder.py
|   |-- llms/
|   |   |-- groqllm.py
|   |-- nodes/
|   |   |-- blog_node.py
|   |-- states/
|   |   |-- blogstate.py
```

## How It Works

### 1. API Layer

The FastAPI app exposes a `POST /blogs` endpoint in [main.py](/c:/Users/KIIT0001/Desktop/AI%20AGENT%20COURSE%202%20KRISH%20NAIK/section20/BlogAgentic/main.py).  
It accepts a JSON payload containing a `topic`.

### 2. LLM Initialization

The Groq client is created in [src/llms/groqllm.py](/c:/Users/KIIT0001/Desktop/AI%20AGENT%20COURSE%202%20KRISH%20NAIK/section20/BlogAgentic/src/llms/groqllm.py) using `ChatGroq`.

### 3. Graph Construction

The generation flow is defined in [src/graphs/graph_builder.py](/c:/Users/KIIT0001/Desktop/AI%20AGENT%20COURSE%202%20KRISH%20NAIK/section20/BlogAgentic/src/graphs/graph_builder.py).

Current graph flow:

```text
START
  -> title_creation
  -> content_generation
  -> END
```

### 4. Blog Generation Nodes

[src/nodes/blog_node.py](/c:/Users/KIIT0001/Desktop/AI%20AGENT%20COURSE%202%20KRISH%20NAIK/section20/BlogAgentic/src/nodes/blog_node.py) contains the node logic:

- `title_creation`: Generates a creative, SEO-friendly blog title
- `content_generation`: Generates detailed blog content for the same topic

### 5. Shared State

[src/states/blogstate.py](/c:/Users/KIIT0001/Desktop/AI%20AGENT%20COURSE%202%20KRISH%20NAIK/section20/BlogAgentic/src/states/blogstate.py) defines the typed workflow state used across the graph.

## API Endpoint

### `POST /blogs`

Generate a blog from a topic.

#### Request Body

```json
{
  "topic": "Artificial Intelligence in Healthcare"
}
```

#### Example Response

```json
{
  "data": {
    "topic": "Artificial Intelligence in Healthcare",
    "blog": {
      "title": "How Artificial Intelligence Is Transforming Healthcare",
      "content": "..."
    }
  }
}
```

## Setup Instructions

### Prerequisites

- Python 3.13 or later
- A Groq API key
- Optional: a LangSmith API key for tracing/observability

### 1. Clone the Repository

```bash
git clone https://github.com/TopoVista/Blog-Generating-Agentic-AI.git
cd Blog-Generating-Agentic-AI
```

### 2. Create and Activate a Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Using `pip`:

```bash
pip install -r requirements.txt
```

Or using `uv`:

```bash
uv sync
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
```

Notes:

- `GROQ_API_KEY` is required for generation.
- `LANGCHAIN_API_KEY` is used by the current code to populate `LANGSMITH_API_KEY`.

## Running the Application

Start the FastAPI server with Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API docs:

```text
http://127.0.0.1:8000/docs
```

## Testing the API

You can test the endpoint with `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/blogs" \
  -H "Content-Type: application/json" \
  -d "{\"topic\":\"Artificial Intelligence in Healthcare\"}"
```

Or with PowerShell:

```powershell
Invoke-RestMethod -Method Post `
  -Uri "http://127.0.0.1:8000/blogs" `
  -ContentType "application/json" `
  -Body '{"topic":"Artificial Intelligence in Healthcare"}'
```

## Architecture Notes

- The project uses a graph-based workflow rather than a single direct LLM call.
- Each node handles one responsibility, which makes the system easier to extend.
- The state object allows multiple graph steps to share structured data.
- This design can be expanded to support research, outlining, editing, tone control, multilingual output, or publishing workflows.

## Potential Enhancements

- Add input validation with request models
- Add error handling for missing topic or failed LLM responses
- Support multiple use cases beyond topic-based generation
- Add unit tests and integration tests
- Add logging and tracing improvements
- Add blog outline, summary, SEO keywords, and metadata generation
- Add persistence or database support
- Add frontend integration for interactive blog generation

## License

This project is currently unlicensed. Add a license if you plan to share or distribute it publicly.
