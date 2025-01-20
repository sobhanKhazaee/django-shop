from django import template

register = template.Library()

def intcomma_fa(value):
    """
    تبدیل اعداد به فرمت هزارگان فارسی.
    """
    try:
        # اطمینان از عدد بودن مقدار
        value = int(value)
        # فرمت عدد به هزارگان
        formatted = f"{value:,}".replace(",", "٬")  # جایگزینی کاما با جداکننده فارسی
        # تبدیل اعداد انگلیسی به فارسی
        return english_to_persian(formatted)
    except (ValueError, TypeError):
        return value  # اگر مقدار ورودی عدد نباشد، بدون تغییر بازگردانده می‌شود
