import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def root(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryListCreateView(View):
    def get(self, request):
        all_categories = Category.object.all
        return JsonResponse([cat.serialize() for cat in all_categories], safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_categopy = Category.objects.create(**data)
        return JsonResponse(new_categopy.serialize())


@method_decorator(csrf_exempt, name="dispatch")
class AdListCreateView(View):
    def get(self, request):
        all_ads = Ad.object.all
        return JsonResponse([ad.serialize() for ad in all_ads], safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(**data)
        return JsonResponse(new_ad.serialize())


class AdDitailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.get_object().serialize())


class CategoryDitailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.get_object().serialize())
