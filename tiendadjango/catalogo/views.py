from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, Comment
from django.views import generic

# Create your views here.
# def index(request):
#     latest_product_list = Product.objects.all()
#     return render(request, 'catalogo/index.html', {
#         'latest_product_list': latest_product_list
#     })

def detail(request, prod_id):
    prod = get_object_or_404(Product, pk=prod_id)
    response = render(request, 'catalogo/detail.html', {
        "producto": prod
    })
    return response


def insert_comment(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == 'POST':
        prod_rating = request.POST.get('rating', None)
        prod_num = request.POST.get('num_serie', None)
        user_mail = request.POST.get('mail', None)
        txt_comment = request.POST.get('comment', None)
        
        comment = Comment(prod_rating=prod_rating, prod_num=prod_num, user_mail=user_mail, text_comment=txt_comment)
        if comment.save():
            return JsonResponse({"comment": "Success"}, status = 200)
        else:
            return JsonResponse({"comment": "Fail"}, status = 200)
            
        

class IndexView(generic.ListView):
    template_name = 'catalogo/index.html'
    context_object_name = "latest_product_list"
    
    def get_queryset(self):
        return Product.objects.order_by("-pub_date")[:6]
