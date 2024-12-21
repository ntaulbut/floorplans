# ![Directory Logo](https://github.com/ntaulbut/floorplans/blob/main/site/src/icons/favicon-32x32.png?raw=true) Floorplans
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub License](https://img.shields.io/github/license/ntaulbut/floorplans)

Website providing a directory of University of Nottingham floorplans.
Building names and codes are scraped semi-automatically using `scrape.js`, these are then used by `find_floorplans.py` to check possible URLs.
The resulting floorplans information is used to generate a static site with Jinja templates.

![a](https://public.ntaulbut.dev/floorplans-site-screenshot.png)

## Testimonials
> wow this is great!

> nathaniel is slowly taking over the entire uon web infastructure \
> and making it 100x better

> Best website ever \
> Trying to find floor plans is a massive pain

> this is actually brilliant \
> very well done

## Update: 21/12/2024
The [Building Information Website](http://buildinginformation.nottingham.ac.uk/) used to scrape the building information, originally made circa 2005, has finally kicked the bucket:
> Microsoft OLE DB Provider for ODBC Drivers error '80004005' \
> [Microsoft][ODBC SQL Server Driver][DBNETLIB]SSL Security error \
> /frMenu.asp, line 11

So it's not as easy to get that information anymore. Hopefully they don't build any new buildings.

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg)](https://www.digitalocean.com/?refcode=ffbee9c97029&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
