from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)

    list_of_salaries = [
        int(salary["max_salary"])
        for salary in jobs
        if salary["max_salary"].isdigit()
    ]

    max_salary = max(list_of_salaries)

    return max_salary


def get_min_salary(path: str) -> int:
    jobs = read(path)

    list_of_salaries = [
        int(salary["min_salary"])
        for salary in jobs
        if salary["min_salary"].isdigit()
    ]

    min_salary = min(list_of_salaries)

    return min_salary


def validate_given_info(job: Dict, salary: Union[int, str]):
    try:
        job_max_salary = int(job["max_salary"])
        job_min_salary = int(job["min_salary"])
        int(salary)
        if job_max_salary < job_min_salary:
            raise ValueError()
    except Exception:
        raise ValueError()


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    validate_given_info(job, salary)

    if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
        return True
    else:
        return False


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
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
    raise NotImplementedError
