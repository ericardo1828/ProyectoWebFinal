from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("home")
    return render(request,'ProyectoWebApp/home.html')

def servicios(request):
    #return HttpResponse("servicios")
    return render(request,'ProyectoWebApp/servicios.html')

def tienda(request):
    #return HttpResponse("tienda")
    return render(request,'ProyectoWebApp/tienda.html')

def blog(request):
    #return HttpResponse("blog")
    return render(request,'ProyectoWebApp/blog.html')

def contacto(request):
    #return HttpResponse("contacto")
    return render(request,'ProyectoWebApp/contacto.html')
