import unittest
from datetime import datetime

from time_left_to_work import (TIME_FORMAT, WEEKDAY_TO_ISOWEEKDAY,
                               count_days_left_to_work,
                               count_time_left_to_work_today, is_weekend_today,
                               print_result_message)

MESSAGE_FOR_WEEKEND = 'Сегодня выходной.'
MESSAGE_FOR_WORK_DAY = (
        'До конца рабочего дня осталось {left_to_work_today_min:.0f} минут.\n'
        'До конца рабочей недели осталось {minutes_in_week_left_to_work:.0f} '
        'минут.'
    )


class TestFunctions(unittest.TestCase):

    def test_func_is_weekend_today(self):
        working_day_1, working_day_2 = 2, 6
        weekend_1, weekend_2 = 1, 7
        self.assertFalse(is_weekend_today(working_day_1))
        self.assertFalse(is_weekend_today(working_day_2))
        self.assertTrue(is_weekend_today(weekend_1))
        self.assertTrue(is_weekend_today(weekend_2))

    def test_func_count_days_left_to_work(self):
        current_weekday_1 = 'Пятница'
        current_weekday_2 = 'Понедельник'
        last_working_day = 'Суббота'
        current_weekday_num_1 = WEEKDAY_TO_ISOWEEKDAY[current_weekday_1]
        current_weekday_num_2 = WEEKDAY_TO_ISOWEEKDAY[current_weekday_2]

        last_working_day_num = WEEKDAY_TO_ISOWEEKDAY[last_working_day]
        diff_1 = last_working_day_num - current_weekday_num_1

        self.assertTrue(count_days_left_to_work(current_weekday_num_1), diff_1)
        self.assertTrue(count_days_left_to_work(current_weekday_num_2), 0)

    def test_func_count_time_left_to_work_today(self):
        time_morning = datetime.strptime('9:00', TIME_FORMAT).time()
        time_evening = datetime.strptime('19:00', TIME_FORMAT).time()
        expected_time_morning = 547.0
        expected_time_evening = 0
        self.assertEqual(count_time_left_to_work_today(time_morning),
                         expected_time_morning)
        self.assertEqual(count_time_left_to_work_today(time_evening),
                         expected_time_evening)

    def test_func_print_result_message(self):
        minutes_in_week_left_to_work = 750
        left_to_work_today_min = 300
        weekend = False

        weekend_day = print_result_message(0, 0, True)
        working_day = print_result_message(
            minutes_in_week_left_to_work,
            left_to_work_today_min, weekend
        )
        working_day_message = MESSAGE_FOR_WORK_DAY.format(
            left_to_work_today_min=left_to_work_today_min,
            minutes_in_week_left_to_work=minutes_in_week_left_to_work
        )
        self.assertEqual(weekend_day, MESSAGE_FOR_WEEKEND)
        self.assertEqual(working_day, working_day_message)


if __name__ == '__main__':
    unittest.main()
