from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from .models import Rockets_bdf
from .serializers import bdfSerializer



def home(request):
    return render(request, 'home.html')


@api_view(["GET", "POST"])
def bdf_list(request):
    if request.method == "GET":
        bdf = Rockets_bdf.objects.all()
        serializer = bdfSerializer(bdf, many = True)
        return Response(serializer.data)
    
    if request.method == "POST":
        text = request.data.get("text")
        start_rocket = request.data.get("start_rocket")
        t = request.data.get("t")
        d0 = request.data.get("d0")
        tol_R = request.data.get("tol_R")
        L = request.data.get("L")
        d0_Kon = request.data.get("d0_Kon")
        tol_Kon = request.data.get("tol_Kon")
        L_Kon = request.data.get("L_Kon")
        kolichestvo_amort = request.data.get("kolichestvo_amort")
        zhestkost_amort = request.data.get("zhestkost_amort")
        X1 = request.data.get("X1")
        X2 = request.data.get("X2")
        X3 = request.data.get("X3")
        X4 = request.data.get("X4")
        X5 = request.data.get("X5")
        bd = Rockets_bdf.objects.create(text=text, start_rocket=start_rocket, t=t, d0=d0, tol_R=tol_R, L=L, d0_Kon=d0_Kon, tol_Kon=tol_Kon, L_Kon=L_Kon, kolichestvo_amort=kolichestvo_amort, zhestkost_amort=zhestkost_amort, X1=X1, X2=X2, X3=X3, X4=X4, X5=X5)
        serializer = bdfSerializer(bd)
        return Response(serializer.data, status=HTTP_200_OK)


