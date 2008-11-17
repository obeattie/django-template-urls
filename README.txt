This is a very simple library to help with URLs in Django templates. Basically, this is a set of two template filters,
which ensure that any URLs they are given are either absolute or relative. This is very useful if you have a lot of
get_url methods and the such defined which return relative URLs and you want them displayed on the site as absolute
ones (or vice-versa, although that's less common for sure).

To use this, you'll need to copy the templatetags directory into one of your applications. If you're not familiar with
doing this, you'll find more information at http://docs.djangoproject.com/en/dev/howto/custom-template-tags/

Now you should be good to go. Put a {% load urls %} at the top of any of your templates you want to use the library in,
and then you can do things like {{ variable|absolute_url }} or {{ variable|relative_url }}.

To note is that the domain is taken from the Django sites application (Site.objects.get_current().domain) -- so if
you're not using sites, this won't work. If you are, make sure that it's up-to-date :)
