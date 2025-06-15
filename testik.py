from datetime import datetime

def get_days_from_today(date_str):
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta_days = (today - input_date).days
        return delta_days
    except ValueError:
        return "Помилка: неправильний формат дати. Використовуйте 'YYYY-MM-DD'."

# Тестуємо функцію
print(get_days_from_today("2025-06-14"))  # Приклад для майбутньої дати
print(get_days_from_today("2020-10-09"))  # Приклад для минулої дати
print(get_days_from_today("10-09-2025"))  # Приклад неправильної дати