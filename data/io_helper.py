#!/usr/bin/env python
# -*_ coding: utf-8 -*-


def get_data_path():
    import os
    import sys

    script_dir = sys.path[0]
    return os.sep.join([script_dir, 'data', 'data.json'])


def get_data():
    import json

    data_path = get_data_path()
    data_file = open(data_path, 'r')
    data_json = data_file.read()
    data_dict = json.loads(data_json)

    api_key = data_dict['api_key']
    user = data_dict['user']

    return (api_key, user)
