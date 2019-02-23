from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from ..filters import TutorFilter
from ..decorators import guardian_required
from ..models import User, GuardianProfiles, TutorProfiles
from django.views.generic import CreateView, ListView
from ..forms import GuardianSignUpForm, CreateGuardianProfile


class GuardianSignUpView(CreateView):
    model = User
    form_class = GuardianSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Guardian'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('guardian:guardian_homepage')


# @method_decorator([login_required, guardian_required], name='dispatch')
@login_required()
@guardian_required()
def GuardianHomepage(request):
    filter = TutorFilter(request.GET, queryset=TutorProfiles.objects.all())
    return render(request, 'hireapp/guardian/search_tutor.html', {'filter': filter})


@method_decorator([login_required, guardian_required], name='dispatch')
class GuardianProfile(CreateView):
    model = GuardianProfiles
    form_class = CreateGuardianProfile

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('guardian:guardian_homepage')
