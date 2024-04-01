from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from Company.filter import CustomCompanyFilter
from Company.models import Company
from Celery_tasks.tasks import send_qr_code_to_email
from Company.serializer import CompanyObjectsSerializer, GenerateQRCodeAndSendEmailSerializer


class CompanyObjectsViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyObjectsSerializer
    permission_classes = (permissions.IsAuthenticated,)
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


class GenerateQRCodeAndSendEmail(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = GenerateQRCodeAndSendEmailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, 200)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = request.user.id

        if serializer.is_valid():
            company = get_object_or_404(self.queryset, id=serializer.data.get("id"))
            company_id = company.id
            send_qr_code_to_email.delay(company_id, user)
            return Response("ok", 200)
        raise ValidationError(serializer.errors)
