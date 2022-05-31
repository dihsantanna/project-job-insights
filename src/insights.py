from src.jobs import read


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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
