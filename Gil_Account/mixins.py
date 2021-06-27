from django.shortcuts import get_object_or_404, redirect
from django.http import Http404

class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = [
            "name_fa","name_en", "slug", "year",
            "price","discount","description","image",
            "image1","image2","image3","image4","active",
            "categories","brands","attributes"
        ]
        return super().dispatch(request, *args, **kwargs)


class AdminAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_admin:
                return super().dispatch(request, *args, **kwargs)
            else:
                raise Http404("You can't see this page.")
        else:
            return redirect("account:login")
