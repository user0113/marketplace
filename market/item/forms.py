from django import forms

from .models import Item

fieldStyling = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': fieldStyling
            }),
            'name': forms.TextInput(attrs={
                'class': fieldStyling
            }),
            'description': forms.Textarea(attrs={
                'class': fieldStyling
            }),
            'price': forms.TextInput(attrs={
                'class': fieldStyling
            }),
            'image': forms.FileInput(attrs={
                'class': fieldStyling
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': fieldStyling
            }),
            'description': forms.Textarea(attrs={
                'class': fieldStyling
            }),
            'price': forms.TextInput(attrs={
                'class': fieldStyling
            }),
            'image': forms.FileInput(attrs={
                'class': fieldStyling
            })
        }