from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet

from . import mixins

class ImportExportModelViewSet(mixins.ExportMixin, ModelViewSet):
    pass