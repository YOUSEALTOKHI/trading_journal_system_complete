"""Database Models"""
from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Trade(Base):
    """Trading transaction model"""
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    trade_date = Column(DateTime, default=datetime.utcnow)
    symbol = Column(String(20), nullable=False)
    trade_type = Column(String(10), nullable=False)
    entry_price = Column(Float, nullable=False)
    exit_price = Column(Float)
    volume = Column(Float, nullable=False)
    profit_loss = Column(Float)
    trading_notes = Column(Text)
    entry_reason = Column(String(100))
    psychological_state = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

class DailyDebriefing(Base):
    """Daily debriefing"""
    __tablename__ = 'daily_debriefings'

    id = Column(Integer, primary_key=True)
    debriefing_date = Column(DateTime, default=datetime.utcnow)
    error_analysis = Column(Text)
    chart_images = Column(JSON)
    van_tharp_checklist = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

class WeeklySummary(Base):
    """Weekly summary"""
    __tablename__ = 'weekly_summaries'

    id = Column(Integer, primary_key=True)
    week_start = Column(DateTime)
    week_end = Column(DateTime)
    total_trades = Column(Integer)
    total_profit_loss = Column(Float)
    win_rate = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class MonthlySummary(Base):
    """Monthly summary"""
    __tablename__ = 'monthly_summaries'

    id = Column(Integer, primary_key=True)
    month_start = Column(DateTime)
    month_end = Column(DateTime)
    total_trades = Column(Integer)
    total_profit_loss = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class FundamentalReport(Base):
    """Fundamental analysis reports"""
    __tablename__ = 'fundamental_reports'

    id = Column(Integer, primary_key=True)
    original_url = Column(String(500))
    original_title = Column(String(255))
    summary = Column(Text)
    key_points = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db(database_url):
    """Initialize database"""
    engine = create_engine(database_url, echo=False)
    Base.metadata.create_all(engine)
    return engine

def get_session(database_url):
    """Get SQLAlchemy session"""
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()
