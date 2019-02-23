"""hiretutor URL Configuration
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from .views import hireapp, tutor, guardian

urlpatterns = [
    path('', hireapp.index, name='home'),

    path('guardian/', include(([
                                   path('guardianhomepage/', guardian.GuardianHomepage,
                                        name='guardian_homepage'),
                                   path('guardianprofile/', guardian.GuardianProfile.as_view(),
                                        name='guardian_profile'),

                               ], 'hireapp'), namespace='guardian')),
    path('tutor/', include(([
                                path('tutorhomepage/', tutor.TutorHomepage,
                                     name='tutor_homepage'),
                                path('tutorprofile/', tutor.TutorProfile.as_view(),
                                     name='tutor_profile'),

                            ], 'hireapp'), namespace='tutor')),
]
