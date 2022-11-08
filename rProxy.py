from flask import Flask, request, redirect, Response
import requests

app = Flask(__name__)

host_name = 'http://localhost:5000/'

@app.route('/')
def index():
    # is_up =  requests.get(host_name).status_code
    try:
        is_up =  requests.get(host_name).status_code
        print(is_up)
    except Exception as e:
        is_up = "CANNOT MAKE CONNECTION | NO STATUS CODE"
        print(">", e)

    return f'<h1>The Proxy server <br> </h1> {is_up}'

@app.route('/<path:path>',methods=['GET','POST','DELETE'])
def proxy(path):
    global host_name
    if request.method=='GET':
        # try:
            resp = requests.get(f'{host_name}{path}')
            print(resp.status_code)
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code)
            if resp.status_code == 200:
                return response
            else:
                return "this requested page doesn't exist! return <a href='/'>home</a>"

    elif request.method=='POST':
        resp = requests.post(f'{host_name}{path}',json=request.get_json())
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response

    elif request.method=='DELETE':
        resp = requests.delete(f'{host_name}{path}').content
        response = Response(resp.content, resp.status_code, headers)
        return response


if __name__ == '__main__':
    app.run(port=5001)