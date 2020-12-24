# coding:utf-8
# Name:run.py
# Author:qi.yu
# Time:2020/12/24 3:29 下午
# Description:
import pytest
import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode('utf-8')
        return o


if __name__ == '__main__':
    report_data = './Report/xml'
    report_html = './Report/html'

    args = ['-sv', '--alluredir', report_data, './TestCase', '-m', 'calc']
    pytest.main(args)

    cmd = 'allure generate %s -o %s --clean' % (report_data, report_html)

    try:
        Shell.invoke(cmd)
    except Exception as e:
        print('执行测试用例失败')
        raise