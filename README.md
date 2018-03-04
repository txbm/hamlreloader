# HamlReloader
[![Build Status](https://travis-ci.org/petermelias/hamlreloader.png?branch=master)](https://travis-ci.org/petermelias/hamlreloader) [![Coverage Status](https://coveralls.io/repos/petermelias/hamlreloader/badge.png?branch=master)](https://coveralls.io/r/petermelias/hamlreloader?branch=master) [![Downloads](https://img.shields.io/pypi/dm/hamlreloader.svg)](https://crate.io/packages/hamlreloader) [![Downloads](https://img.shields.io/pypi/v/hamlreloader.svg)](https://crate.io/packages/hamlreloader)

## Usage

1) Run without arguments to read and generate to same directory

``` hamwatch ```

2) Run with arguments for source / target spec.

``` hamwatch my_haml/ my_html/ ```

 - OR -

``` hamwatch . rendered/ ```

CLI outputs generated path on change.

Boom. That's it.