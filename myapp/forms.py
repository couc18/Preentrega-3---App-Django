from django import forms
from .models import Author, Book, Publisher

class AuthorForm(forms.ModelForm):
    name = forms.CharField(label="Nombre:")
    email= forms.CharField(label="Email")

    class Meta:
        model = Author
        fields = ['name', 'email']
        labels = {
            'name': 'Nombre del autor:',
            'email':'Email del autor:'
        }

class BookForm(forms.ModelForm):
    author_name = forms.CharField(label="Nombre del autor:", max_length= 100)
    
    class Meta:
        model = Book
        fields = ['title']
        labels = {
            'title': 'Titulo del libro:'
        }

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']
        labels = {
        'name': 'Editorial:',
        }
        

class SearchForm(forms.Form):
    titulo_del_libro = forms.CharField(max_length=100)

