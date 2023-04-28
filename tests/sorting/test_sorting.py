from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 1200, "max_salary": 1600, "date_posted": "2022-03-10"},
        {"min_salary": 400, "max_salary": 2000, "date_posted": "2021-06-07"},
        {"min_salary": 0, "max_salary": 400, "date_posted": "2022-07-22"},
    ]

    ordered_by_min_salary = [
        {"min_salary": 0, "max_salary": 400, "date_posted": "2022-07-22"},
        {"min_salary": 400, "max_salary": 2000, "date_posted": "2021-06-07"},
        {"min_salary": 1200, "max_salary": 1600, "date_posted": "2022-03-10"},
    ]

    ordered_by_max_salary = [
        {"min_salary": 400, "max_salary": 2000, "date_posted": "2021-06-07"},
        {"min_salary": 1200, "max_salary": 1600, "date_posted": "2022-03-10"},
        {"min_salary": 0, "max_salary": 400, "date_posted": "2022-07-22"},
    ]

    ordered_by_date_posted = [
        {"min_salary": 0, "max_salary": 400, "date_posted": "2022-07-22"},
        {"min_salary": 1200, "max_salary": 1600, "date_posted": "2022-03-10"},
        {"min_salary": 400, "max_salary": 2000, "date_posted": "2021-06-07"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == ordered_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == ordered_by_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == ordered_by_date_posted
