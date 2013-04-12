from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home_view'),
    url(r'^about$', 'home.views.home_view'),
    url(r'^contact$', 'home.views.home_view'),
    url(r'^profile/(?P<username>[\w.@+-]+)$', 'accounts.views.profile_view'),
    url(r'^accounts/logout$', 'accounts.views.logout_view'),
    url(r'^accounts/signup$', 'accounts.views.signup_view'),
    url(r'^accounts/register$', 'accounts.views.register'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^account_redirect$', 'accounts.views.account_redirect'),
    # url(r'^tutoring_site/', include('tutoring_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


