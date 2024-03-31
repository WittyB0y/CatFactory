from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from Company.filter import CustomCompanyFilter
from Company.models import Company
from Company.serializer import CompanyObjectsSerializer


class CompanyObjectsViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyObjectsSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filterset_class = CustomCompanyFilter
    filter_backends = [DjangoFilterBackend, ]

    def get_queryset(self):
        """
        get objs where user = staff_id in Company table,
        if user is superuser, returns all objects.
        """
        user = self.request.user
        if user.is_superuser:
            return self.queryset
        return self.queryset.filter(staff_id=user)
