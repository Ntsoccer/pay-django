from django.shortcuts import render, redirect
from django.conf import settings
from django.views import generic
from .models import Book, BuyingHistory

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexView(generic.ListView):
    model = Book


class DetailView(generic.DetailView):
    model = Book

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(
                amount=book.price,
                currency='jpy',
                source=token,
                description='メール：{} 書籍名：{}'.format(
                    request.user.email, book.title),
            )
        except stripe.error.CardError as e:
            context = self.get_context_data()
            context['message'] = 'Your payment cannot be completed The card has been declined'
            return render(request, 'payapp/book_detail.html', context)
        else:
            BuyingHistory.objects.create(
                book=book, user=request.user, stripe_id=charge.id)
            return redirect('payapp:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publick_key'] = settings.STRIPE_PUBLIC_KEY
        return context
