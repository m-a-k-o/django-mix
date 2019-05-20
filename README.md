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

Include in base.html (or any other template)
```
{% load mix %}
```

Use mix template tag in your templates to load scripts, styles,...
```
<script src="{% mix 'app.js' 'polls/static' %}"></script>
```

The paths are related to webpack.mix.js configuration.

---
**Example configration of webpack.mix.js**:

```
let mix = require('laravel-mix');

let staticPath = 'polls/static'
let resourcesPath = 'polls/resources'

// if you don't need browser-sync feature you can remove this lines
if (process.argv.includes('--browser-sync')) {
  mix.browserSync('localhost:8000')
}

mix.setResourceRoot('/static/build') // setResroucesRoots add prefix to url() in scss on example: from /images/close.svg to /static/images/close.svg
mix.setPublicPath('polls/static') // Path where mix-manifest.json is created

mix.js(`${resourcesPath}/js/app.js`, `${staticPath}/`)
```

---
Maintained by: [Marek Racík](mailto:marek@racik.info) from [IdeaLoop](http://idea-loop.com)
