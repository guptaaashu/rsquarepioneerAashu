from popup_field.views import PopupCRUDViewSet

from .models import *


class RouteForm(forms.ModelForm):
class Meta:
model = Route
fields = "__all__"




class RoutePopupCRUDViewSet(PopupCRUDViewSet):
model = Route
form_class = RouteForm
template_name_create = 'popup/create.html'
template_name_update = 'popup/update.html'
