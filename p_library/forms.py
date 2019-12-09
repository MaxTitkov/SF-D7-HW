from django import forms  
from p_library.models import Author, Book, Rent, UserProfile
from django.forms import formset_factory
  
class AuthorForm(forms.ModelForm):  
  
    full_name = forms.CharField(widget=forms.TextInput)  
  
    class Meta:  
        model = Author  
        fields = '__all__'  
  
  
class BookForm(forms.ModelForm):  
    class Meta:  
        model = Book  
        fields = '__all__'


class RentForm(forms.ModelForm): 
    class Meta:  
        model = Rent  
        fields = '__all__'


class ProfileCreationForm(forms.ModelForm):  
  
    class Meta:  
        model = UserProfile  
        fields = ['age']