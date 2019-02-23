import django_filters
from .models import TutorProfiles, GuardianProfiles


class TutorFilter(django_filters.FilterSet):
    tution_you_give_to_class = django_filters.CharFilter(lookup_expr='exact', label='Search by class')
    fees_per_subject = django_filters.CharFilter(lookup_expr='exact', label='Search by fees per subject')
    subjects_you_teach = django_filters.CharFilter(lookup_expr='icontains', label='Search by subjects')
    address = django_filters.CharFilter(lookup_expr='icontains', label='Search by address')

    class Meta:
        model = TutorProfiles
        fields = [
            'tution_you_give_to_class',
            'fees_per_subject',
            'subjects_you_teach',
            'address',
        ]


class GuardianFilter(django_filters.FilterSet):
    s_class = django_filters.CharFilter(lookup_expr='exact', label='Search by class')
    subject = django_filters.CharFilter(lookup_expr='icontains', label='Search by subject')
    payment = django_filters.CharFilter(lookup_expr='exact', label='Search by payment')
    address = django_filters.CharFilter(lookup_expr='icontains', label='Search by address')

    class Meta:
        model = GuardianProfiles
        fields = [
            's_class',
            'subject',
            'payment',
            'address',
        ]
