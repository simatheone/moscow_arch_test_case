from datetime import date, datetime, time
from typing import Tuple

FIRST_WORKING_DAY = 'Вторник'
LAST_WORKING_DAY = 'Суббота'
SEC_IN_A_MIN = 60
TIME_FORMAT = '%H:%M'
WORK_DAY_START_TIME = '8:00'
WORK_DAY_END_TIME = '18:07'
WEEKDAY_TO_ISOWEEKDAY = {
    'Понедельник': 1,
    'Вторник': 2,
    'Среда': 3,
    'Четверг': 4,
    'Пятница': 5,
    'Суббота': 6,
    'Воскресенье': 7,
}


def convert_string_time_to_datetime_obj() -> Tuple[datetime, datetime]:
    """
    Конвертирует исходные данные времени из строки в объект типа datetime.
    """
    end_work_day = datetime.strptime(WORK_DAY_END_TIME, TIME_FORMAT)
    start_work_day = datetime.strptime(WORK_DAY_START_TIME, TIME_FORMAT)
    return start_work_day, end_work_day


def get_current_date_time_stats() -> Tuple[date, time, int]:
    """Возвращает текущую дату, время и порядковый номер дня недели."""
    date_today = date.today()
    time_now = datetime.now().time()
    current_weekday = datetime.now().isoweekday()
    return date_today, time_now, current_weekday


def is_weekend_today(current_weekday: int) -> bool:
    """
    Проверяет, является ли сегодняшний день недели выходным.
    Выходными считаются дни:
        - воскресенье;
        - понедельник.
    """
    if (current_weekday > WEEKDAY_TO_ISOWEEKDAY[LAST_WORKING_DAY] or
        current_weekday < WEEKDAY_TO_ISOWEEKDAY[FIRST_WORKING_DAY]):
        return True
    return False


def get_working_time_for_one_day_in_minutes() -> float:
    """Возвращает количество минут в рабочем дне."""
    start_of_work_day, end_of_work_day = convert_string_time_to_datetime_obj()
    total_time_in_sec = (end_of_work_day - start_of_work_day).total_seconds()
    total_time_in_mins = total_time_in_sec / SEC_IN_A_MIN
    return total_time_in_mins


def count_time_left_to_work_today(time_now: time) -> float:
    """
    Возвращает количество минут, которые сегодня осталось отработать.
    Если количество минут меньше 0, то возвращается 0.
    """
    date_today = date.today()
    start_of_work_day, end_of_work_day = convert_string_time_to_datetime_obj()

    working_start_time = time_now
    if time_now < start_of_work_day.time():
        working_start_time = start_of_work_day.time()

    total_time_in_sec = (
        datetime.combine(date_today, end_of_work_day.time()) -
        datetime.combine(date_today, working_start_time)
    ).total_seconds()

    total_time_in_min = total_time_in_sec / SEC_IN_A_MIN
    return 0 if total_time_in_min < 0 else total_time_in_min


def count_days_left_to_work(current_weekday_num: int) -> int:
    """
    Возвращает количество дней, которые осталось отработать.
    Если количество дней меньше 0, то возвращается 0.
    """
    last_work_day_num = WEEKDAY_TO_ISOWEEKDAY[LAST_WORKING_DAY]
    days_left = last_work_day_num - current_weekday_num
    return 0 if days_left < 0 else days_left


def print_result_message(minutes_in_week_left_to_work: float,
                         left_to_work_today_min: float,
                         weekend: bool) -> str:
    """
    Возвращает итоговое сообщение о количестве оставшихся минут:
        - до конца рабочего дня,
        - до конца рабочей недели.
    """
    if weekend:
        return 'Сегодня выходной.'
    return (
        f'До конца рабочего дня осталось {left_to_work_today_min:.0f} минут.\n'
        f'До конца рабочей недели осталось {minutes_in_week_left_to_work:.0f} '
        'минут.'
    )


if __name__ == '__main__':
    date_today, time_now, current_weekday = get_current_date_time_stats()
    one_day_work_time_in_min = get_working_time_for_one_day_in_minutes()

    weekend = False
    left_to_work_today_min = None
    minutes_in_week_left_to_work = None

    if not is_weekend_today(current_weekday):
        left_to_work_today_min = count_time_left_to_work_today(time_now)
        days_left_to_work = count_days_left_to_work(current_weekday)
        minutes_in_week_left_to_work = (
            days_left_to_work * one_day_work_time_in_min +
            left_to_work_today_min
        )
    else:
        weekend = True

    print(print_result_message(minutes_in_week_left_to_work,
                               left_to_work_today_min,
                               weekend))
