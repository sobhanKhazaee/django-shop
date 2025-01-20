from jalali_date import date2jalali
from django.http import HttpResponse


PERSIAN_DIGITS = '۰۱۲۳۴۵۶۷۸۹'

def english_to_persian(value):
    return ''.join(PERSIAN_DIGITS[int(char)] if char.isdigit() else char for char in str(value))

def show_jalali_date(value):
    date = date2jalali(value).strftime(' %Y/%m/%d ')
    return english_to_persian(date)

def get_client_ip(request:HttpResponse):
    X_FORWARDED_FOR = request.META.get("HTTP_X_FORWARDED_FOR")
    if X_FORWARDED_FOR:
        ip = X_FORWARDED_FOR.split(",")[0]
    else:
        ip =     
        
        
