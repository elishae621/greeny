from main.models import Greeny

class AddGreenyToAllContext:
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
        return response


class AddTotalCartAmountToAllContext:
    def __init__(self, get_response):
        self.get_response = get_response 
        
    def __call__(self, request):
        return self.get_response(request)
    
    def process_template_response(self, request, response):
        total = 0
        if self.request.user.is_authenticated:
            for item in self.request.user.cart.all():
                total += item.variant.price
        response.context_data["total"] = total
        return response