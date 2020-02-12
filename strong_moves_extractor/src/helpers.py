import re


def get_url_groups(url):
    """Return tuple of (protocol, address, port)"""

    address_regex = re.compile(r'(^.*:\/\/)(.*)(:)(.*$)')
    address_r = address_regex.match(url)

    return (address_r.groups()[0][:-3], address_r.groups()[1], int(address_r.groups()[3]))