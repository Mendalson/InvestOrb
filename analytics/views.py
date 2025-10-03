from django.shortcuts import render, redirect
from .parsing import parsing_sber_document


def main_view(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    return render(request, 'main_page.html')


def add_document_view(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    if request.method == 'POST':
        parsing_sber_document(request.files)
        return redirect('analytics:main')
    return render(request, 'add_document.html')
