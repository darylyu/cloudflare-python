#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import click

import caches

from http_client import CloudFlareClient


@click.group()
@click.version_option(prog_name='cloudflare-python', version='0.0.2')
def cli():
    """cloudflare-python - CLI and object wrappers for CloudFlare's API.

    Want to contribute to development?

    Fork the repo at https://github.com/darylyu/cloudflare-python
    """

@cli.command('cache')
@click.argument('action')
@click.argument('zone')
@click.option('--path', default=None)
def cache(action, zone, path):
    if action == 'purge':
        click.echo('Purging cache of %s' % zone)
        response = caches.purge(zone)
        click.echo(response)


@cli.command('dns')
@click.argument('action')
@click.argument('url')
@click.argument('value')
@click.option('--type', default=None)
def dns(action, url, value, type):
    click.echo("Updating DNS of %s" % url)


@cli.command('zone')
@click.argument('action')
@click.argument('zone')
def zone(action, zone):
    click.echo("Performing zone command on %s" % zone)


if __name__ == '__main__':
    cli()
