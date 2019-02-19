import django_filters

from .models import TutorProfiles


class TutorFilter(django_filters.FilterSet):

    class Meta:
        model = TutorProfiles
        fields = ('tution_you_give_to_class',
                  'fees_per_subject',
                  'subjects_you_teach',
                  'address',
                  )