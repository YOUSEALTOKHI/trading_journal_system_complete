# -*- coding: utf-8 -*-
"""
إدارة قاعدة البيانات والجلسات
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

# إنشاء محرك قاعدة البيانات
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
    echo=False
)

# إنشاء فئة الجلسة
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# الأساس للنماذج
Base = declarative_base()

def get_db():
    """الحصول على جلسة قاعدة البيانات"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """إنشاء جميع الجداول"""
    Base.metadata.create_all(bind=engine)

def get_db_session():
    """الحصول على جلسة مباشرة"""
    return SessionLocal()
