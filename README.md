# News Data Engineering Pipeline

End-to-end data engineering project — built during industrial training at IIUC.

## What It Does
Scrapes live news data → stores in a structured MySQL database →
serves via FastAPI REST API → delivers through an interactive Streamlit dashboard.

## Pipeline Architecture
## Tech Stack
- **Ingestion:** Python (requests / BeautifulSoup), web scraping
- **Storage:** MySQL — structured schema, full DB implementation
- **API Layer:** FastAPI — REST endpoints serving pipeline output
- **Delivery:** Streamlit — interactive data exploration app
- **Extras:** LangChain + Gemini chatbot module

## Key Modules
| Folder | Purpose |
|--------|---------|
| `DB implement with scrapper` | Database schema + scraper integration |
| `Final Work _Scrapper_with_API` | Production scraper with FastAPI layer |
| `my_news` | Core news data pipeline |
| `Chatbot` | LangChain + Gemini conversational layer |

## Setup
```bash
pip install -r requirements.txt
```
See individual folders for run instructions.
