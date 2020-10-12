from django.shortcuts import render,get_object_or_404
from store.models import TopCategory,AltCategory,Product
# Create your views here.

def mainpage(request):
    topcategories=TopCategory.objects.all()
    altcategories=AltCategory.objects.all()
    products=Product.objects.filter(is_bestseller=True)
    content={"topcategories":topcategories,"altcategories":altcategories,"products":products}
    return render(request,"mainpage.html",content)

def shop(request,category_slug):
    topcategories=TopCategory.objects.all()
    altcategories=AltCategory.objects.all()
    categorys=get_object_or_404(AltCategory,slug=category_slug)
    items=Product.objects.filter(categories=categorys)
    count_item=items.count()

    content={"topcategories":topcategories,"altcategories":altcategories,"categorys":categorys,"items":items,
    "count_item":count_item}

    return render(request,"shop.html",content)
