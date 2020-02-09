from django.shortcuts import render
from django.views import View
from core.models import Index
from products.models import Product
from feedback.forms import FeedBackForm
from orders.forms import OrderForm
from news.models import News
from contacts.models import *


class IndexView(View):
    def get(self, request):
        index = Index.objects.first()
        first_slide = index.slides.first()

        products = Product.objects.filter(is_active=True)[:3]

        order_form = OrderForm()
        feedback_form = FeedBackForm()

        news = News.objects.filter(is_active=True)[:4]

        addresses = Address.objects.all()
        phones = Phone.objects.all()
        emails = Email.objects.all()
        map_code = MapCode.objects.first()

        context = {
            'index': index,
            'first_slide': first_slide,
            'products': products,
            'order_form': order_form,
            'feedback_form': feedback_form,
            'news': news,
            'addresses': addresses,
            'phones': phones,
            'emails': emails,
            'map_code': map_code,
        }

        return render(request, 'core/index.html', context)
