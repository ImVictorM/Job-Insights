from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industries_list = read(path)

    unique_industries = {
        industry["industry"]
        for industry in industries_list
        if industry["industry"]
    }

    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_jobs = [
        job
        for job in jobs
        if job['industry'] == industry
    ]

    return filtered_jobs
