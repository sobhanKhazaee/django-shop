from django import template
from jalali_date import date2jalali

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
        value = int(value)
        formatted = f"{value:,}".replace(",", "٬")  
        return english_to_persian(formatted)
    except (ValueError, TypeError):
        return value
    
@register.filter
def show_jalali_date(value):
    value = date2jalali(value)
    value = value.replace("")