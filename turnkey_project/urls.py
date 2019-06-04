from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'turnkey_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^askfeedback/', include('askfeedback.urls')),
    url(r'^leavefeedback/', include('leavefeedback.urls')),
    
]
