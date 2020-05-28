from django.shortcuts import render

from quant.models import Ticker, MonitorStock, MinOHLCV, UserState, PortHistory
from quant.permissions import IsOwnerOrReadOnly
from quant.serializers import (
    TickerSerializer,
    MonitorStockSerializer,
    MinOHLCVSerializer,
    UserStateSerializer,
    PortHistorySerializer,
)

from rest_framework import mixins, status
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

class MonitorStockList(generics.ListCreateAPIView):
    queryset = MonitorStock.objects.all()
    serializer_class = MonitorStockSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = (IsAuthenticated,)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    def get_queryset(self, *args, **kwargs):
        queryset = MonitorStock.objects.all()
        user_by = self.request.GET.get('user')
        date_by = self.request.GET.get('date')
        if user_by:
            queryset = queryset.filter(user=user_by)
        if date_by:
            queryset = queryset.filter(date=date_by)
        return queryset

class MonitorStockDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = MonitorStock.objects.all()
    serializer_class = MonitorStockSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class MinOHLCVList(generics.ListCreateAPIView):
    queryset = MinOHLCV.objects.all()
    serializer_class = MinOHLCVSerializer
    filter_backends = [SearchFilter, OrderingFilter]

    def create(self, request, *args, **kwargs):
        if request.user.is_staff == True:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'FAILED': 'Cannot POST. Not authorized'}, status=403)

    def get_queryset(self, *args, **kwargs):
        queryset = MinOHLCV.objects.all()
        code_by = self.request.GET.get('code')
        date_by = self.request.GET.get('date')
        if code_by:
            queryset = queryset.filter(code=code_by)
        if date_by:
            queryset = queryset.filter(date=date_by)
        return queryset

class UserStateList(generics.ListCreateAPIView):
    queryset = UserState.objects.all()
    serializer_class = UserStateSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = (IsAuthenticated,)
        
    def get_queryset(self, *args, **kwargs):
        queryset = UserState.objects.all()
        user_by = self.request.GET.get('user')
        date_by = self.request.GET.get('date')
        if user_by:
            queryset = queryset.filter(user=user_by)
        if date_by:
            queryset = queryset.filter(date=date_by)
        return queryset

class UserStateDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserState.objects.all()
    serializer_class = UserStateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

class PortHistoryList(generics.ListCreateAPIView):
    queryset = PortHistory.objects.all()
    serializer_class = PortHistorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = (IsAuthenticated,)
        
    def get_queryset(self, *args, **kwargs):
        queryset = PortHistory.objects.all()
        user_by = self.request.GET.get('user')
        date_by = self.request.GET.get('date')
        if user_by:
            queryset = queryset.filter(user=user_by)
        if date_by:
            queryset = queryset.filter(date=date_by)
        return queryset

class PortHistoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PortHistory.objects.all()
    serializer_class = PortHistorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]