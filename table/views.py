#!/usr/bin/env python
# coding: utf-8

from django import http
from django.utils import simplejson as json
from django.views.generic import BaseListView

class FeedDataView(JSONResponseMixin, BaseListView):
    def get_queryset(self):
        # for search
        # self.publisher = get_object_or_404(Publisher, name__iexact=self.args[0])
        # return Book.objects.filter(publisher=self.publisher)

class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)
