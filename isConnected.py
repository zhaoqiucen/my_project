import requests


def is_connected():
    try:
        res = requests.get("http://www.baidu.com", timeout=1)
        print(res)
        return 'Connected OK'
    except:
        return 'Connected Fail'


if __name__ == '__main__':
    res = is_connected()
    print(res)
