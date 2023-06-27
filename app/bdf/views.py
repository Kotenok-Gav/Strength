from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from .models import Rockets_bdf
from .serializers import bdfSerializer
from decimal import Decimal
from django.http import FileResponse
from django.conf import settings
from django.views import View
import os
from django.http import FileResponse
from rest_framework.views import APIView


def home(request):
    return render(request, "home.html")


@api_view(["GET", "POST"])
def bdf_list(request):
    if request.method == "GET":
        bdf = Rockets_bdf.objects.all()
        serializer = bdfSerializer(bdf, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        # 1 ------------
        text = request.data.get("text")
        start_rocket = request.data.get("start_rocket")
        t = request.data.get("t")
        # 2 ------------
        d0 = request.data.get("d0")
        tol_R = request.data.get("tol_R")
        L = request.data.get("L")
        d0_Kon = request.data.get("d0_Kon")
        tol_Kon = request.data.get("tol_Kon")
        L_Kon = request.data.get("L_Kon")
        # 3 ------------
        kolichestvo_amort = request.data.get("kolichestvo_amort")
        zhestkost_amort = request.data.get("zhestkost_amort")
        X1 = request.data.get("X1")
        X2 = request.data.get("X2")
        X3 = request.data.get("X3")
        X4 = request.data.get("X4")
        X5 = request.data.get("X5")
        # 4 ------------
        V_sredy = request.data.get("V_sredy")
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
        # 5 ------------
        m = request.data.get("m")
        m_gch = request.data.get("m_gch")
        X_gch = request.data.get("X_gch")
        m_cy = request.data.get("m_cy")
        X_cy = request.data.get("X_cy")
        m_dy_1 = request.data.get("m_dy_1")
        X_dy_1 = request.data.get("X_dy_1")
        mo_1 = request.data.get("mo_1")
        Lo_1 = request.data.get("Lo_1")
        Xo_1 = request.data.get("Xo_1")
        mg_1 = request.data.get("mg_1")
        Lg_1 = request.data.get("Lg_1")
        Xg_1 = request.data.get("Xg_1")

        L_kon_zakr_1 = request.data.get("L_kon_zakr_1")
        tip_zakr_1 = request.data.get("tip_zakr_1")

        L_kon_zakr_2 = request.data.get("L_kon_zakr_2")
        tip_zakr_2 = request.data.get("tip_zakr_2")

        L_kon_zakr_3 = request.data.get("L_kon_zakr_3")
        tip_zakr_3 = request.data.get("tip_zakr_3")

        L_kon_zakr_4 = request.data.get("L_kon_zakr_4")
        tip_zakr_4 = request.data.get("tip_zakr_4")

        L_kon_zakr_5 = request.data.get("L_kon_zakr_5")
        tip_zakr_5 = request.data.get("tip_zakr_5")

        # 6 ------------
        modul_unga1 = request.data.get("modul_unga1")
        koeff_puass1 = request.data.get("koeff_puass1")
        modul_unga2 = request.data.get("modul_unga2")
        koeff_puass2 = request.data.get("koeff_puass2")
        plotnost2 = request.data.get("plotnost2")

        # -----------------------------------------------------------------------
        bd = Rockets_bdf.objects.create(
            # 1 ------------
            text=text,
            start_rocket=start_rocket,
            t=t,
            # 2 ------------
            d0=d0,
            tol_R=tol_R,
            L=L,
            d0_Kon=d0_Kon,
            tol_Kon=tol_Kon,
            L_Kon=L_Kon,
            # 3 ------------
            kolichestvo_amort=kolichestvo_amort,
            zhestkost_amort=zhestkost_amort,
            X1=X1,
            X2=X2,
            X3=X3,
            X4=X4,
            X5=X5,
            # 4 ------------
            V_sredy=V_sredy,
            t_p1=t_p1,
            P1=P1,
            t_p2=t_p2,
            P2=P2,
            t_p3=t_p3,
            P3=P3,
            t_p4=t_p4,
            P4=P4,
            t_p5=t_p5,
            P5=P5,
            t_p6=t_p6,
            P6=P6,
            t_p7=t_p7,
            P7=P7,
            t_p8=t_p8,
            P8=P8,
            t_p9=t_p9,
            P9=P9,
            t_p10=t_p10,
            P10=P10,
            t_p11=t_p11,
            P11=P11,
            t_p12=t_p12,
            P12=P12,
            t_p13=t_p13,
            P13=P13,
            # 5 ------------
            m=m,
            m_gch=m_gch,
            X_gch=X_gch,
            m_cy=m_cy,
            X_cy=X_cy,
            m_dy_1=m_dy_1,
            X_dy_1=X_dy_1,
            mo_1=mo_1,
            Lo_1=Lo_1,
            Xo_1=Xo_1,
            mg_1=mg_1,
            Lg_1=Lg_1,
            Xg_1=Xg_1,
            L_kon_zakr_1=L_kon_zakr_1,
            tip_zakr_1=tip_zakr_1,
            L_kon_zakr_2=L_kon_zakr_2,
            tip_zakr_2=tip_zakr_2,
            L_kon_zakr_3=L_kon_zakr_3,
            tip_zakr_3=tip_zakr_3,
            L_kon_zakr_4=L_kon_zakr_4,
            tip_zakr_4=tip_zakr_4,
            L_kon_zakr_5=L_kon_zakr_5,
            tip_zakr_5=tip_zakr_5,
            # 6 ------------
            modul_unga1=modul_unga1,
            koeff_puass1=koeff_puass1,
            modul_unga2=modul_unga2,
            koeff_puass2=koeff_puass2,
            plotnost2=plotnost2,
        )

#-------Начало формирования BDF файла---------------------------------------------------------

        file = open("1.txt", "w")

        file.write("NASTRAN SYSTEM(151)=1\nNASTRAN BUFFSIZE=65537\n\nID START\nTIME	300\nSOL	129\nDIAG	8,50\nCEND\necho=both\n\n")

        file.write("DISPLACEMENT(SORT1,REAL)	= all\nSPCFORCES(SORT1, REAL) = all\nFORCE(SORT1, REAL, BILIN) = all\n")

        file.write("VELOCITY = all\nACCELERATION = all\nOLOAD(SORT1, REAL) = all\nLOADSET = 100\n\nSUBCASE 1\nSUBTITLE = STATIKA\n")

        file.write("DISPLACEMENT = ALL\nLOAD = 222\nSPC = 10\nTSTEPNL = 1\nPARAM, TSTATIC, 1\n\n")

        file.write("SUBCASE 2\nSUBTITLE =   DINAMIKA_1\nPARAM,TSTATIC,-1\nDLOAD=210\nDISPLACEMENT=ALL\n")

        file.write("TSTEPNL=2\nNONLINEAR=1\nSPC=10\nSTATSUB  =   5\n\n")

        file.write("OUTPUT(XYPLOT)\n   PLOTTER = NAST\n   CSCALE = 1.3\n   XAXIS = YES\n   YAXIS = YES\n")

        file.write("   XTITLE = TIME IN SEC\n   YTITLE = DISPLACEMENT\nXYPLOT DISP RESP / 11(T2) / 11(T3) / 11(R1)\n")

        file.write("BEGIN   BULK\nPARAM   G           0.1\nPARAM   W3          1.0\n\nPARAM   POST      0\n")

        file.write("PARAM   PRTMAXIM  YES\n\n")


        N_rocket = L / 0.1 + 1
        N_konteiner = L_Kon / 0.1 + 1
        k = 0.1



#--1.1--- Запись GRID с 1 по N-й узел
        u = 0
        while u < N_rocket:
            cox = u * k
            u += 1
            file.write(f"GRID    {u: <8d}        {cox: <8.1f}\n")
        file.write("\n\n")



#--1.2--- Запись GRID с 100001 по 10000N-й узел контейнера
        u = 0
        while u < N_konteiner:
            u_1 = 100001 + u
            cox = u * k
            coy = (bd.d0_Kon - bd.d0) / 2
            u += 1
            file.write(f"GRID    {u_1: <8d}        {cox: <8.1f}{coy: <8.2f}\n")
        file.write("\n\n\n\n\n\n\n\n\n\n")



#--2.1--- Запись GRID для баков окилителя с Xo+1000 по (Xo+o)+1000 узел
        o = (bd.Xo_1 + bd.Lo_1) / k + 1001
        o1 = bd.Xo_1 / k + 1001
        u = o1
        while u < o + 1:
            cox = (u - 1001) * k
            file.write(f"GRID    {int(u): <8d}        {cox: <8.1f}\n")
            u += 1
        file.write("\n\n")



#--2.2--- Запись GRID для баков горючего с Xg+1000 по (Xg+g)+1000 узел
        g = (bd.Xg_1 + bd.Lg_1) / k + 1001
        g1 = bd.Xg_1 / k + 1001
        u = g1
        while u < g + 1:
            cox = (u - 1001) * k
            file.write(f"GRID    {int(u): <8d}        {cox: <8.1f}\n")
            u += 1
        file.write("\n\n\n\n\n\n\n\n\n\n")



#--3.1--- Запись CBAR с 1 по N-1-й узел
        u = 0
        Np = 1  # Np - номер параметра балочного элемента (для ракеты = 1)
        while u < N_rocket - 1:
            u += 1
            file.write(f"CBAR    {int(u): <8d}{Np: <8d}{int(u): <8d}{u + 1: <8d}0.0     1.0     0.0\n")
        file.write("\n\n")



#--3.2--- Запись CBAR с 100001 по 10000N-1-й узел контейнера
        u = 0
        Np = 2  # Np - номер параметра балочного элемента (для контейнера = 2)
        while u < N_konteiner - 1:
            u += 1
            u = int(u)
            file.write(f"CBAR    {u + 100000: <8d}{Np: <8d}{u + 100000: <8d}{u + 100001: <8d}0.0     1.0     0.0\n")
        file.write("\n\n\n\n\n\n\n\n\n\n")



#--4.1--- Запись RBE2 для баков окислителя с Xo+1000 по (Xo+o)+1000 узел
        u = int(o1)
        while u < o + 1:
            file.write(f"RBE2    {u + 1000: <8d}{u - 1000: <8d}2       {u: <8d}\n")
            u += 1
        file.write("\n")

        file.write(f"RBE2    {int(o1 + 2000): <8d}{int(o1 - 1000): <8d}1       {int(o1): <8d}\n")
        
        u = int(o1)
        while u < o:
            file.write(f"RBE2    {u + 2001: <8d}{u: <8d}1       {u + 1: <8d}\n")
            u += 1
        file.write("\n\n")



#--4.2--- Запись RBE2 для баков горючего с Xg+1000 по (Xg+g)+1000 узел
        u = int(g1)
        while u < g + 1:
            file.write(f"RBE2    {u + 1000: <8d}{u - 1000: <8d}2       {u: <8d}\n")
            u += 1
        file.write("\n")

        file.write(f"RBE2    {int(g1 + 2000): <8d}{int(g1 - 1000): <8d}1       {int(g1): <8d}\n")

        u = int(g1)
        while u < g:
            file.write(f"RBE2    {u + 2001: <8d}{u: <8d}1       {u + 1: <8d}\n")
            u += 1
        file.write("\n\n\n\n\n\n\n\n\n\n")



#--5.1--- Запись CONM2 для бака окислителя
# определение сосредоточенной массы узла бака окислителя
        mo_uzla = bd.mo_1 / (o - o1)
        u = o1
        while u < o + 1:
            u = int(u)
            file.write(f"CONM2   {u: <8d}{u: <8d}        {mo_uzla: <8.1f}\n")
            u += 1
        file.write("\n\n")



#--5.2--- Запись CONM2 для бака горючего
# определение сосредоточенной массы узла бака горючего
        mg_uzla = bd.mg_1 / (g - g1)
        u = g1
        while u < g + 1:
            u = int(u)
            file.write(f"CONM2   {u: <8d}{u: <8d}        {mg_uzla: <8.1f}\n")
            u += 1
        file.write("\n\n")



#--5.3--- Запись CONM2 сосредоточенных масс (ду,су,пн)
        if bd.m_dy_1 > 0:
            n_dy = (bd.X_dy_1 / k) + 1
            file.write(f"CONM2   {int(n_dy + 7000): <8d}{int(n_dy): <8d}        {int(bd.m_dy_1): <8.2f}\n")

        if bd.m_cy > 0:
            n_cy = (bd.X_cy / k) + 1
            file.write(f"CONM2   {int(n_cy + 7000): <8d}{int(n_cy): <8d}        {int(bd.m_cy): <8.2f}\n")

        if bd.m_gch > 0:
            n_gch = (bd.X_gch / k) + 1
            file.write(f"CONM2   {int(n_gch + 7000): <8d}{int(n_gch): <8d}        {int(bd.m_gch): <8.2f}\n")

        file.write("\n\n\n\n\n\n\n\n\n\n")



#--6--- Запись NOLIN1 с 1 по N-й узел
        u = 1
        while u < N_rocket + 1:
            file.write(f"NOLIN1  1       {u: <8d}2       1.0     {u: <8d}1       {u + 100: <8d}\n")
            u += 1
        file.write("\n\n\n\n\n\n\n\n\n\n")



#--7--- Запись TABLED1 (ветровые усилия)
# если ракета с наземным стартом
        if bd.start_rocket == 1:
            po_vozduh = 1225
            P_veter = ((po_vozduh * bd.V_sredy * bd.V_sredy) / 2) * (0.1 * bd.d0)
            u = 1

            while u < N_rocket + 1:
                vychitanie = L_Kon - ((u * k) - k)
                slozhenie = L_Kon - ((u * k) - k) + k
                file.write(f"TABLED1 {u + 100: <8d}\n        0.00    0.00    {vychitanie: <8.1f}0.00    {slozhenie: <8.1f}{P_veter: <8.1f}100.0   {P_veter: <8.1f}\n        ENDT\n")
                u += 1

            file.write("\n\n\n\n\n\n\n\n\n\n")

        else:
            po_vody = 997
            P_vody = ((po_vody * bd.V_sredy * bd.V_sredy) / 2) * (0.1 * bd.d0)
            u = 1
            while u < N_rocket + 1:
                vychitanie = L_Kon - ((u * k) - k)
                slozhenie = L_Kon - ((u * k) - k) + k
                file.write(f"TABLED1 {u + 100: <8d}\n        0.00    0.00    {vychitanie: <8.1f}0.00    {slozhenie: <8.1f}{P_vody: <8.1f}100.0   {P_vody: <8.1f}\n        ENDT\n")
                u += 1

            file.write("\n\n\n\n\n\n\n\n\n\n")



#--8.1--- Запись SPC с 1 по N-й узел
        u = 1
        while u < N_rocket + 1:
            file.write(f"SPC     10      {u: <8d}345\n")
            u += 1
        file.write("\n\n")



#--8.2--- Запись SPC с 100001 по 10000N-й узел контейнера
        u = 1
        while u < N_konteiner + 1:
            file.write(f"SPC     10      {u + 100000: <8d}345\n")
            u += 1
        file.write("\n\n\n\n\n\n\n\n\n\n")



#--9.1--- Запись SPC окислитель
        u = o1
        while u < o + 1:
            file.write(f"SPC     10      {int(u): <8d}345\n")
            u += 1
        file.write("\n\n")



#--9.2--- Запись SPC горючее
        u = g1
        while u < g + 1:
            file.write(f"SPC     10      {int(u): <8d}345\n")
            u += 1
        file.write("\n\n")



#--9.3--- Запись SPC опорных узлов контейнера
        def tip_zakr_obsh():
            if tip_zakr_3 == None:
                file.write(f"SPC     10      {int(L_kon_zakr_1) * 10 + 100001: <8d}{tip_zakr_1: <8d}\n")
                file.write(f"SPC     10      {int(L_kon_zakr_2) * 10 + 100001: <8d}{tip_zakr_2: <8d}\n")
                file.write("\n\n\n\n\n\n\n\n\n\n")

            elif tip_zakr_4 == None:
                file.write(f"SPC     10      {int(L_kon_zakr_1) * 10 + 100001: <8d}{tip_zakr_1: <8d}\n")
                file.write(f"SPC     10      {int(L_kon_zakr_2) * 10 + 100001: <8d}{tip_zakr_2: <8d}\n")
                file.write(f"SPC     10      {int(L_kon_zakr_3) * 10 + 100001: <8d}{tip_zakr_3: <8d}\n")
                file.write("\n\n\n\n\n\n\n\n\n\n")

            elif tip_zakr_5 == None:
                file.write(f"SPC     10      {int(L_kon_zakr_1) * 10 + 100001: <8d}{tip_zakr_1: <8d}\n")
                file.write(f"SPC     10      {int(L_kon_zakr_2) * 10 + 100001: <8d}{tip_zakr_2: <8d}\n")
                file.write(f"SPC     10      {int(L_kon_zakr_3) * 10 + 100001: <8d}{tip_zakr_3: <8d}\n")
                file.write(f"SPC     10      {int(L_kon_zakr_4) * 10 + 100001: <8d}{tip_zakr_4: <8d}\n")
                file.write("\n\n\n\n\n\n\n\n\n\n")

            else:
                file.write(f"SPC     10      {int(L_kon_zakr_1) * 10 + 100001: <8d}{tip_zakr_1: <8d}\n")
                file.write(f"SPC     10      {int(L_kon_zakr_2) * 10 + 100001: <8d}{tip_zakr_2: <8d}\n")
                file.write(f"SPC     10      {int(L_kon_zakr_3) * 10 + 100001: <8d}{tip_zakr_3: <8d}\n")
                file.write(f"SPC     10      {int(L_kon_zakr_4) * 10 + 100001: <8d}{tip_zakr_4: <8d}\n")
                file.write(f"SPC     10      {int(L_kon_zakr_5) * 10 + 100001: <8d}{tip_zakr_5: <8d}\n")
                file.write("\n\n\n\n\n\n\n\n\n\n")
        tip_zakr_obsh()



#--10--- Количество аморт.
        bd.kolichestvo_amort = int(bd.kolichestvo_amort)
        def kolichestvo_amort_obsh():

            if bd.kolichestvo_amort == 2:
                # Запись GRID узлы скольжения

                a1 = bd.X1 / k  # узел первого амортизатора
                a2 = bd.X2 / k  # узел второго амортизатора

                a1 = int(a1)
                a2 = int(a2)

                file.write(f"GRID    {a1 + 200001: <8d}        {bd.X1: <8.1f}{coy: <8.1f}0.00\n")
                file.write(f"GRID    {a2 + 200001: <8d}        {bd.X2: <8.1f}{coy: <8.1f}0.00\n")

                file.write("\n\n")

                file.write(f"GRID    {a1 + 200011: <8d}        {bd.X1: <8.1f}{coy: <8.1f}0.00\n")
                file.write(f"GRID    {a2 + 200011: <8d}        {bd.X2: <8.1f}{coy: <8.1f}0.00\n")

                coy_kont = coy * 2

                file.write("\n\n")

                file.write(f"GRID    {a1 + 300011: <8d}        {bd.X1: <8.1f}{coy_kont: <8.1f}0.00\n")

                file.write(f"GRID    {a2 + 300011: <8d}        {bd.X2: <8.1f}{coy_kont: <8.1f}0.00\n")

                file.write("\n\n")

                # Запись CELAS1 узлов скольжения

                file.write(f"CELAS1  {a1 + 200001: <8.1f}2       {a1 + 1: <8.1f}2       {a1 + 200001: <8.1f}2\n")

                file.write(f"CELAS1  {a2 + 200001: <8.1f}2       {a2 + 1: <8.1f}2       {a2 + 200001: <8.1f}2\n")

                file.write("\n\n")

                file.write(f"CELAS1  {a1 + 200011: <8.1f}2       {a1 + 200011: <8.1f}2       {a1 + 300011: <8.1f}2\n")

                file.write(f"CELAS1  {a2 + 200011: <8.1f}2       {a2 + 200011: <8.1f}2       {a2 + 300011: <8.1f}2\n")

                file.write("\n\n")

                # Запись PELAS узлов скольжения (жесткость?)

                file.write(f"PELAS   2       {bd.zhestkost_amort: <8.1f}+6\n\n")

                file.write("\n\n")

                # Запись RBE2 узлов скольжения

                i1 = 1

                file.write(f"RBE2    {a1 + 400001: <8.1f}{a1 + 1: <8.1f} {i1: <8d}{a1 + 200001: <8.1f}{a1 + 200011: <8.1f}{a1 + 300011: <8.1f}\n")

                file.write(f"RBE2    {a2 + 400001: <8.1f}{a2 + 1: <8.1f} {i1: <8d}{a2 + 200001: <8.1f}{a2 + 200011: <8.1f}{a2 + 300011: <8.1f}\n")

                file.write("\n\n")

                i2 = 2

                file.write(f"RBE2    {a1 + 400011: <8.1f}{a1 + 1: <8.1f} {i2: <8d}{a1 + 300011: <8.1f}\n")

                file.write(f"RBE2    {a2 + 400011: <8.1f}{a2 + 1: <8.1f} {i2: <8d}{a2 + 300011: <8.1f}\n")

                file.write("\n\n")

                # Запись BLSEG

                file.write(f"BLSEG   1       {a1 + 1: <8.1f}{a1 + 200001: <8.1f}\n")
                file.write(f"BLSEG   3       {a2 + 1: <8.1f}{a2 + 200001: <8.1f}\n")

                file.write("\n\n")

                file.write(f"BLSEG   7       {a1 + 300011: <8.1f}{a1 + 200011: <8.1f}\n")
                file.write(f"BLSEG   8       {a2 + 300011: <8.1f}{a2 + 200011: <8.1f}\n")

                file.write("\n\n")

                # Запись BCONP

                file.write("BCONP   1       1       2               1.0     10      1       1\n")
                file.write("BCONP   2       3       2               1.0     10      1       1\n")

                file.write("\n\n")

                file.write("BCONP   6       7       2               1.0     10      1       3\n")
                file.write("BCONP   7       8       2               1.0     10      1       3\n")

                file.write("\n\n\n\n\n\n\n\n\n\n")

            elif bd.kolichestvo_amort == 3:
                # Запись GRID узлы скольжения

                a1 = bd.X1 / k  # узел первого амортизатора
                a2 = bd.X2 / k  # узел второго амортизатора

                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a1 + 200001, bd.X1, coy
                    )
                )
                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a2 + 200001, bd.X2, coy
                    )
                )
                file.write("\n\n")

                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a1 + 200011, bd.X1, coy
                    )
                )
                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a2 + 200011, bd.X2, coy
                    )
                )
                file.write("\n\n")

                coy_kont = coy * 2

                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a1 + 300011, bd.X1, coy_kont
                    )
                )
                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a2 + 300011, bd.X2, coy_kont
                    )
                )
                file.write("\n\n")

                # Запись CELAS1 узлов скольжения

                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a1 + 200001, a1 + 1, a1 + 200001
                    )
                )
                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a2 + 200001, a2 + 1, a2 + 200001
                    )
                )
                file.write("\n\n")

                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a1 + 200011, a1 + 200011, a1 + 300011
                    )
                )
                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a2 + 200011, a2 + 200011, a2 + 300011
                    )
                )
                file.write("\n\n")

                # Запись PELAS узлов скольжения (жесткость?)

                file.write("PELAS   2       {: <8.1f}+6\n\n".format(bd.zhestkost_amort))

                # Запись RBE2 узлов скольжения

                i1 = 1

                file.write(
                    "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(
                        a1 + 400001, a1 + 1, i1, a1 + 200001, a1 + 200011, a1 + 300011
                    )
                )
                file.write(
                    "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(
                        a2 + 400001, a2 + 1, i1, a2 + 200001, a2 + 200011, a2 + 300011
                    )
                )
                file.write("\n\n")

                i2 = 2

                file.write(
                    "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(
                        a1 + 400011, a1 + 1, i2, a1 + 300011
                    )
                )
                file.write(
                    "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(
                        a2 + 400011, a2 + 1, i2, a2 + 300011
                    )
                )
                file.write("\n\n")

                # Запись BLSEG

                file.write(
                    "BLSEG   1       {: <8.1f}{: <8.1f}\n".format(a1 + 1, a1 + 200001)
                )
                file.write(
                    "BLSEG   3       {: <8.1f}{: <8.1f}\n".format(a2 + 1, a2 + 200001)
                )
                file.write("\n")

                file.write(
                    "BLSEG   7       {: <8.1f}{: <8.1f}\n".format(a1 + 300011, a1 + 200011)
                )
                file.write(
                    "BLSEG   8       {: <8.1f}{: <8.1f}\n".format(a2 + 300011, a2 + 200011)
                )
                file.write("\n\n")

                # Запись BCONP

                file.write(
                    "BCONP   1       1       2               1.0     10      1       1\n"
                )
                file.write(
                    "BCONP   2       3       2               1.0     10      1       1\n"
                )
                file.write("\n")

                file.write(
                    "BCONP   6       7       2               1.0     10      1       3\n"
                )
                file.write(
                    "BCONP   7       8       2               1.0     10      1       3\n"
                )

            elif bd.kolichestvo_amort == 4:
                # Запись GRID узлы скольжения

                a1 = bd.X1 / k  # узел первого амортизатора
                a2 = bd.X2 / k  # узел второго амортизатора

                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a1 + 200001, bd.X1, coy
                    )
                )
                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a2 + 200001, bd.X2, coy
                    )
                )
                file.write("\n\n")

                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a1 + 200011, bd.X1, coy
                    )
                )
                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a2 + 200011, bd.X2, coy
                    )
                )
                file.write("\n\n")

                coy_kont = coy * 2

                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a1 + 300011, bd.X1, coy_kont
                    )
                )
                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a2 + 300011, bd.X2, coy_kont
                    )
                )
                file.write("\n\n")

                # Запись CELAS1 узлов скольжения

                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a1 + 200001, a1 + 1, a1 + 200001
                    )
                )
                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a2 + 200001, a2 + 1, a2 + 200001
                    )
                )
                file.write("\n\n")

                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a1 + 200011, a1 + 200011, a1 + 300011
                    )
                )
                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a2 + 200011, a2 + 200011, a2 + 300011
                    )
                )
                file.write("\n\n")

                # Запись PELAS узлов скольжения (жесткость?)

                file.write("PELAS   2       {: <8.1f}+6\n\n".format(bd.zhestkost_amort))

                # Запись RBE2 узлов скольжения

                i1 = 1

                file.write(
                    "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(
                        a1 + 400001, a1 + 1, i1, a1 + 200001, a1 + 200011, a1 + 300011
                    )
                )
                file.write(
                    "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(
                        a2 + 400001, a2 + 1, i1, a2 + 200001, a2 + 200011, a2 + 300011
                    )
                )
                file.write("\n\n")

                i2 = 2

                file.write(
                    "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(
                        a1 + 400011, a1 + 1, i2, a1 + 300011
                    )
                )
                file.write(
                    "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(
                        a2 + 400011, a2 + 1, i2, a2 + 300011
                    )
                )
                file.write("\n\n")

                # Запись BLSEG

                file.write(
                    "BLSEG   1       {: <8.1f}{: <8.1f}\n".format(a1 + 1, a1 + 200001)
                )
                file.write(
                    "BLSEG   3       {: <8.1f}{: <8.1f}\n".format(a2 + 1, a2 + 200001)
                )
                file.write("\n")

                file.write(
                    "BLSEG   7       {: <8.1f}{: <8.1f}\n".format(a1 + 300011, a1 + 200011)
                )
                file.write(
                    "BLSEG   8       {: <8.1f}{: <8.1f}\n".format(a2 + 300011, a2 + 200011)
                )
                file.write("\n\n")

                # Запись BCONP

                file.write(
                    "BCONP   1       1       2               1.0     10      1       1\n"
                )
                file.write(
                    "BCONP   2       3       2               1.0     10      1       1\n"
                )
                file.write("\n")

                file.write(
                    "BCONP   6       7       2               1.0     10      1       3\n"
                )
                file.write(
                    "BCONP   7       8       2               1.0     10      1       3\n"
                )

            else:
                # Запись GRID узлы скольжения

                a1 = bd.X1 / k  # узел первого амортизатора
                a2 = bd.X2 / k  # узел второго амортизатора

                file.write(
                    "GRID    {: <8.1f}   gg     {: <8f}{: <8.1f}0.00\n".format(
                        a1 + 200001, bd.X1, coy
                    )
                )
                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a2 + 200001, bd.X2, coy
                    )
                )
                file.write("\n\n")

                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a1 + 200011, bd.X1, coy
                    )
                )
                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a2 + 200011, bd.X2, coy
                    )
                )
                file.write("\n\n")

                coy_kont = coy * 2

                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a1 + 300011, bd.X1, coy_kont
                    )
                )
                file.write(
                    "GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(
                        a2 + 300011, bd.X2, coy_kont
                    )
                )
                file.write("\n\n")

                # Запись CELAS1 узлов скольжения

                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a1 + 200001, a1 + 1, a1 + 200001
                    )
                )
                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a2 + 200001, a2 + 1, a2 + 200001
                    )
                )
                file.write("\n\n")

                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a1 + 200011, a1 + 200011, a1 + 300011
                    )
                )
                file.write(
                    "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(
                        a2 + 200011, a2 + 200011, a2 + 300011
                    )
                )
                file.write("\n\n")

                # Запись PELAS узлов скольжения (жесткость?)

                file.write("PELAS   2       {: <8.1f}+6\n\n".format(bd.zhestkost_amort))

                # Запись RBE2 узлов скольжения

                i1 = 1

                file.write(
                    "RBE2    {: <8.1f}{: <8.1f}{: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(
                        a1 + 400001, a1 + 1, i1, a1 + 200001, a1 + 200011, a1 + 300011
                    )
                )
                file.write(
                    "RBE2    {: <8.1f}{: <8.1f}{: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(
                        a2 + 400001, a2 + 1, i1, a2 + 200001, a2 + 200011, a2 + 300011
                    )
                )
                file.write("\n\n")

                i2 = 2

                file.write(
                    "RBE2    {: <8.1f}{: <8.1f}{: <8d}{: <8.1f}\n".format(
                        a1 + 400011, a1 + 1, i2, a1 + 300011
                    )
                )
                file.write(
                    "RBE2    {: <8.1f}{: <8.1f}{: <8d}{: <8.1f}\n".format(
                        a2 + 400011, a2 + 1, i2, a2 + 300011
                    )
                )
                file.write("\n\n")

                # Запись BLSEG

                file.write(
                    "BLSEG   1       {: <8.1f}{: <8.1f}\n".format(a1 + 1, a1 + 200001)
                )
                file.write(
                    "BLSEG   3       {: <8.1f}{: <8.1f}\n".format(a2 + 1, a2 + 200001)
                )
                file.write("\n")

                file.write(
                    "BLSEG   7       {: <8.1f}{: <8.1f}\n".format(a1 + 300011, a1 + 200011)
                )
                file.write(
                    "BLSEG   8       {: <8.1f}{: <8.1f}\n".format(a2 + 300011, a2 + 200011)
                )
                file.write("\n\n")

                # Запись BCONP

                file.write(
                    "BCONP   1       1       2               1.0     10      1       1\n"
                )
                file.write(
                    "BCONP   2       3       2               1.0     10      1       1\n"
                )
                file.write("\n")

                file.write(
                    "BCONP   6       7       2               1.0     10      1       3\n"
                )
                file.write(
                    "BCONP   7       8       2               1.0     10      1       3\n"
                )
        kolichestvo_amort_obsh()



