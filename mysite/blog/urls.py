from django.conf.urls  import url, include
import blog.views

urlpatterns = [
        url(r'^$', blog.views.archive),
]

