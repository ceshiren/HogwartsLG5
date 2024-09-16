from jenkinsapi.jenkins import Jenkins
from jenkinsapi.job import *
# def test_jenkins():
#     jenkins = Jenkins(
#         'http://106.53.106.215:8081/',
#         username='john',
#         password='110440d03256a94eb905c545d22afddf20',
#         # useCrumb= True
#     )


def test_jenkins():
    jenkins = Jenkins(
        'http://192.168.50.232:8081/',
        username='john',
        password='113353d2bafd76427f8b39640853e81e6d',
        # useCrumb=True
    )
    print(jenkins.keys())
    print(jenkins.version)
    print(jenkins.jobs)
    print(jenkins.get_jobs())
    # for job_name in jenkins.keys():
    #     my_job = jenkins.get_job(job_name)
    #     print(job_name)
    #     print(my_job)
    #     jenkins.build_job(my_job)
