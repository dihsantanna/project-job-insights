from src.sorting import sort_by

jobs = [
    {
        "job_title": "job1",
        "min_salary": "3500",
        "max_salary": "4000",
        "date_posted": "2020-05-08",
        "id": "0",
    },
    {
        "job_title": "job2",
        "min_salary": "3600",
        "max_salary": "4100",
        "date_posted": "2020-05-09",
        "id": "1",
    },
    {
        "job_title": "job3",
        "min_salary": "3700",
        "max_salary": "4200",
        "date_posted": "2020-05-10",
        "id": "2",
    },
]

expected_min_salary = jobs

expected_max_salary = [
    {
        "job_title": "job3",
        "min_salary": "3700",
        "max_salary": "4200",
        "date_posted": "2020-05-10",
        "id": "2",
    },
    {
        "job_title": "job2",
        "min_salary": "3600",
        "max_salary": "4100",
        "date_posted": "2020-05-09",
        "id": "1",
    },
    {
        "job_title": "job1",
        "min_salary": "3500",
        "max_salary": "4000",
        "date_posted": "2020-05-08",
        "id": "0",
    },
]

expected_date_posted = expected_max_salary


min_salary, max_salary, date_posted = [
    "min_salary",
    "max_salary",
    "date_posted",
]


def test_sort_by_criteria():
    sort_by(jobs, min_salary)
    assert jobs == expected_min_salary

    sort_by(jobs, max_salary)
    assert jobs == expected_max_salary

    sort_by(jobs, date_posted)
    assert jobs == expected_date_posted
