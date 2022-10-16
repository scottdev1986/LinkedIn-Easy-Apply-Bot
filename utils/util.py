def parse_job_title(job_title: str, blackList_titles:list) -> bool:
    """Parse job title."""
    for title in blackList_titles:
        if title.lower() in job_title.lower():
            return True
    return False
