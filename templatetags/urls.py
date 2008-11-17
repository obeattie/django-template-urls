"""URL-related template library."""
import re

from django import template
from django.contrib.sites.models import Site
from django.template.defaultfilters import stringfilter

__author__ = u'Oliver Beattie'

register = template.Library()

# Pattern for matching an absolute URL
ABSOLUTE_URL_PATTERN = re.compile(r'http:\/\/(?P<host>[\w\.]+)(?P<extra>.*)')

@register.filter
@stringfilter
def absolute_url(value):
    """Makes sure that the URL is a fully-qualified, absolute URL. The only instance
       where this will fail (lol) is when a relative URL is not prepended by a leading
       slash (the filter can't determine the current path so this can't be implemented.)"""
    domain = Site.objects.get_current().domain
    if ABSOLUTE_URL_PATTERN.match(value):
        # If the value is already an absolute URL, just return it as-is
        return value
    else:
        value = value.rsplit(domain, 1)[-1]
        # Remove leading and trailing slashes, these are re-added when returned
        if value[0] == '/':
            value = value[1:]
        if value[-1:] == '/':
            value = value[:-1]
        if len(value.rsplit('#', 1)) < 2:
            # The URL has no anchor, so add a trailing slash
            value += u'/'
        return u'http://%s/%s' % (domain, value)

@register.filter
@stringfilter
def relative_url(value):
    """Returns a relative URL from the passed URL. Basically absolute_url in reverse :)"""
    domain = get_domain()
    match = ABSOLUTE_URL_PATTERN.match(value)
    if not match:
        # The value is not an absolute URL, so just return that shit :)
        return value
    else:
        # Absolutification
        return match.group('extra')