#--11--- Запись BLSEG

        file.write("BLSEG   2       100001  THRU    {: <8.1f}".format(float(N_konteiner) + 100010))
        file.write("\n\n")

        # Запись BFRIC

        file.write("BFRIC   10                      0.1")
        file.write("\n\n")

        # Запись CORD2R

        file.write("CORD2R  1               0.0     1.1     0.0     0.0     1.1     -1.0\n        1.0     1.1     0.0")
        file.write("\n\n")

        # Запись CORD2R

        file.write(
            "CORD2R  3               0.0     -1.1    0.0     0.0     -1.1    1.0\n        1.0     -1.1    0.0"
        )
        file.write("\n\n")

# --------------------------------- Запись TABLED1 (тяга)

        file.write(
            f"TABLED1 411\n        0.0     0.0     1.0     0.0     {bd.t_p1:<8.2e} {bd.P1:<8.2e} {bd.t_p2:<8.2e} {bd.P2:<8.2e}\n".replace(
                "e", ""
            )
        )

        file.write(
            f"        {bd.t_p3:<8.2e} {bd.P3:<8.2e} {bd.t_p4:<8.2e} {bd.P4:<8.2e} {bd.t_p5:<8.2e} {bd.P5:<8.2e} {bd.t_p6:<8.2e} {bd.P6:<8.2e}\n".replace(
                "e", ""
            )
        )

        file.write(
            f"        {bd.t_p7:<8.2e} {bd.P7:<8.2e} {bd.t_p8:<8.2e} {bd.P8:<8.2e} {bd.t_p9:<8.2e} {bd.P9:<8.2e} {bd.t_p10:<8.2e} {bd.P10:<8.2e}\n".replace(
                "e", ""
            )
        )

        file.write(
            f"        {bd.t_p11:<8.2e} {bd.P11:<8.2e} {bd.t_p12:<8.2e} {bd.P12:<8.2e} {bd.t_p13:<8.2e} {bd.P13:<8.2e}ENDT\n".replace(
                "e", ""
            )
        )

        file.write("\n\n")

        # Запись TLOAD1

        file.write("TLOAD1  210     110     0       0       411")
        file.write("\n\n")

        # Запись FORCE

        file.write("FORCE   111     1       0       1.0     1.0     0.0")
        file.write("\n\n")

        # Запись LSEQ

        file.write("LSEQ    100     110     111")
        file.write("\n\n")

        # Запись DLOAD

        file.write("DLOAD   333     1.00    1.00    210     1.00    310")
        file.write("\n\n")

        # Запись LOAD

        file.write("LOAD    444     1.0     1.0     222")
        file.write("\n\n")

        # Запись MAT1

        massa_korpusa = bd.m - bd.m_gch - bd.m_cy - bd.m_dy_1 - bd.mo_1 - bd.mg_1
        plotnost1 = massa_korpusa / (((3.14 * bd.d0 * bd.d0 / 4) - (3.14 * (bd.d0 - tol_R) * (bd.d0 - tol_R) / 4))* bd.L)

        file.write(
            "MAT1    1       {: <2.1f}+10          {: <8.2f}{: <8.1f}\n".format(
                bd.modul_unga1, bd.koeff_puass1, plotnost1
            )
        )
        file.write(
            "MAT1    2       {: <2.1f}+10          {: <8.2f}{: <8.3f}".format(
                bd.modul_unga2, bd.koeff_puass2, bd.plotnost2
            )
        )
        file.write("\n\n")

        # Запись PBARL

        file.write(
            f"PBARL   1       1               TUBE2\n        {(float(bd.d0) / 2):<8.2e} {float(tol_R):<8.2e}".replace(
                "e", ""
            )
        )
        file.write("\n")
        file.write(
            f"PBARL   2       2               TUBE2\n        {(float(d0_Kon) / 2):<8.2e} {float(tol_Kon):<8.2e}".replace(
                "e", ""
            )
        )
        file.write("\n\n")

        # Запись LSEQ для ускорения свободного падения

        file.write("LSEQ    100     210     222")
        file.write("\n")

        # Запись GRAV для ускорения свободного падения

        file.write("GRAV    222             -9.81   1.0     0.0     0.0")
        file.write("\n")

        # Запись TLOAD1 для ускорения свободного падения

        file.write("TLOAD1  310     210     0       0       511")
        file.write("\n")

        # Запись TABLED1 для ускорения свободного падения

        file.write("TABLED1 511\n        0.0     1.0     30.0    1.0     ENDT")
        file.write("\n\n")

        # Запись GRID для продольной амортизации контейнера

        file.write(
            "GRID    9000            0.0     {: <8.3f}0.0".format((bd.d0 / 2) + 0.1)
        )
        file.write("\n\n")

        # Запись PELAS

        file.write("PELAS   9000    658.6+6")
        file.write("\n\n")

        # Запись CELAS1

        file.write("CELAS1  9000    9000    100001  1       9000    1")
        file.write("\n\n")

        # Запись SPC для опорного стола

        file.write("SPC     10      9000    123456\n")
        file.write("\n\n")

        # Запись TSTEPNL

        n_time = 0.001  # шаг по времени
        t_shoda = bd.t / n_time  # время схода поясов амортизации

        file.write("TSTEPNL 1       10      0.1     1       ADAPT\n")
        file.write(
            "TSTEPNL 2       {: <8.0f}{: <8.3f}1       ADAPT\n".format(t_shoda, n_time)
        )
        file.write("\n\n")

        file.write("ENDDATA")

        file.close()

        serializer = bdfSerializer(bd)
        return Response(serializer.data, status=HTTP_200_OK)


def download_file(request):
    # Укажите путь к вашему файлу 1.txt
    file_path = "/home/ilya/Рабочая/Strength/app/1.txt"
    return FileResponse(open(file_path, "rb"), as_attachment=True, filename="1.txt")
