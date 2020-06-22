# abby
import json
from mitmproxy import http

url_index = dict()
# 这个是等价类划分
arrays = [-1, 0, 1, 2, 3, 4, 5, 100]


def response(flow: http.HTTPFlow) -> None:
    # 如何响应的key里面包含了 Content-Type  且  Content-Type这个key的值包含了 text
    if 'Content-Type' in flow.response.headers.keys() and \
            'text' in flow.response.headers['Content-Type']:
        #url切割
        url = flow.request.url.split('.ashx')[0]
        # 第一次访问值就是0，今后每次访问+1
        if url not in url_index.keys():
            url_index[url] = 0
        else:
            url_index[url] += 1


        #     结果得到是arrays中的下标
        seed = url_index[url] % len(arrays)
        # 反序列化数据为python 对象
        data = json.loads(flow.response.text)
        # 调用递归函数
        data_new = json_travel(data, num=arrays[seed])
        # 序列化数据
        json_new = json.dumps(data_new, indent=2)
        flow.response.text = json_new


def response1(flow: http.HTTPFlow) -> None:
    if 'Content-Type' in flow.response.headers.keys() and \
            'json' in flow.response.headers['Content-Type']:
        url = flow.request.url.split('.json')[0]
        if url not in url_index.keys():
            url_index[url] = 0
        else:
            url_index[url] += 1



        #     结果得到是arrays中的下标
        seed = url_index[url] % len(arrays)

        data = json.loads(flow.response.text)
        data_new = json_travel(data, num=arrays[seed])
        json_new = json.dumps(data_new, indent=2)
        flow.response.text = json_new



def json_travel(data, array=None, text=1, num=1):
    data_new = None
    # 层层的递归，是为了最后拿到数字类型的数据
    if isinstance(data, dict):
        data_new = dict()
        for k, v in data.items():
            data_new[k] = json_travel(v, array, text, num)
    elif isinstance(data, list):
        data_new = list()
        for item in data:
            item_new = json_travel(item, array, text, num)
            if array is None:
                data_new.append(item_new)
            elif len(data_new) < array:
                data_new.append(item_new)
            else:
                pass
    # 如何实字符串类型的数据，这个特意的出来，乘以num
    elif isinstance(data, str) and '万' in data:
        # data_new = data * text

        data1=float(data.split('-')[0])*num
        data2=float(data.split('-')[1].split('万')[0])*num
        data_new=str(data1)+str('-')+str(data2)+str('万')


    # 如何实int乘以num ,就可以把最小值，最大值，0 ，正数 ，负数都测试一遍
    elif isinstance(data, int) or isinstance(data, float):
        data_new = data * num


    else:
        data_new = data
    return data_new
