# -*- coding: utf-8 -*-
#!/usr/bin/env python2

import click

@click.group()
@click.version_option(prog_name='cloudflare-python', version='0.0.1')
def cli():
    """cloudflare-python - CLI and object wrappers for CloudFlare's API.

    Want to contribute to development?

    Fork the repo at https://github.com/darylyu/cloudflare-python
    """

@cli.command('cache')
@click.argument('action')
@click.argument('zone')
@click.option('--file', default=None)
def cache(action, zone, file):
    click.echo("here")

if __name__ == '__main__':
    cli()
