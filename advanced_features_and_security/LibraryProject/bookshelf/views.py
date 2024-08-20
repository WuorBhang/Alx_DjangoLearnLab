from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Document
from .forms import DocumentForm
from django.views.generic import ListView
from .models import Book
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django import forms
from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            description = form.cleaned_data['description']
            # You can save this data to the database or perform other actions
            return render(request, 'success.html', {'title': title})
    else:
        form = ExampleForm()
    
    return render(request, 'example_form.html', {'form': form})


class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=100)

@require_POST
def search_books(request):
    form = BookSearchForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        books = Book.objects.filter(title__icontains=title)
        return render(request, 'books/book_list.html', {'books': books})
    return HttpResponse("Invalid input", status=400)



class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html' 
    context_object_name = 'books'  

    def get_queryset(self):
        return Book.objects.all()  



@permission_required('app_name.can_create', raise_exception=True)
def create_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.created_by = request.user
            document.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'document_form.html', {'form': form})

@permission_required('app_name.can_edit', raise_exception=True)
def edit_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'document_form.html', {'form': form})

@permission_required('app_name.can_delete', raise_exception=True)
def delete_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'document_confirm_delete.html', {'document': document})
