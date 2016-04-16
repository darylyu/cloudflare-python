# -*- coding: utf-8 -*-
from .http_client import CloudFlareClient


def purge(url):
    cfc = CloudFlareClient()
    response = cfc.purge_cache(url)
    msg = ''
    if response['success']:
        msg = 'Successful!'
    else:
        for error in response['errors']:
            msg += 'ERROR: (%s) %s\n' % (error['code'], error['message'])
    return msg


def purge_files(url, paths):
    cfc = CloudFlareClient()
    paths = ['http://www.%s/%s' % (url, p) for p in paths]
    response = cfc.purge_cache(url, paths)
    msg = ''
    if response['success']:
        msg = 'Successful!'
    else:
        for error in response['errors']:
            msg += 'ERROR: (%s) %s\n' % (error['code'], error['message'])
    return msg
