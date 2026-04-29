"""Configuration Management Module"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    # Flask/FastAPI
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-in-production')

    # Database
    DATABASE_PATH = os.getenv('DATABASE_PATH', './data/trading_journal.db')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'

    # Data Storage
    DATA_DIR = './data'
    UPLOADS_DIR = './data/uploads'
    CHARTS_DIR = './data/charts'
    REPORTS_DIR = './data/reports'

    # AI Configuration
    AI_PROVIDER = os.getenv('AI_PROVIDER', 'openai')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
    GOOGLE_GENAI_API_KEY = os.getenv('GOOGLE_GENAI_API_KEY', '')

    # API Configuration
    API_HOST = os.getenv('API_HOST', '127.0.0.1')
    API_PORT = int(os.getenv('API_PORT', 8000))

    # Van Tharp Principles
    VAN_THARP_PRINCIPLES = [
        "Have a positive expectancy",
        "Have a written trading plan",
        "Record all trades",
        "Keep a trading journal",
        "Have a positive risk/reward ratio",
        "Use position sizing",
        "Follow your system",
        "Let profits run and cut losses short",
        "Diversify trades",
        "Never risk more than you can afford to lose"
    ]
