import django_filters

from .models import TutorProfiles


class TutorFilter(django_filters.FilterSet):
    address = django_filters.CharFilter(field_name='search_by', lookup_expr='icontains')

    class Meta:
        model = TutorProfiles
        fields = ['tution_you_give_to_class',
                  'fees_per_subject',
                  'subjects_you_teach',
                  ]
