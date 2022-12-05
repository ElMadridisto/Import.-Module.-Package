from application.salary import calculate_salary
from application.db.get_employees import get_employees
from application.datetime_m import date_today
if __name__ == '__main__':

    calculate_salary()
    get_employees()
    date_today()