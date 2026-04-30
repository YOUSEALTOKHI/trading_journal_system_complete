# -*- coding: utf-8 -*-
"""
إعدادات التطبيق الرئيسية
"""

import os
from dotenv import load_dotenv

load_dotenv()

# إعدادات قاعدة البيانات
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./trading_journal.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# مفاتيح API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GOOGLE_SHEETS_API_KEY = os.getenv("GOOGLE_SHEETS_API_KEY", "")
SHEETS_SPREADSHEET_ID = os.getenv("SHEETS_SPREADSHEET_ID", "")

# إعدادات التطبيق
APP_NAME = "نظام إدارة يوميات التداول"
APP_VERSION = "1.0.0"

# العملات المدعومة
SUPPORTED_SYMBOLS = [
    "EURUSD", "GBPUSD", "USDJPY", "USDCAD", "USDCHF",
    "AUDUSD", "NZDUSD", "EURGBP", "EURJPY", "GBPJPY",
    "GOLD", "OIL", "S&P500", "DAX", "FTSE"
]

# أنواع الصفقات
TRADE_TYPES = ["BUY", "SELL"]

# الحالات النفسية
PSYCHOLOGICAL_STATES = [
    "مريح وهادئ",
    "قليل القلق",
    "قلق جداً",
    "غاضب",
    "متحمس بشدة",
    "متردد",
    "مشتت التركيز",
    "واثق جداً"
]

# أسباب الدخول
ENTRY_REASONS = [
    "إشارة فنية",
    "مستوى دعم/مقاومة",
    "خبر اقتصادي",
    "نمط شموعي",
    "تقارب متحرك",
    "تباعد",
    "اختراق",
    "ارتداد"
]

# مبادئ Van Tharp
VAN_THARP_PRINCIPLES = [
    "فهم نظام التداول الخاص بي",
    "إدارة المخاطر والحجم المناسب",
    "الالتزام الكامل بقواعد النظام",
    "مراقبة الحالة النفسية والعواطف",
    "الانضباط والصبر في التنفيذ",
    "تقبل الخسائر كجزء من التداول",
    "المحافظة على رأس المال",
    "التعلم المستمر من الأخطاء",
    "التقييم الذاتي المنتظم",
    "التطور والتحسين المستمر"
]
