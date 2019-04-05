import json
import os

from django import template

register = template.Library()


@register.simple_tag
def mix(path, manifest_directory=''):
    if path[0] != '/':
        path = f'/{path}'

    if manifest_directory and manifest_directory[0] != '/':
        manifest_directory = f'{manifest_directory}'

    if os.path.exists(manifest_directory + '/hot'):
        return f'//localhost:8080{path}'

    manifest_path = manifest_directory + '/mix-manifest.json'

    if not os.path.exists(manifest_path):
        raise FileNotFoundError

    with open(manifest_path, 'r') as f:
        manifest = json.load(f)

    if path not in manifest:
        raise Exception('Unable to locate mix file: ' + path)

    return '/static' + manifest[path]

