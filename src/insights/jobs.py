from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r") as file:
        list_of_dict = [row for row in csv.DictReader(file)]
        return list_of_dict


def get_unique_job_types(path: str) -> List[str]:
    list_of_jobs = read(path)
    job_types = {job["job_type"] for job in list_of_jobs}
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = [
        job
        for job in jobs
        if job['job_type'] == job_type
    ]

    return filtered_jobs
