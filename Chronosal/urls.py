from django.urls import include, path
from django.contrib import admin
from chronos import views
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/chronos/'


urlpatterns = [
    path('', views.index, name='index'),
    path('chronos/', include('chronos.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


