# Django Mix
Django integration for [Laravel Mix](https://github.com/JeffreyWay/laravel-mix)

Laravel Mix helper in python representation to easy usage with laravel-mix npm package in Django projects.

## Installation

### Django:
```
pip install djangomix
```
### Laravel Mix NPM package:
[Follow instructions on Laravel Mix webpage](https://laravel-mix.com/docs/4.0/installation#stand-alone-project)

Please, see example of webpack.mix.js configration below.

## Usage

```
<script src="{% mix 'app.js' 'polls/static' %}"></script>
```

The paths are related to webpack.mix.js configuration.

Example configration of webpack.mix.js:

```
let mix = require('laravel-mix');

let staticPath = 'polls/static'
let resourcesPath = 'polls/resources'

if (process.argv.includes('--browser-sync')) {
  mix.browserSync('localhost:8000')
}

// setResroucesRoots add prefix to url() in scss on example: from /images/close.svg?a898fb5d07d8c21381d4566b74e12d93 to /static/images/close.svg?a898fb5d07d8c21381d4566b74e12d93
mix.setResourceRoot('/static/')
mix.setPublicPath('polls/static/')

mix.js(`${resourcesPath}/js/app.js`, `${staticPath}/`)
```

---
Maintained by: [Marek Racík](mailto:marek@racik.info) from [IdeaLoop](http://idea-loop.com)
