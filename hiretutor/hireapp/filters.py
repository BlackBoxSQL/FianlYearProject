import django_filters

from .models import TutorProfiles, GuardianProfiles


class TutorFilter(django_filters.FilterSet):
    tution_you_give_to_class = django_filters.CharFilter(lookup_expr='exact', label='Search by class')
    fees_per_subject = django_filters.CharFilter(lookup_expr='exact', label='Search by tuition fees')
    address = django_filters.CharFilter(lookup_expr='icontains', label='Search by address')
    subjects_you_teach = django_filters.CharFilter(lookup_expr='icontains', label='Search by subject')
    class Meta:
        model = TutorProfiles
        fields = ['tution_you_give_to_class',
                  'fees_per_subject',
                  'subjects_you_teach',
                  'address',
        ]

class GuardianFilter(django_filters.FilterSet):
    subject = django_filters.CharFilter(lookup_expr='icontains', label='Search by subject')
    s_class = django_filters.CharFilter(lookup_expr='exact', label="Search by student's class")
    payment = django_filters.CharFilter(lookup_expr='exact', label='Search by payment')
    gender = django_filters.CharFilter(lookup_expr='exact', label='Search by gender')

    class Meta:
        model = GuardianProfiles
        fields = [
            'subject',
            's_class',
            'payment',
            'gender',
        ]