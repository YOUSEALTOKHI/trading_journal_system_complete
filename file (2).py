# -*- coding: utf-8 -*-
"""
نماذج قاعدة البيانات - SQLAlchemy
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, JSON
from app.database import Base
from datetime import datetime

class Trade(Base):
    """نموذج الصفقة التجارية"""
    __tablename__ = "trades"
    
    id = Column(Integer, primary_key=True, index=True)
    ticket = Column(String, unique=True, index=True)
    symbol = Column(String, index=True)
    trade_type = Column(String)  # BUY أو SELL
    open_time = Column(DateTime, index=True)
    close_time = Column(DateTime)
    size = Column(Float)
    open_price = Column(Float)
    close_price = Column(Float)
    profit = Column(Float)
    profit_percent = Column(Float)
    entry_reason = Column(String)
    trading_notes = Column(Text)
    psychological_state = Column(String)
    thoughts_at_entry = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            "id": self.id,
            "ticket": self.ticket,
            "symbol": self.symbol,
            "trade_type": self.trade_type,
            "open_time": self.open_time.isoformat() if self.open_time else None,
            "close_time": self.close_time.isoformat() if self.close_time else None,
            "size": self.size,
            "open_price": self.open_price,
            "close_price": self.close_price,
            "profit": self.profit,
            "profit_percent": self.profit_percent,
        }


class DailyDebrief(Base):
    """نموذج الديلي دبريفنج"""
    __tablename__ = "daily_debriefs"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True, unique=True)
    total_trades = Column(Integer, default=0)
    winning_trades = Column(Integer, default=0)
    losing_trades = Column(Integer, default=0)
    daily_profit = Column(Float, default=0)
    daily_pnl_percent = Column(Float, default=0)
    error_analysis = Column(Text)
    psychological_insights = Column(Text)
    main_mistakes = Column(Text)
    improvement_areas = Column(Text)
    chart_images = Column(JSON, default={})
    van_tharp_checklist = Column(JSON, default={})
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class WeeklySummary(Base):
    """نموذج الملخص الأسبوعي"""
    __tablename__ = "weekly_summaries"
    
    id = Column(Integer, primary_key=True, index=True)
    week_start = Column(DateTime, index=True)
    week_end = Column(DateTime)
    total_trades = Column(Integer, default=0)
    winning_trades = Column(Integer, default=0)
    losing_trades = Column(Integer, default=0)
    win_rate = Column(Float, default=0)
    weekly_profit = Column(Float, default=0)
    weekly_pnl_percent = Column(Float, default=0)
    best_trade = Column(Float, default=0)
    worst_trade = Column(Float, default=0)
    avg_profit_per_trade = Column(Float, default=0)
    psychological_summary = Column(Text)
    emotional_patterns = Column(Text)
    weekly_performance_review = Column(Text)
    next_week_goals = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class MonthlySummary(Base):
    """نموذج الملخص الشهري"""
    __tablename__ = "monthly_summaries"
    
    id = Column(Integer, primary_key=True, index=True)
    month = Column(DateTime, index=True, unique=True)
    total_trades = Column(Integer, default=0)
    winning_trades = Column(Integer, default=0)
    losing_trades = Column(Integer, default=0)
    win_rate = Column(Float, default=0)
    monthly_profit = Column(Float, default=0)
    monthly_pnl_percent = Column(Float, default=0)
    best_trade = Column(Float, default=0)
    worst_trade = Column(Float, default=0)
    avg_profit_per_trade = Column(Float, default=0)
    best_symbol = Column(String)
    worst_symbol = Column(String)
    most_traded_symbol = Column(String)
    monthly_comprehensive_review = Column(Text)
    strengths = Column(Text)
    weaknesses = Column(Text)
    future_development_plans = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class FundamentalReport(Base):
    """نموذج التقرير الأساسي"""
    __tablename__ = "fundamental_reports"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    source = Column(String)
    source_url = Column(String, unique=True)
    original_content = Column(Text)
    summary = Column(Text)
    published_date = Column(DateTime)
    extracted_date = Column(DateTime, index=True, default=datetime.utcnow)
    language = Column(String, default="ar")
    keywords = Column(JSON, default=[])
    symbols_mentioned = Column(JSON, default=[])
    importance_level = Column(String)  # High, Medium, Low
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
