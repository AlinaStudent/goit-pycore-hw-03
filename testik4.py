from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    upcoming = []

    for user in users:
        # Перетворюємо дату народження на об'єкт дати
        birthday_full = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_full.replace(year=today.year)

        # Якщо день народження вже був цьогоріч, перевіряємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Чи день народження входить у наступні 7 днів?
        if today <= birthday_this_year <= end_date:
            congrats_date = birthday_this_year

            # Якщо день привітання припадає на вихідний – переносимо на понеділок
            if congrats_date.weekday() == 5:  # субота
                congrats_date += timedelta(days=2)
            elif congrats_date.weekday() == 6:  # неділя
                congrats_date += timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congrats_date.strftime("%Y.%m.%d")
            })

    return upcoming