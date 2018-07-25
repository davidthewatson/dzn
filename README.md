# dzn

Download Zillow Neighborhoods in pure python

## Summary

This script was inspired by https://github.com/claymation/django-zillow-neighborhoods

The difference is that while the former requires various bits of django, this
one eliminates the need for django imports by copying US states from 
django local flavor in order to have an
iterable US state list. Further, it merely downloads the files to the local
file system instead of importing those files into various django models.

You can do what you like with the downloaded files. I assume your use case may
be different than that implied by the aforementioned django models.

## Install

What install?

I run pyenv. This has only been tested on python 3.6.2.

## Requirements

What requirements?

## Runtime

    python download_zillow_neighborhoods.py
