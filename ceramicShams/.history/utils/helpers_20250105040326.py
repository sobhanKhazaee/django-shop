from jalali_date import date2jalali

def show_jalali_date(value):
    date = date2jalali(value).strftime(' %Y/%m/%d ')
    return english_to_persian(date)
