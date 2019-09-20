import json
import os
from django.conf import settings
from django import template

register = template.Library()

MANIFEST_DIRECTORY = getattr(settings, 'LARAVELMIX_MANIFEST_DIRECTORY','')
PUBLIC_URL = getattr(settings, 'LARAVELMIX_PUBLIC_URL', settings.STATIC_URL)

@register.simple_tag
def mix(path, manifest_directory=MANIFEST_DIRECTORY):
    os_sep = os.path.sep

    # laravel-mix generate / on the path in manifest.json
    if path[0] != '/': # url separator
        path = f'/{path}'


    if os.path.exists(os.path.join(manifest_directory, 'hot')):
        # taken from https://github.com/laravel/framework/blob/master/src/Illuminate/Foundation/Mix.php
        url = open(os.path.join(manifest_directory, 'hot')).read().strip()
        if 'http://' or 'https://' in url:
            return ':'.join(url.split(':')[1:]) + path
        else:
            return f'//localhost:8080{path}'

    manifest_path = os.path.join(manifest_directory ,'mix-manifest.json')

    if not os.path.exists(manifest_path):
        raise FileNotFoundError('Unable to locate manifest file: '
                                + manifest_path)

    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    for key, value in manifest.items():
        if path in key:
            path = key
            full_path = f"{PUBLIC_URL.rstrip('/')}/{manifest[path].lstrip('/')}"
            return full_path
    raise Exception('Unable to locate mix file: ' + path)
