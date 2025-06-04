def normalize_persian(text):
    """
    نرمال‌سازی متن فارسی برای مقایسه دقیق‌تر (حذف فاصله‌های اضافی و ی/ک استاندارد)
    """
    return text.strip().replace('ي', 'ی').replace('ك', 'ک').replace('‌', ' ').lower()
