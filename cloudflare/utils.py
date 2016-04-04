def get_site_id(domain_name, sites):
    '''
    Accepts a domain name and a list of sites.

    sites is assumed to be the return value of
    ZoneSerializer.get_basic_info()

    This function will return the CloudFlare ID
    of the given domain name.
    '''
    site_id = filter(lambda x: x['name'] == domain_name, sites)
    return site_id
