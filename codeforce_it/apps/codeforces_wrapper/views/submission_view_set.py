from rest_framework import viewsets

from codeforce_it.apps.codeforces_wrapper.models import Submission
from codeforce_it.apps.codeforces_wrapper.serializers import SubmissionSerializer


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
