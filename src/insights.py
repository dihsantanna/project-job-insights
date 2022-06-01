from src.jobs import read
from src.is_valid_salary import is_valid_salary


def get_unique_job_types(path):
    info_jobs = read(path)
    job_types = list()

    for job in info_jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    info_jobs = read(path)
    industries = list()

    for job in info_jobs:
        industry = job["industry"].strip()
        if industry not in industries and industry != '':
            industries.append(industry)
    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    info_jobs = read(path)
    max_salary = 0

    for job in info_jobs:
        salary = str(job["max_salary"])
        digit = int(salary) if salary.isdigit() else 0

        if digit > max_salary:
            max_salary = digit

    return max_salary


def get_min_salary(path):
    info_jobs = read(path)
    min_salary = get_max_salary(path)

    for job in info_jobs:
        salary = str(job["min_salary"])
        digit = int(salary) if salary.isdigit() else 0

        if digit < min_salary and digit != 0:
            min_salary = digit

    return min_salary


def matches_salary_range(job, salary):
    if not is_valid_salary(job, salary):
        raise ValueError

    return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    ranges = []
    for job in jobs:
        if is_valid_salary(job, salary) and matches_salary_range(job, salary):
            ranges.append(job)
    return ranges
