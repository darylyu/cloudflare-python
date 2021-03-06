#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import click

import caches
import development_mode


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
@click.option('--path', default=None, multiple=True)
def cache(action, zone, path):
    # assigning path to paths so it's not too confusing
    # the var name path is retained since we allow multiple --path flags
    paths = path
    response = ''
    if action == 'purge' and paths:
        click.echo('Purging the following cached files:')
        for p in paths:
            click.echo('%s/%s' % (zone, p))
        response = caches.purge_files(zone, paths)

    elif action == 'purge':
        click.echo('Purging cache of %s' % zone)
        response = caches.purge(zone)
    click.echo(response)


@cli.command('dev_mode')
@click.argument('action')
@click.argument('zone')
def dev_mode(action, zone):
    if action == 'get':
        click.echo('Dev mode for %s: ' % zone)
        response = development_mode.get(zone)
    elif action == 'disable':
        response = development_mode.disable(zone)
    elif action == 'enable':
        response = development_mode.enable(zone)


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
