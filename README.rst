===============================
CloudFlare - Python Wrappers
===============================

.. image:: https://img.shields.io/travis/darylyu/cloudflare.svg
        :target: https://travis-ci.org/darylyu/cloudflare

.. image:: https://img.shields.io/pypi/v/cloudflare.svg
        :target: https://pypi.python.org/pypi/cloudflare


STILL UNDER DEVELOPMENT! It'll provide a CLI and Python wrappers for CloudFlare's REST API

* Free software: BSD license
* Documentation: https://cloudflare.readthedocs.org.

Features
--------

* TODO

Usage
-----

    According to CloudFlare's official API documentation, a `zone` is a domain name along with its subdomains and other identities.

  .. code-block:: bash

    # General form:
    $ cloudflare <noun> <verb> <noun_instance> args...

    # Add a site to your CloudFlare account:
    $ cloudflare zone create example.com

    # List the DNS entries for a site
    $ cloudflare dns list example.com

    # Create a DNS entry for a site
    $ cloudflare dns create subdomain.example.com 1.2.3.4 --type=A

    # Update a DNS entry for a site
    $ cloudflare dns update subdomain.example.com 1.2.3.4 --type=CNAME
