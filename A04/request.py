from http.client import HTTPConnection

__author__ = 'Aly'


from json_with_dates import loads


def request_to_birt(path=""):
    print('path', path)
    hconn = HTTPConnection('localhost', 80)
    hconn.request('GET', '/cgi-bin/birt.py' + path)
    resp = hconn.getresponse()
    print('status', resp.status)
    body_j = resp.read()
    # print('body',body)
    body_str = body_j.decode()
    if resp.status == 200:
        #data = json_with_dates.loads(bodystr)
        #return data #json_with_dates.loads(hconn.getresponse().read().decode())
        body = loads(body_str)
        return 'K', body
    else:
        print("response status", resp.status)
        print('body_str', body_str)
        return 'E', resp.status, body_str