from django import template

register = template.Library()

PERSIAN_DIGITS = '۰۱۲۳۴۵۶۷۸۹'

def english_to_persian(value):
    return ''.join(PERSIAN_DIGITS[int(char)] if char.isdigit() else char for char in str(value))

@register.filter
def intcomma_fa(value):
    """
    تبدیل اعداد به فرمت هزارگان فارسی.
    """
    try:
        # اطمینان از عدد بودن مقدار 
        value = int(value)
        # فرمت عدد به هزارگان
        return f"{value:,}".replace(",", "٬")  # جایگزینی کاما با جداکننده فارسی
      return english_to_persian(formatted)   
    except (ValueError, TypeError):
        return value  # اگر مقدار ورودی عدد نباشد، بدون تغییر بازگردانده می‌شود
