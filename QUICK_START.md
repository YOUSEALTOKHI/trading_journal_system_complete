# 🚀 Quick Start Guide

## Installation

```bash
# 1. Clone repository
git clone https://github.com/yourusername/trading-journal-system.git
cd trading-journal-system

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your API keys (optional)
```

## Running

### Option 1: Streamlit (Recommended)
```bash
streamlit run app/streamlit_app.py
```
Access: http://localhost:8501

### Option 2: FastAPI
```bash
python app/main.py
```
Access: http://localhost:8000/docs

## Features

- ✅ Trade journal management
- ✅ MT4 statement import
- ✅ Daily/Weekly/Monthly analysis
- ✅ AI-powered report summarization
- ✅ Interactive dashboards

## Next Steps

1. Add your first trade
2. Configure AI API keys in .env
3. Explore Van Tharp principles
4. Review documentation in docs/

## Support

- GitHub Issues: Report bugs
- Documentation: See docs/ folder
- Examples: Check examples/ folder
