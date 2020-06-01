from reqecho import echo
from flask import *

@echo.route('/', methods=['POST','GET'])
def list_header():
    if request.method == "GET":
        return """
        <form action="/" method="POST">
        <input name="num"></input>
        </form>"""
    else:
        try:
            result = ""
            for key in request.headers.keys():
                result += "{}: {}</br>".format(key, request.headers[key])
            return result
        except:
            return """
                    <form action="/" method="POST">
                    <input name="num"></input>
                    </form>"""
