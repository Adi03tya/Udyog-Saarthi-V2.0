"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
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
from django.contrib import admin
from django.urls import path
from udyogSaarthi.views import*
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('register_candidate/',register_candidate,name='register_candidate'),
    path('register_employer/',register_employer,name='register_employer'),
    path('candidate_login/',candidate_login,name='candidate_login'),
    path('employer_login/',employer_login,name='employer_login'),
    path('candidate_home/',candidate_home,name='candidate_home'),
    path('employer_home',employer_home,name='employer_home'),
    path('previous_Year_questions',previous_Year_questions,name='previous_Year_questions'),
    path('logout_page',logout_page,name="logout_page"),
    path('jobs_page',jobs_page,name='jobs_page'),
    path('jobs/apply/<int:job_id>/', apply_job, name='apply_job'),
    path ('posted_job',posted_job,name='posted_job'),
    path('jobs/applicants/<int:job_id>/',applicants,name='applicants'),
    path('candidate_profile',candidate_profile,name='candidate_profile'),
    path('tutorials',tutorials,name='tutorials'),
    path('base',base,name='base'),
    path('home',home,name='home'),
    # path('generate-speech/', generate_speech, name='generate_speech'),
    path('register_candidate_new/',register_candidate_new,name='register_candidate_new'),
    # path('convert_to_speech/', convert_to_speech, name='convert_to_speech')
    # path('scrape_data/',scrape_data,name='scrape_data'),
    path('scrape/', scrape_data_view, name='scrape_data'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)