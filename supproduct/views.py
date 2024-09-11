from django.shortcuts import render
from supproduct.models import Suppro
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    products=Suppro.objects.filter(isTrending=True)
    return render(request,"index.html",{"products":products})

def supproductDetail(request,id):
    product=Suppro.objects.get(pk=id)
    return render(request,"detail.html",{"product":product})

def supproducts(request):
    all_products=Suppro.objects.all().order_by("name")
    #กำหนดหมายเลขหน้า
    page = request.GET.get("page")
    paginator=Paginator(all_products,3)
    all_products=paginator.get_page(page)
    return render(request,"products.html",{"all_products":all_products})