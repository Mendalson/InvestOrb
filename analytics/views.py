from django.shortcuts import render, redirect


# Create your views here.
def main_view(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    return render(request, 'main_page.html')
