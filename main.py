import os
from google.appengine.ext.webapp import util
from django.conf import settings
import django.core.handlers.wsgi

settings._target = None
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

def real_main():
    application = django.core.handlers.wsgi.WSGIHandler()
    util.run_wsgi_app(application)

def profile_main():
    import cProfile, pstats
    prof = cProfile.Profile()
    prof = prof.runctx("real_main()", globals(), locals())
    print "\n<pre>"
    print '--------------------[PROFIILING INFORMATION]-------------------'
    stats = pstats.Stats(prof)
    stats.sort_stats("time")  # Or cumulative
    stats.print_stats(20)
    print "</pre>"

main = real_main
if settings.PROFILE:
    main = profile_main

if __name__ == '__main__':
    main()