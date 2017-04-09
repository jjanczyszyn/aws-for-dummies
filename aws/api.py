from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Image
from .serializers import ImageSerializer
from .views import get_signed_upload_url


@api_view(['GET'])
def generate_signed_upload_url(request):
    return Response(get_signed_upload_url())


class ImageViewSet(ListModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [AllowAny]

    def filter_queryset(self, queryset):
        if self.action == 'list':
            return queryset.filter(url__isnull=False)
        return queryset
