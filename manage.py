#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_automation_test.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

#E:\Python37\python3.exe G:/api_automation_test/manage.py runserver 127.0.0.1:8000

#python3 manage.py runserver 192.168.1.110:8000
# 自动化测试平台  http://127.0.0.1:8000/  账号密码：david/123456