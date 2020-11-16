import requests

url = 'http://icanhazip.com/'


def get_proxy():
    return requests.get("http://182.92.193.59:5010/get/").json()


def delete_proxy(proxy):
    requests.get("http://182.92.193.59:5010/delete/?proxy={}".format(proxy))


def get_local_ip():
    return requests.get(url).text


def get_random_proxy():
    local_ip = get_local_ip()

    while True:
        ip = get_proxy().get('proxy')
        try:
            proxies = {"http": "http://" + ip, "https": "https://" + ip}
            html = requests.get(url, proxies=proxies)
            # print(html.text + '------' + local_ip)
            if not html.text == local_ip:
                return proxies
            else:
                delete_proxy(ip)
        except Exception:
            delete_proxy(ip)


for i in range(100):
    print('\'%s\',' % get_random_proxy().get('http'))
