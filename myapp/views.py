from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, PublisherForm, SearchForm
from .models import Author, Book, Publisher

def index(req):
    return render(req, 'index.html',{})

def add_data(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        book_form = BookForm(request.POST)
        publisher_form = PublisherForm(request.POST)

        if author_form.is_valid() and book_form.is_valid() and publisher_form.is_valid():
            # Obtener el nombre del autor desde el formulario de libro
            author_name = book_form.cleaned_data['author_name']
            author_email = author_form.cleaned_data['email']

            author, created = Author.objects.get_or_create(name=author_name, defaults={'email': author_email})
            if not created:
                author.email = author_email
                author.save()

            # Buscar o crear el autor basado en el nombre proporcionado
            author, created = Author.objects.get_or_create(name=author_name)

            # Guardar el libro con el autor correspondiente
            book_title = book_form.cleaned_data['title']
            book, created = Book.objects.get_or_create(title=book_title, author=author)

            # Guardar editorial y asociar el libro
            publisher = publisher_form.save(commit=False)
            publisher.save()
            publisher.books.add(book)
            publisher.save()

            return redirect('index')
    else:
        author_form = AuthorForm()
        book_form = BookForm()
        publisher_form = PublisherForm()

    return render(request, 'add_data.html', {
        'author_form': author_form,
        'book_form': book_form,
        'publisher_form': publisher_form,
    })



def search_data(request):
    results = None
    all_books = Book.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            titulo_del_libro = form.cleaned_data['titulo_del_libro']
            results = Book.objects.filter(title__icontains=titulo_del_libro)
    else:
        form = SearchForm()
    return render(request, 'search_data.html', {'form': form, 'results': results, 'books': all_books})

