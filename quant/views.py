from django.shortcuts import render

from quant.models import Ticker
from quant.serializers import TickerSerializer

from rest_framework import mixins
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

def index(request):
    ticker_list = Ticker.objects.all()
    output = ', '.join([q.code for q in ticker_list])
    context = {
        'ticker_list': output,
    }
    return render(request, 'index.html', context)

def detail(request, question_id):
    return HttpResponse('youre looking at question {}'.format(question_id))

class TickerList(generics.ListCreateAPIView):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = Ticker.objects.all()
        code_by = self.request.GET.get('code')
        if code_by:
            queryset = queryset.filter(code=code_by)
        return queryset
    
# class TickerDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Ticker.objects.all()
#     serializer_class = TickerSerializer

class TickerDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer

    def get(self, request, *args, **kwargs):
        print(request.query_params)
        return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)