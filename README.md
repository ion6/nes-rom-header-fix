ROM Manager
===========

This project includes various small utilities for managing ROMs.

sort.py
-------
Usage:

`sort.py --path /path/to/sort>`

This script takes the path of a flat-directory zipped roms, then sorts the roms in that path according to the following folders / rules:

- `beta`: Beta, prototype, unlicensed roms
- `import`: International (non-USA) ROMS
- `zip`: A backup copy of the zipped licensed and released USA roms
- An unzipped copy of the licensed and released USA roms in the root folder

fix-headers.py
--------------

Usage:

`fix-headers.py --path /path/to/nes/roms --ext nes --recursive`

If you omit a file extension, it assumes 'nes'.  The search is non-recursive by default.

This utility analyzes NES headers and fixes them if they are missing or corrupt. `path` can point to a single file or a directory, in which case `fix-headers` will analyze each file in that directory.

This utility is a refactoring of the ines-fix utility from Greg Kennedy:

[https://greg-kennedy.com/wordpress/2012/05/30/ines-header-fixer/](https://greg-kennedy.com/wordpress/2012/05/30/ines-header-fixer/)

The utility should now be python 2/3 compatible, and can be called on a single rom or a directory

Which in turn relies up BootGod's ROM XML document:
[http://bootgod.dyndns.org:7777/xml.php](http://bootgod.dyndns.org:7777/xml.php)

