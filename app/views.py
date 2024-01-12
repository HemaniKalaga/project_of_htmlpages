from django.shortcuts import render

# Create your views here.
def internal(request):
    return render(request,'internal.html')

def HtmlLoginForm(request):
    return render(request,'HtmlLoginForm.html')

def anchortag(request):
    return render(request,'anchortag.html')

def bootstrap_grid(request):
    return render(request,'bootstrap_grid.html')

def InlineExternal(request):
    return render(request,'InlineExternal.html')

def selectors(request):
    return render(request,'selectors.html')

def table(request):
    return render(request,'table.html')

def css1(request):
    return render(request,'css1.css')

def PrimeAndComposite(request):
    return render(request,'PrimeAndComposite.html')

def perfect(request):
    return render(request,'perfect.html')

def booking(request):
    return render(request,'booking.html')

