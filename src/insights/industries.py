from typing import List, Dict
import jobs


def get_unique_industries(path: str) -> List[str]:
    industries_list = jobs.read(path)
    unique_industries = {industry["industry"] for industry in industries_list}
    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
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
    raise NotImplementedError
