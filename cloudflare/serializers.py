# -*- coding: utf-8 -*-
class ZoneSerializer(object):
    '''
    Helper class for serializing the JSON response
    to something that is more suited to the calling
    function or CLI.

    Example: It doesn't make sense to show all of the zone
    info for `cloudflare zone list all` - just the most
    important ones. And it doesn't make sense to get as
    much info as `cloudflare zone list all` for the other
    commands.
    '''

    def __init__(self, http_response):
        '''
        Constructor. Accepts the HTTP response, but doesn't
        do any parsing. Parsing is done by the other functions.
        '''
        zones = http_response.json()['result']
        self.data = zones

    def human_readable(self):
        human_readable = ''
        zones = self.data
        for zone in zones:
            zone_info = '\n%s - %s - %s' % (zone['id'],
                                            zone['name'],
                                            zone['status'])
            human_readable += zone_info
        return human_readable

    def get_basic_info(self):
        zones = self.data

        # return a list of lightweight zones
        # the lightweight zones only have the IDs and names
        lw_zones = [{'id': x['id'], 'name': x['name']} for x in zones]

        return lw_zones
