from __future__ import unicode_literals

from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response



class ExportMixin(object):
    """
    Download a rendered serialized response.
    """

    def download(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        queryset = self.paginate_queryset(qs) or qs
        serializer = self.get_serializer(queryset, many=True)

        filename = getattr(self, 'filename', self.get_view_name())
        extension = self.get_content_negotiator().select_renderer(
            request, self.renderer_classes
        )[0].format

        return Response(
            data=serializer.data, status=HTTP_200_OK,
            headers={
                'content-disposition': (
                    'attachment; filename="{}.{}"'.format(filename, extension)
                )
            }
        )