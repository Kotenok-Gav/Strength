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

        V_sredy = request.data.get("V_sredy")
        t_p0 = request.data.get("t_p0")
        P0 = request.data.get("P0")
        t_p1 = request.data.get("t_p1")
        P1 = request.data.get("P1")
        t_p2 = request.data.get("t_p2")
        P2 = request.data.get("P2")
        t_p3 = request.data.get("t_p3")
        P3 = request.data.get("P3")
        t_p4 = request.data.get("t_p4")
        P4 = request.data.get("P4")
        t_p5 = request.data.get("t_p5")
        P5 = request.data.get("P5")
        t_p6 = request.data.get("t_p6")
        P6 = request.data.get("P6")
        t_p7 = request.data.get("t_p7")
        P7 = request.data.get("P7")
        t_p8 = request.data.get("t_p8")
        P8 = request.data.get("P8")
        t_p9 = request.data.get("t_p9")
        P9 = request.data.get("P9")
        t_p10 = request.data.get("t_p10")
        P10 = request.data.get("P10")
        t_p11 = request.data.get("t_p11")
        P11 = request.data.get("P11")
        t_p12 = request.data.get("t_p12")
        P12 = request.data.get("P12")
        t_p13 = request.data.get("t_p13")
        P13 = request.data.get("P13")

        dl_1 = request.data.get("dl_1")
        nap_zak_1 = request.data.get("nap_zak_1")
        zhestkost_opor_1 = request.data.get("zhestkost_opor_1")

        dl_2 = request.data.get("dl_2")
        nap_zak_2 = request.data.get("nap_zak_2")
        zhestkost_opor_2 = request.data.get("zhestkost_opor_2")

        dl_3 = request.data.get("dl_3")
        nap_zak_3 = request.data.get("nap_zak_3")
        zhestkost_opor_3 = request.data.get("zhestkost_opor_3")

        bd = Rockets_bdf.objects.create(text=text, start_rocket=start_rocket, t=t, d0=d0, tol_R=tol_R, L=L, d0_Kon=d0_Kon, tol_Kon=tol_Kon, L_Kon=L_Kon, kolichestvo_amort=kolichestvo_amort, zhestkost_amort=zhestkost_amort, X1=X1, X2=X2, X3=X3, X4=X4, X5=X5,V_sredy=V_sredy, t_p0=t_p0, P0=P0, t_p1=t_p1, P1=P1, t_p2=t_p2, P2=P2, t_p3=t_p3, P3=P3, t_p4=t_p4, P4=P4, t_p5=t_p5, P5=P5, t_p6=t_p6, P6=P6, t_p7=t_p7, P7=P7, t_p8=t_p8, P8=P8, t_p9=t_p9, P9=P9, t_p10=t_p10, P10=P10, t_p11=t_p11, P11=P11, t_p12=t_p12, P12=P12, t_p13=t_p13, P13=P13, dl_1=dl_1, nap_zak_1=nap_zak_1, zhestkost_opor_1=zhestkost_opor_1, dl_2=dl_2, nap_zak_2=nap_zak_2, zhestkost_opor_2=zhestkost_opor_2, dl_3=dl_3, nap_zak_3=nap_zak_3, zhestkost_opor_3=zhestkost_opor_3)
        serializer = bdfSerializer(bd)
        return Response(serializer.data, status=HTTP_200_OK)


