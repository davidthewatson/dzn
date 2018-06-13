import os
import shutil
import tempfile
import urllib.request as urllib2
import zipfile

CONTIGUOUS_STATES = (
    ('AL', 'Alabama'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

#: Non contiguous states (Not connected to mainland USA)
NON_CONTIGUOUS_STATES = (
    ('AK', 'Alaska'),
    ('HI', 'Hawaii'),
)

US_STATES = CONTIGUOUS_STATES + NON_CONTIGUOUS_STATES

ZILLOW_SHAPEFILE_URL = 'http://www.zillow.com/static/shp/ZillowNeighborhoods-%s.zip'
ZILLOW_SHAPEFILE_DIR = './'

def main():
    for abbrev, name in US_STATES:
        print('Downloading\ %s neighborhoods\n' % abbrev)
        try:
            url = ZILLOW_SHAPEFILE_URL % abbrev
            zip_file = download(url)
        except Exception as e:
            print('Warning: Failed to fetch %s: %s\n' % (url, str(e)))
            continue
        try:
            zipfile.ZipFile(zip_file).extractall(ZILLOW_SHAPEFILE_DIR)
        finally:
            zip_file.close()


def download(url):
    """Helper function to download a file to a temporary location."""
    remote = urllib2.urlopen(url)
    local = tempfile.NamedTemporaryFile(dir=ZILLOW_SHAPEFILE_DIR)
    try:
        shutil.copyfileobj(remote, local)
    except Exception as e:
        local.close()
        raise
    finally:
        remote.close()
    return local

if __name__ == '__main__':
    main()
