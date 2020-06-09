from reqecho import echo
from flask import *
import time
import sys

@echo.route('/matcher/v2/matchImage', methods=['POST','GET'])
@echo.route('/', methods=['POST','GET'])
def list_header():
    timeout = time.time() + 20
    test_post = """
        <form action="/" method="POST">
        Post Test: <input name="num"></input>
        </form>"""
    while True:
        if time.time() < timeout:
            break
        else:
            sys.exit(1)
            return 'TIMEOUT',500
    print(request.headers)
    if request.method == "GET":
        return test_post
    else:
        try:
            return 'OK',200
        except:
            return test_post
