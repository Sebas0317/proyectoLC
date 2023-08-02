from django.shortcuts import render, HttpResponse

def home(request):
        return render(request, "core/home.html")

def productdetail(request):
        return render(request, "core/product-detail.html")

def productlist(request):
        return render(request, "core/product-list.html")

def checkout(request):
        return render(request, "core/checkout.html")
def myaccount(request):
        return render(request, "core/my-account.html")
def wishlist(request):
        return render(request, "core/wishlist.html")
def contact(request):
        return render(request, "core/contact.html")
def admin(request):
        return render(request, "core/admin.html")
def regis(request):
        return render(request, "core/regis.html")
