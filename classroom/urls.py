from django.urls import path
from .views import HomeView, ThankYouView, ContactFormView, TeacherCreateView, TeacherListView, TeacherDetailView

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thankyou/', ThankYouView.as_view(), name='thankyou'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('createteacher', TeacherCreateView.as_view(), name='createteacher'),
    path('list_teacher/', TeacherListView.as_view(), name='list_teacher'),
    path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='detailteacher'),
]
