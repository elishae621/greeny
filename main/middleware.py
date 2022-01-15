from main.models import Greeny, Category, Product

class AddToAllContext:
    def __init__(self, get_response):
        self.get_response = get_response
        if len(Greeny.objects.all()) != 1:
            Greeny.objects.all().delete()
            Greeny.objects.create()
        self.greeny = Greeny.objects.values()[0]

    def __call__(self, request):
        return self.get_response(request)

    def process_template_response(self, request, response):
        response.context_data['greeny'] = self.greeny
        response.context_data['categories'] = Category.objects.all()
        response.context_data['products'] = Product.objects.all()
        total = 0
        if request.user.is_authenticated:
            for item in request.user.cart.all():
                total += item.variant.price
        response.context_data["total"] = round(total, 2)
        return response

