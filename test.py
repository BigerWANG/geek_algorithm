# coding: utf8
from collections import defaultdict

origin_data = [
                {'appkey': 'xxxx', 'http': 'xxx', "date": "2012-10-10"},
                {'appkey': 'xxxx', 'http': 'xxx', "date": "2012-10-11"},
                {'appkey': 'xxxx', 'http': 'xxx', "date": "2012-10-12"},
                {'appkey': 'xxxx', 'http': 'xxx', "date": "2012-10-13"},
                {'appkey': 'xxxx', 'http': 'xxx', "date": "2012-10-14"},

                {'appkey': 'xxxx1', 'http': 'xxx1', "date": "2012-10-15"},
                {'appkey': 'xxxx1', 'http': 'xxx1', "date": "2012-10-16"},
                {'appkey': 'xxxx1', 'http': 'xxx1', "date": "2012-10-17"},
                {'appkey': 'xxxx1', 'http': 'xxx1', "date": "2012-10-18"},
                {'appkey': 'xxxx1', 'http': 'xxx1', "date": "2012-10-19"},

                {'appkey': 'xxxx2', 'http': 'xxx1', "date": "2012-10-20"},
                {'appkey': 'xxxx2', 'http': 'xxx1', "date": "2012-10-21"},
                {'appkey': 'xxxx2', 'http': 'xxx1', "date": "2012-10-22"},
                {'appkey': 'xxxx2', 'http': 'xxx1', "date": "2012-10-23"},
                {'appkey': 'xxxx2', 'http': 'xxx1', "date": "2012-10-24"},
                {'appkey': 'xxxx2', 'http': 'xxx1', "date": "2012-10-25"},
                {'appkey': 'xxxx2', 'http': 'xxx1', "date": "2012-10-26"},
                {'appkey': 'xxxx2', 'http': 'xxx1', "date": "2012-10-27"},

                {'appkey': 'xxxx3', 'http': 'xxx1', "date": "2012-10-28"},
                {'appkey': 'xxxx3', 'http': 'xxx1', "date": "2012-10-29"},
                {'appkey': 'xxxx3', 'http': 'xxx1', "date": "2012-10-30"},
                {'appkey': 'xxxx3', 'http': 'xxx1', "date": "2012-10-31"},
                {'appkey': 'xxxx3', 'http': 'xxx1', "date": "2012-10-32"},
                {'appkey': 'xxxx3', 'http': 'xxx1', "date": "2012-10-33"},

                {'appkey': 'xxxx4', 'http': 'xxx1', "date": "2012-11-29"},
                {'appkey': 'xxxx4', 'http': 'xxx1', "date": "2012-11-30"},
                {'appkey': 'xxxx4', 'http': 'xxx1', "date": "2012-11-31"},
                {'appkey': 'xxxx4', 'http': 'xxx1', "date": "2012-11-32"},
                {'appkey': 'xxxx4', 'http': 'xxx1', "date": "2012-11-33"},
]

target = {
    "http可用": lambda i: i+1,
    "http调用量": lambda i: i+1,
    "响应时间": lambda i: i+1,
    "机器数": lambda i: i+1,
    "qps": lambda i: i+1,
    "资源利用": lambda i: i+1,
}


def main():
    dic = dict()
    render_data = []
    i = 0
    try:
        for d in origin_data:
            appkey = d["appkey"]
            if dic.has_key(appkey) and dic.get("target") == target[i]:
                dic[appkey]["detail"][d["date"]] = 10
            else:
                dic[appkey] = dict()
                dic[appkey].update(d)
                dic[appkey].pop("date")
                dic[appkey]["target"] = i
                dic[appkey]["detail"] = dict()
                dic[appkey]["detail"][d["date"]] = 20
            i += 1
    except IndexError:
        pass
    for k, v in dic.iteritems():
        d = dict()
        d.update(v)
        render_data.append(d)
    return render_data


if __name__ == '__main__':
    print main()
