from src.pre_built.counter import count_ocurrences


def test_counter():
    JOBS_FILE_PATH = "data/jobs.csv"
    FILE_PYTHON_OCURRENCES = 1639

    assert count_ocurrences(JOBS_FILE_PATH, "python") == FILE_PYTHON_OCURRENCES
    assert count_ocurrences(JOBS_FILE_PATH, "PYTHON") == count_ocurrences(
        JOBS_FILE_PATH, "python"
    )
