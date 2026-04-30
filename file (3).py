# -*- coding: utf-8 -*-
"""
بيانات تجريبية للعرض التوضيحي
"""

import pandas as pd
from datetime import datetime, timedelta
from app.config import SUPPORTED_SYMBOLS

def generate_mock_trades(days=30):
    """إنشاء بيانات صفقات تجريبية"""
    dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
    trades_list = []
    
    for i, date in enumerate(dates):
        num_trades = (i % 5) + 1
        for j in range(num_trades):
            trade_type = "BUY" if (i + j) % 2 == 0 else "SELL"
            profit = (50 if j % 2 == 0 else -30) + (i * 5)
            
            trades_list.append({
                'ticket': f"{i*10 + j + 1000}",
                'symbol': SUPPORTED_SYMBOLS[i % len(SUPPORTED_SYMBOLS)],
                'trade_type': trade_type,
                'open_time': date + timedelta(hours=j),
                'close_time': date + timedelta(hours=j+2),
                'size': 1.0 + (j * 0.5),
                'open_price': 1.0850 + (j * 0.0010),
                'close_price': 1.0880 + (j * 0.0010),
                'profit': profit,
                'profit_percent': (profit / (1.0850 * 100000 * (1.0 + j * 0.5))) * 100,
                'entry_reason': ['إشارة فنية', 'مستوى دعم', 'خبر اقتصادي'][i % 3],
                'trading_notes': f'صفقة رقم {i*10 + j + 1}',
                'psychological_state': ['مريح وهادئ', 'قليل القلق', 'متحمس'][j % 3],
                'thoughts_at_entry': 'تحليل جيد للسوق'
            })
    
    return pd.DataFrame(trades_list)


def get_sample_daily_stats():
    """إحصائيات يومية عينة"""
    return {
        'date': datetime.now().date(),
        'total_trades': 5,
        'winning_trades': 3,
        'losing_trades': 2,
        'daily_profit': 150.50,
        'daily_pnl_percent': 2.5,
        'best_trade': 120.0,
        'worst_trade': -80.0,
        'win_rate': 60.0
    }


def get_sample_weekly_stats():
    """إحصائيات أسبوعية عينة"""
    return {
        'week_start': (datetime.now() - timedelta(days=7)).date(),
        'week_end': datetime.now().date(),
        'total_trades': 35,
        'winning_trades': 21,
        'losing_trades': 14,
        'weekly_profit': 850.75,
        'weekly_pnl_percent': 3.2,
        'best_trade': 250.0,
        'worst_trade': -150.0,
        'win_rate': 60.0,
        'avg_profit_per_trade': 24.31
    }


def get_sample_monthly_stats():
    """إحصائيات شهرية عينة"""
    return {
        'month': datetime.now().date().replace(day=1),
        'total_trades': 150,
        'winning_trades': 90,
        'losing_trades': 60,
        'monthly_profit': 3500.25,
        'monthly_pnl_percent': 5.8,
        'best_trade': 450.0,
        'worst_trade': -200.0,
        'win_rate': 60.0,
        'avg_profit_per_trade': 23.33,
        'best_symbol': 'EURUSD',
        'worst_symbol': 'USDJPY'
    }
