# Django Mix
Django integration for [Laravel Mix](https://github.com/JeffreyWay/laravel-mix)

Laravel Mix helper in python representation to easy usage with laravel-mix npm package in Django projects.

## Installation

### Django:
```
pip install djangomix
```

Note: **Do not forget to include the package in requirements**
### Laravel Mix NPM package:
[Follow instructions on Laravel Mix webpage](https://laravel-mix.com/docs/4.0/installation#stand-alone-project)

Please, see example of webpack.mix.js configration below.

## Usage

Add **'djangomix'** to INSTALLED APPS in Django config

```
INSTALLED_APPS = [
    ...
    'djangomix',
]
```

Include in base.html (or any other template)
```
{% load mix %}
```

Use mix template tag in your templates to load scripts, styles,...

Note: Second parameter is path to manifest.json
```
<script src="{% mix 'build/app.js' 'polls/static' %}"></script>
```

The paths are related to webpack.mix.js configuration.

---
You can set path for manifest dir and public path also in Django settings
```
MANIFEST_DIRECTORY = getattr(settings, 'LARAVELMIX_MANIFEST_DIRECTORY','')
PUBLIC_URL = getattr(settings, 'LARAVELMIX_PUBLIC_URL', settings.STATIC_URL)
```
---
**Example configration of webpack.mix.js**:

```
let mix = require('laravel-mix');

let staticPath = 'polls/static/build'
let resourcesPath = 'polls/resources'

mix.setResourceRoot('/static/build') // setResroucesRoots add prefix to url() in scss on example: from /images/close.svg to /static/images/close.svg

mix.setPublicPath('polls/static') // Path where mix-manifest.json is created

// if you don't need browser-sync feature you can remove this lines
if (process.argv.includes('--browser-sync')) {
  mix.browserSync('localhost:8000')
}

// Now you can use full mix api
mix.js(`${resourcesPath}/js/app.js`, `${staticPath}/`)
mix.sass(`${resourcesPath}/sass/app.scss`, `${staticPath}/`)
```
---

Do you have problem with setup? [Read how to setup and start with Vue in Django](https://medium.com/@marek_94752/how-to-start-with-vue-or-any-other-framework-lib-in-django-in-few-minutes-b34fd4291f7)

---
Maintained by: [Marek Racík](mailto:marek@racik.info) from [IdeaLoop](http://idea-loop.com)
