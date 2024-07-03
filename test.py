from backend.Linkedin import Linkedin



def test_bad_role_substring():
    linkedin = Linkedin()
    assert linkedin.bad_role_substring("Software Engineer") == False
    assert linkedin.bad_role_substring("Software Developer") == False
    assert linkedin.bad_role_substring("Software Engineer II") == False
    assert linkedin.bad_role_substring("Software Engineer III") == False



def test_job_exists():
    linkedin = Linkedin()
    job = {
        'job_url': 'https://www.linkedin.com/jobs/view/123',
        'title': 'Software Engineer',
        'company': 'Google',
        'location': 'New York, NY',
        'date_posted': '2021-07-01'
    }
    linkedin.add_job(job)
    assert linkedin.job_exists(job) == True
    assert linkedin.job_exists({'job_url': 'https://www.linkedin.com/jobs/view/456'}) == False


def test_clear_jobs():
    linkedin = Linkedin()
    job = {
        'job_url': 'https://www.linkedin.com/jobs/view/123',
        'title': 'Software Engineer',
        'company': 'Google',
        'location': 'New York, NY',
        'date_posted': '2021-07-01'
    }
    linkedin.add_job(job)
    linkedin.clear_jobs()
    assert linkedin.job_exists(job) == False


