===============================
cloudflare-python
===============================

.. image:: https://img.shields.io/travis/darylyu/cloudflare.svg
        :target: https://travis-ci.org/darylyu/cloudflare

.. image:: https://img.shields.io/pypi/v/cloudflare.svg
        :target: https://pypi.python.org/pypi/cloudflare

THIS PROJECT IS STILL IN ITS PLANNING STAGE!

cloudflare-python provides a CLI and Python wrappers for CloudFlare's API.

* Free software: BSD license
* Documentation: https://cloudflare-python.readthedocs.org.

Configuration
-------------
We need to create a configuration file the first time you use this.

  .. code-block:: bash
  $ cloudflare config

This asks you for the email address and API key associated with your CloudFlare account.

It then creates a file named .cloudflare.yaml in your home directory. The first line is your API key. The second line is the email address tied to your CloudFlare account.

  .. code-block:: yaml
     ---
     email: email@example.com
     api_key: 8q688bzazqqnhlyflwv88mldw53o62v7e8kzx

     zones:
     - name: example1.com
       id: 1eb3b3756c4180adeba44e1fef92981r7

     - name: example2 .com
       id: 0e23f3756c464641eba44e1fef92981rz

We need this file, because CloudFlare's API wants the zone ID for most requests and it would be expensive to fetch it every time.

Usage
-----

  .. code-block:: bash

    # General form:
    $ cloudflare <noun> <verb> <noun_instance> args...

Usage: zones
------------

According to CloudFlare's official API documentation, a `zone` is a domain name along with its subdomains and other identities.

  .. code-block:: bash

    # Add a site to your CloudFlare account:
    $ cloudflare zone create example.com

    # Show the basic info for a site tied to your CloudFlare account.
    $ cloudflare zone show example.com

    # List the sites tied to your CloudFlare account.
    $ cloudflare zone list

Usage: DNS
------------

  .. code-block:: bash

    # Show the DNS entries for a site
    $ cloudflare dns show example.com

    # Create a DNS entry for a site
    $ cloudflare dns create subdomain.example.com 1.2.3.4 --type=A

    # Update a DNS entry for a site
    $ cloudflare dns update subdomain.example.com 1.2.3.4 --type=CNAME

Usage: cache
------------

  .. code-block:: bash

    # Purge all files in a zone's cache
    $ cloudflare cache purge example.com

    # Purge a specific file in a zone's cache
    $ cloudflare cache purge example.com --path=<url>
