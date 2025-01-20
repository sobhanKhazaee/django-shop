from django import template

register = template.Library()



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
    except (ValueError, TypeError):
        return value  # اگر مقدار ورودی عدد نباشد، بدون تغییر بازگردانده می‌شود
