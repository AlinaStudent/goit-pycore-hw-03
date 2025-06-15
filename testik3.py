import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, окрім цифр і плюса
    cleaned = re.sub(r'[^\d+]', '', phone_number.strip())

    # Якщо номер починається з '+', перевіряємо, чи далі 380 (залишаємо як є)
    if cleaned.startswith('+'):
        if cleaned.startswith('+380'):
            return cleaned
        else:
            # Якщо починається з іншого коду — просто очищений номер
            return cleaned

    # Якщо починається з '380' — додаємо '+'
    if cleaned.startswith('380'):
        return f'+{cleaned}'

    # Якщо номер без міжнародного коду — додаємо '+38'
    return f'+38{cleaned}'