import os
from functools import wraps
from pandas import json_normalize


def response_decorator(func):
    @wraps(func)
    async def decorate(*args, **kwargs):
        response = await func(*args, **kwargs)
        if not response.content:
            response._content = b"{}"
        data = response.json()
        return data

    return decorate


async def save_exel(path, data, file_name):
    path = f'./downloads/{path}'
    os.makedirs(path, exist_ok=True)
    df = json_normalize(data)
    df.to_excel(f'{path}/{file_name}', index=False)


def _filter(f, dicts):
    result = []
    for _dict in dicts:
        if eval(f):
            result.append(_dict)
    return result


async def base_filter(params, list_dicts, depth=None):
    f = [f'_dict["{k}"]=={v}' for k, v in params.items() if v]
    if f:
        f = ' and '.join(f)
        print(11111, f, depth)
        if depth:
            res_list = []
            for _dicts in list_dicts:
                res = _filter(f, _dicts.pop(depth))
                if res:
                    _dicts[depth] = res
                    res_list.append(_dicts)
            return res_list
        else:
            return _filter(f, list_dicts)
    return list_dicts
