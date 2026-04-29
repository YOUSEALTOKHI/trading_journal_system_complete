# 📊 Trading Journal & Fundamental Analysis System

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

نظام شامل لإدارة يوميات التداول وتحليل التقارير الأساسية مع دعم كامل للذكاء الاصطناعي

A comprehensive system for managing trading journals and fundamental analysis reports with full AI support.

## 🌟 Features / المميزات

### Trading Journal (يوميات التداول)
- ✅ Import MT4 statements with OCR
- ✅ Manual trade entry with psychological tracking
- ✅ Daily debriefing and error analysis
- ✅ Van Tharp's 10 principles evaluation
- ✅ Weekly and monthly automated summaries

### Fundamental Analysis (التحليل الأساسي)
- ✅ Web scraping from Forex Factory, Investing.com, Bloomberg
- ✅ AI-powered summarization (OpenAI, Claude, Gemini)
- ✅ Bilingual support (English & Arabic)
- ✅ Key points extraction

### Dashboards (لوحات المعلومات)
- ✅ Interactive daily dashboard
- ✅ Weekly performance review
- ✅ Monthly comprehensive analysis
- ✅ Real-time metrics and charts

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/trading-journal-system.git
cd trading-journal-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

### Running

```bash
# Option 1: Streamlit Interface (Recommended)
streamlit run app/streamlit_app.py

# Option 2: FastAPI Backend
python app/main.py
```

### Access
- **Streamlit**: http://localhost:8501
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 📖 Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [User Guide](docs/USER_GUIDE.md)
- [API Reference](docs/API.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## 🏗️ Architecture

```
trading_journal_system/
├── app/                    # Application code
│   ├── main.py            # FastAPI backend
│   ├── streamlit_app.py   # Streamlit frontend
│   └── scheduler.py       # Task scheduling
├── config/                # Configuration
├── database/              # Database models
├── data_processing/       # Data analysis
├── ocr_vision/           # OCR/Vision extraction
├── ai_plugins/           # AI model integrations
├── web_scraping/         # Web scraping modules
└── dashboards/           # Dashboard components
```

## 🤖 AI Integration

Supports multiple AI providers:
- **OpenAI** (GPT-4/mini)
- **Anthropic** (Claude)
- **Google** (Gemini)

Switch between providers in `.env`:
```env
AI_PROVIDER=openai  # or claude or gemini
OPENAI_API_KEY=your-key-here
```

## 📊 Database Schema

- **Trade**: Trading transactions
- **DailyDebriefing**: Daily analysis
- **WeeklySummary**: Weekly performance
- **MonthlySummary**: Monthly review
- **FundamentalReport**: Scraped reports

## 🔒 Security

- Environment variable management
- API key isolation
- Input validation
- SQL injection prevention
- CORS configuration

## 📈 Performance Metrics

- Win Rate
- Profit Factor
- Max Drawdown
- Risk/Reward Ratio
- Consecutive Wins/Losses

## 🌐 Deployment

### Streamlit Cloud (Free)
1. Push to GitHub
2. Go to https://streamlit.io/cloud
3. Connect repository
4. Deploy!

### Railway / Render / Heroku
See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions.

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check documentation in `docs/`

## ✨ Acknowledgments

- Van Tharp for trading principles
- FastAPI and Streamlit communities
- All contributors

---

**Version**: 1.0.0  
**Status**: Production Ready ✅  
**Last Updated**: 2026-04-29
