# -*- coding: utf-8 -*-
import json
import os

class JSONConfigReader(object):

    def read(self, config_path="~/.cloudflare.jsonl"):
        os_agnostic_path = os.path.expanduser(config_path)
        with open(os_agnostic_path) as config_file:
            for line in config_file:
                auth_pair = json.loads(line)
                self.email = auth_pair.get('email')
                self.api_key = auth_pair.get('api_key')
