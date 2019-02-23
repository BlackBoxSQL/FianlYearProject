from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from ..filters import GuardianFilter
from ..decorators import tutor_required
from ..models import User, TutorProfiles, GuardianProfiles
from django.views.generic import CreateView, ListView
from ..forms import TutorSignUpForm, CreateTutorProfile


class TutorSignUpView(CreateView):
    model = User
    form_class = TutorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Tutor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tutor:tutor_homepage')


# @method_decorator([login_required, guardian_required], name='dispatch')
@login_required()
@tutor_required()
def TutorHomepage(request):
    filters = GuardianFilter(request.GET, queryset=GuardianProfiles.objects.all())
    return render(request, 'hireapp/tutor/search_guardian.html', {'filters': filters})


@method_decorator([login_required, tutor_required], name='dispatch')
class TutorProfile(CreateView):
    model = TutorProfiles
    form_class = CreateTutorProfile

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('tutor:tutor_homepage')
