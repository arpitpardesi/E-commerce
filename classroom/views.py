from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView
from .forms import ContactForm
from .models import Teacher

# Create your views here.
# def home_view(request):
#     return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYouView(TemplateView):
    template_name = 'classroom/thankyou.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # NOT TEMPLATE ITS url
    success_url = reverse_lazy('classroom:thankyou')
    # success_url = '/classroom/thankyou/ '

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class TeacherCreateView(CreateView):
    model = Teacher
    fields = '__all__'
    # it will automaticall look for the template
    success_url = reverse_lazy('classroom:thankyou')

class TeacherListView( ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('fName')
    context_object_name = 'teacher_list'
    # template will be model_list.html

class TeacherDetailView(DetailView):
    #  returns only one model entry using pk
    model = Teacher
    #  LOOKS FOR model_detail.html