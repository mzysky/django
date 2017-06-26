from django.conf.urls  import url, include
import blog.views

urlpatterns = [
        url(r'^create/', blog.views.create_blogpost),
        url(r'^$', blog.views.archive),
]

