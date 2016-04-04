# -*- coding: utf-8 -*-
import json

from .config import email, api_key
from .serializers import ZoneSerializer
from .utils import get_site_id

import requests
DEFAULT_API_HOST = 'https://api.cloudflare.com/client/v4'

class CloudFlareClient(object):

    def __init__(self, api_host=DEFAULT_API_HOST, email=email, api_key=api_key):
        # api_host, email, api_key are optional.
        # If they are not explicitly set, it is assumed that
        # it is used within this package so it gets the auth information
        # from config.JSONConfigReader which in turn gets
        # it from ~/.cloudflare.jsonl
        self.api_host = api_host
        self.email = email
        self.api_key = api_key

        # pre=configure the auth requirements
        self.headers = {}
        self.headers['X-Auth-Email'] = email
        self.headers['X-Auth-Key'] = api_key
        self.headers['Content-Type'] = 'application/json'

    def __get__(self, end_point, query_params={}):
        full_url = '%s%s' % (self.api_host, end_point)
        response = requests.get(full_url, headers=self.headers)
        return response

    def __delete__(self, end_point, data={}):
        full_url = '%s%s' % (self.api_host, end_point)
        print data
        print full_url
        response = requests.delete(full_url, headers=self.headers, data=data)
        return response

    def get_zones_and_internal_ids(self):
        # This does not directly map to the /zones end point. We use this
        # mainly for the site IDs, because the other API calls use the site
        # ID instead of the domain name.
        end_point = '/zones'
        response = self.__get__(end_point)
        serializer = ZoneSerializer(response)
        data = serializer.get_basic_info()
        return data

    def list_zones(self):
        # https://api.cloudflare.com/#zone-list-zones
        end_point = '/zones'
        response = self.__get__(end_point)
        serializer = ZoneSerializer(response)
        data = serializer.data
        return data

    def purge_cache(self, url):
        sites_and_ids =  self.get_zones_and_internal_ids()
        site_id = get_site_id(url, sites_and_ids)
        end_point = '/zones/%s/purge_cache' % site_id

        data = {}
        data['purge_everything'] = True
        response = self.__delete__(end_point, data=json.dumps(data))
        print response.text
        return response
