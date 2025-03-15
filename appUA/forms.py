from django import forms
import re

'''
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(widget=forms.Textarea, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Simulación de restricción (solo correos con .com, .net, sin dominios internacionales)
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|net)$', email):
            raise forms.ValidationError("❌ Solo se permiten correos con dominios '.com' o '.net'.")
        return email
'''    
    
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Asunto'}))
    message = forms.CharField(widget=forms.Textarea(), required=True)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Expresión regular para permitir solo caracteres latinos básicos (sin acentos)
        if not re.match(r'^[a-zA-Z\s]+$', name):
            raise forms.ValidationError("❌ Sólo se permiten letras sin acentos ni caracteres especiales.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Solo permite dominios con ".com" y '.org' y '.edu' y ".net"
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|net|org|edu)$', email):
            raise forms.ValidationError("❌ Sólo se permiten correos sin acentos ni caracteres especiales y con dominios '.com' o '.net' o '.org' o '.edu'.")
        return email