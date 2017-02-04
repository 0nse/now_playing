#!/usr/bin/env python
# -*_ coding: utf-8 -*-

import requests


API_KEY = ''
USER = ''


def initialise_data():
    import data.io_helper as io_helper

    global API_KEY, USER
    API_KEY, USER = io_helper.get_data()


def make_request():
    base_url = 'https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks'
    parameters = {
        'api_key':    API_KEY,
        'format':     'json',
        'limit':      '1',
        'nowplaying': 'true',
        'user':       USER
    }
    return requests.get(base_url, parameters)


def process_result(request):
    response = request.json()
    return response['recenttracks']['track'][0]


def is_now_playing(track):
    return track['@attr']['nowplaying'] == 'true'


def format_track(track):
    artist = track['artist']['#text']
    title = track['name']
    return '%s - %s' % (artist, title)


if __name__ == '__main__':
    import time

    initialise_data()
    while True:
        try:
            request = make_request()
            if request.status_code == 200:
                most_recent_track = process_result(request)

                if is_now_playing(most_recent_track):
                    now_playing = format_track(most_recent_track)
                    print(now_playing, flush=True)
        except:
            pass
        time.sleep(5)
