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

This assumes that you saved your configuration in ~/.cloudflare.jsonl

It should contain a single line JSON with keys `email` and `api_key`.

The key `email` is the email address tied to your CloudFlare account.

Your CloudFlare API key can be found here: https://www.cloudflare.com/a/account/my-account

Example:

    .. code-block:: javascript

      {"email": "john@example.com", "api_key": "21d2f4a18141b891256400d40f289748f1a2b"}


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
    $ cloudflare cache purge example.com --path=favicon.ico

    # It is also possible to purge multiple files
    $ cloudflare cache purge example.com --path=favicon.ico --path=index.html
