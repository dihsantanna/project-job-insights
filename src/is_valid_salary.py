def is_valid_salary(job, salary):
    job_keys = job.keys()
    if "min_salary" not in job_keys or "max_salary" not in job_keys:
        return False

    if not isinstance(job["min_salary"], int) or not isinstance(
        job["max_salary"], int
    ):
        return False

    if job["min_salary"] > job["max_salary"]:
        return False

    if not isinstance(salary, int):
        return False

    return True
