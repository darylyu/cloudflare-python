def get_site_id(domain_name, sites):
    '''
    Accepts a domain name and a list of sites.

    sites is assumed to be the return value of
    ZoneSerializer.get_basic_info()

    This function will return the CloudFlare ID
    of the given domain name.
    '''
    site_id = None
    match = filter(lambda x: x['name'] == domain_name, sites)
    if match:
        site_id = match[0]['id']
    return site_id
