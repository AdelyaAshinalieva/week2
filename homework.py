import datetime as dt
class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        day_stats = []
        for record in self.records:
            if record.date == self.today:
                day_stats.append(record.amount)
        return sum(day_stats)

    def get_week_stats(self):
        week_stats = []
        for record in self.records:
            if self.week_ago <= record.date <= self.today:
                week_stats.append(record.amount)
        return sum(week_stats)

    def remained(self):
        remained = self.limit - self.get_today_stats()
        return remained

class CaloriesCalculator (Calculator):
    def get_calories_remained(self):
        N = self.remained()
        if N > 0:
            message = (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                       f'калорийностью не более {N} кКал')
        else:
            message = 'Хватит есть!'
        return message

class CashCalculator (Calculator):
    USD_RATE = 75.0
    EURO_RATE = 92.0
    RUB_RATE = 1
    def get_today_cash_remained(self, currency):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE),
                      'eur': ('Euro', CashCalculator.EURO_RATE),
                      'rub': ('руб', CashCalculator.RUB_RATE)}
        N = self.remained()
        name, rate = currencies[currency]
        N = round(N / rate, 2)
        if N > 0:
            message = (f'На сегодня осталось {N} {name}')
        elif N == 0:
            message = 'Денег нет, держись'
        else:
            message = (f'Денег нет, держись: твой долг - {-N} {name}')
        return message


