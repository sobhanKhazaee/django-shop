        // به‌روزرسانی خروجی مقدار قیمت در هنگام تغییر اسلایدر
        function updatePriceOutput(value) {
            document.getElementById('price_output').textContent = 
                'تا ' + new Intl.NumberFormat('fa-IR').format(value) + ' هزار تومان';
        }