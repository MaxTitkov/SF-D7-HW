from allauth.socialaccount.models import SocialAccount
from django.contrib import auth    
from django.contrib.auth import login, authenticate  
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import formset_factory  
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, FormView  
from p_library.forms import AuthorForm, BookForm, RentForm, ProfileCreationForm 
from p_library.models import Book, Author, Redaction, Friend, Rent


class RegisterView(FormView):  
  
    form_class = UserCreationForm  
  
    def form_valid(self, form):  
        form.save()  
        username = form.cleaned_data.get('username')  
        raw_password = form.cleaned_data.get('password1')  
        login(self.request, authenticate(username=username, password=raw_password))  
        return super(RegisterView, self).form_valid(form)  
  
  
class CreateUserProfile(FormView):  
  
    form_class = ProfileCreationForm  
    template_name = 'profile-create.html'  
    success_url = reverse_lazy('p_library:index')  
  
    def dispatch(self, request, *args, **kwargs):  
        if self.request.user.is_anonymous:  
            return HttpResponseRedirect(reverse_lazy('p_library:login'))  
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)  
  
    def form_valid(self, form):  
        instance = form.save(commit=False)  
        instance.user = self.request.user  
        instance.save()  
        return super(CreateUserProfile, self).form_valid(form)


class Oauth(): 
    def index(request):  
        context = {}  
        if request.user.is_authenticated:  
            context['username'] = request.user.username  
        return render(request, 'oauth_index.html', context)  
      
      
def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    
    # 
    rbooks = Rent.objects.all()
    for book in books:
        can_give = book.copy_count
        for rbook in rbooks:
            if rbook.book.title == book.title and rbook.num > 0:
                can_give -= rbook.num
        book.can_be_borrowed = can_give
        book.save()

    # 

    biblio_data = {
        "title": "нашу библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

# ------------------------------------------------------------

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def redactions(request):
    template = loader.get_template('redactions.html')
    redactions = Redaction.objects.all()
    data = {
        "redactions": redactions,
    }
    return HttpResponse(template.render(data, request))

# ------------------------------------------------------------

class AuthorEdit(CreateView):  
    model = Author  
    form_class = AuthorForm  
    success_url = reverse_lazy('author_list')  
    template_name = 'author_edit.html'  
  
  
class AuthorList(ListView):  
    model = Author  
    template_name = 'author_list.html'

# ------------------------------------------------------------

def author_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  #  Первым делом, получим класс, который будет создавать наши формы. Обратите внимание на параметр `extra`, в данном случае он равен двум, это значит, что на странице с несколькими формами изначально будет появляться 2 формы создания авторов.
    if request.method == 'POST':  #  Наш обработчик будет обрабатывать и GET и POST запросы. POST запрос будет содержать в себе уже заполненные данные формы
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  #  Здесь мы заполняем формы формсета теми данными, которые пришли в запросе. Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм, но и разных формсетов, этот параметр позволяет их отличать в запросе.
        if author_formset.is_valid():  #  Проверяем, валидны ли данные формы
            for author_form in author_formset:  
                author_form.save()  #  Сохраним каждую форму в формсете
            return HttpResponseRedirect(reverse_lazy('author_list'))  #  После чего, переадресуем браузер на список всех авторов.
    else:  #  Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        author_formset = AuthorFormSet(prefix='authors')  #  Инициализируем формсет и ниже передаём его в контекст шаблона.
    return render(request, 'manage_authors.html', {'author_formset': author_formset})


def books_authors_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  
    BookFormSet = formset_factory(BookForm, extra=2)  
    if request.method == 'POST':  
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')  
        if author_formset.is_valid() and book_formset.is_valid():  
            for author_form in author_formset:  
                author_form.save()  
            for book_form in book_formset:  
                book_form.save()  
            return HttpResponseRedirect(reverse_lazy('author_list'))  
    else:  
        author_formset = AuthorFormSet(prefix='authors')  
        book_formset = BookFormSet(prefix='books')  
    return render(
        request,  
        'manage_books_authors.html',  
        {  
            'author_formset': author_formset,  
            'book_formset': book_formset,  
        }  
    )

# ------------------------------------------------------------

class RentEdit(CreateView):  
    model = Rent  
    form_class = RentForm  
    success_url = reverse_lazy('rent_list')  
    template_name = 'rent_edit.html'  
  
  
class RentList(ListView):  
    model = Rent  
    template_name = 'rent_list.html'

# ------------------------------------------------------------
def rent_create_many(request):  
    RentFormSet = formset_factory(RentForm, extra=2)  #  Первым делом, получим класс, который будет создавать наши формы. Обратите внимание на параметр `extra`, в данном случае он равен двум, это значит, что на странице с несколькими формами изначально будет появляться 2 формы создания авторов.
    if request.method == 'POST':  #  Наш обработчик будет обрабатывать и GET и POST запросы. POST запрос будет содержать в себе уже заполненные данные формы
        rent_formset = RentFormSet(request.POST, request.FILES, prefix='rents')  #  Здесь мы заполняем формы формсета теми данными, которые пришли в запросе. Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм, но и разных формсетов, этот параметр позволяет их отличать в запросе.
        if rent_formset.is_valid():  #  Проверяем, валидны ли данные формы
            for rent_form in rent_formset:  
                rent_form.save()  #  Сохраним каждую форму в формсете
            return HttpResponseRedirect(reverse_lazy('rent_list'))  #  После чего, переадресуем браузер на список всех авторов.
    else:  #  Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        rent_formset = RentFormSet(prefix='rents')  #  Инициализируем формсет и ниже передаём его в контекст шаблона.
    return render(request, 'manage_rents.html', {'rent_formset': rent_formset})
