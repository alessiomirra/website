from django import forms 
from cars.models import Car, CompanyInfo

#### 

class NewCarForm(forms.ModelForm):
    class Meta:
        model = Car 
        fields = ["make","model","version","price","year","gear","fuel","mileage","power","optionals","description","miniature","slug","showcase"]
        widgets = {
            'make': forms.TextInput(attrs={'class':'form-control'}), 
            'model': forms.TextInput(attrs={'class':'form-control'}), 
            'version': forms.TextInput(attrs={'class':'form-control'}), 
            'price': forms.TextInput(attrs={'class':'form-control'}), 
            'year': forms.TextInput(attrs={'class':'form-control'}), 
            'gear': forms.TextInput(attrs={'class':'form-control'}), 
            'fuel': forms.TextInput(attrs={'class':'form-control'}), 
            'mileage': forms.TextInput(attrs={'class':'form-control'}), 
            'power': forms.TextInput(attrs={'class':'form-control'}), 
            'optionals': forms.Textarea(attrs={'class':'form-control', 'rows':2}), 
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':3}), 
            'slug': forms.TextInput(attrs={'class':'form-control'}), 
            'miniature': forms.FileInput(attrs={'class':'form-control'}), 
            'showcase': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }


class InfoesUpdate(forms.ModelForm):
    class Meta:
        model = CompanyInfo 
        fields = ["address","phoneNumber","email","idCode"]
        widgets = {
            "address": forms.TextInput(attrs={'class':'form-control'}),
            "phoneNumber": forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.TextInput(attrs={'class':'form-control'}),
            "idCode": forms.TextInput(attrs={'class':'form-control'})
        }