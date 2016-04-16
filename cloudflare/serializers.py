# -*- coding: utf-8 -*-
class ZoneSerializer(object):

    def __init__(self, http_response):
        zones = http_response.json()['result']
        self.data = zones

    def human_readable(self):
        human_readable = ''
        zones = self.data
        for z in zones:
            zone_info = '\n%s - %s - %s' % (z['id'], z['name'], z['status'])
            human_readable += zone_info
        return human_readable

    def get_basic_info(self):
        zones = self.data

        # return a list of lightweight zones
        # the lightweight zones only have the IDs and names
        lw_zones = [{'id': x['id'], 'name': x['name']} for x in zones]

        return lw_zones
