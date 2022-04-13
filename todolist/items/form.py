
from django.forms import ModelForm
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description']
    # title = forms.CharField(max_length=20)
    # content = forms.CharField(max_length=255)