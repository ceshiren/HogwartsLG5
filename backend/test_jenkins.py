from jenkinsapi.jenkins import Jenkins


def test_jenkins():
    jenkins = Jenkins(
        'http://stuq.ceshiren.com:8020/',
        username='seveniruby',
        password='11d937bfe0f5cdf06fb70074e12dfcac6c'
    )

    print(jenkins.keys())
    print(jenkins.version)
    print(jenkins.jobs.keys())
    print(jenkins.views.keys())
    jenkins.jobs.build("demo")
