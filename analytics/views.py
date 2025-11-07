from django.shortcuts import render, redirect
from pathlib import Path
from .parsing import parse_sber_html
from . import forms


def main_view(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    return render(request, 'main_page.html')


def add_document_view(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    if request.method == 'POST':
        form = forms.UserReport(request.POST, request.FILES)
        if form.is_valid():
            uploaded_files = request.FILES.getlist('file')

            if not uploaded_files:
                return render(request, 'add_document.html', {'form': form})

            for uploaded_file in uploaded_files:
                fn = Path(uploaded_file.name)

                if fn.suffix.lower() != '.html':
                    continue

                parse_sber_html(uploaded_file, request.user)

            return redirect('analytics:main')
        else:
            print("Форма невалидна:", form.errors)
    else:
        form = forms.UserReport()

    return render(request, 'add_document.html', {'form': form})
