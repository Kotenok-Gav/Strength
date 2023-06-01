from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from .models import Rockets_bdf
from .serializers import bdfSerializer

from decimal import Decimal



def home(request):
    return render(request, 'home.html')


@api_view(["GET", "POST"])
def bdf_list(request):
    if request.method == "GET":
        bdf = Rockets_bdf.objects.all()
        serializer = bdfSerializer(bdf, many = True)
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
        N = request.data.get("N")
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
# 6 ------------
        modul_unga1 = request.data.get("modul_unga1")
        koeff_puass1 = request.data.get("koeff_puass1")
        modul_unga2 = request.data.get("modul_unga2")
        koeff_puass2 = request.data.get("koeff_puass2")
        plotnost2 = request.data.get("plotnost2")

#-----------------------------------------------------------------------
        bd = Rockets_bdf.objects.create(
        # 1 ------------ 
            text=text,
            start_rocket=float(start_rocket),
            t=Decimal(t),
        # 2 ------------  
            d0=Decimal(d0),
            tol_R=Decimal(tol_R),
            L=Decimal(L),
            d0_Kon=Decimal(d0_Kon),
            tol_Kon=Decimal(tol_Kon),
            L_Kon=Decimal(L_Kon),
        # 3 ------------  
            kolichestvo_amort=Decimal(kolichestvo_amort),
            zhestkost_amort=Decimal(zhestkost_amort),
            X1=Decimal(X1),
            X2=Decimal(X2),
            X3=Decimal(X3),
            X4=Decimal(X4),
            X5=Decimal(X5),
        # 4 ------------ 
            V_sredy=Decimal(V_sredy),
            N=Decimal(N),
            t_p0=Decimal(t_p0), P0=Decimal(P0), 
            t_p1=Decimal(t_p1), P1=Decimal(P1), 
            t_p2=Decimal(t_p2), P2=Decimal(P2), 
            t_p3=Decimal(t_p3), P3=Decimal(P3), 
            t_p4=Decimal(t_p4), P4=Decimal(P4), 
            t_p5=Decimal(t_p5), P5=Decimal(P5), 
            t_p6=Decimal(t_p6), P6=Decimal(P6), 
            t_p7=Decimal(t_p7), P7=Decimal(P7), 
            t_p8=Decimal(t_p8), P8=Decimal(P8), 
            t_p9=Decimal(t_p9), P9=Decimal(P9), 
            t_p10=Decimal(t_p10), P10=Decimal(P10), 
            t_p11=Decimal(t_p11), P11=Decimal(P11), 
            t_p12=Decimal(t_p12), P12=Decimal(P12), 
            t_p13=Decimal(t_p13), P13=Decimal(P13), 
            dl_1=Decimal(dl_1), 
            nap_zak_1=Decimal(nap_zak_1), 
            zhestkost_opor_1=Decimal(zhestkost_opor_1),
            dl_2=Decimal(dl_2), 
            nap_zak_2=Decimal(nap_zak_2), 
            zhestkost_opor_2=Decimal(zhestkost_opor_2), 
            dl_3=Decimal(dl_3), 
            nap_zak_3=Decimal(nap_zak_3), 
            zhestkost_opor_3=Decimal(zhestkost_opor_3),
        # 5 ------------ 
            m=Decimal(m),
            m_gch=Decimal(m_gch),
            X_gch=Decimal(X_gch),
            m_cy=Decimal(m_cy),
            X_cy=Decimal(X_cy),
            m_dy_1=Decimal(m_dy_1),
            X_dy_1=Decimal(X_dy_1),
            mo_1=Decimal(mo_1),
            Lo_1=Decimal(Lo_1),
            Xo_1=Decimal(Xo_1),
            mg_1=Decimal(mg_1),
            Lg_1=Decimal(Lg_1),
            Xg_1=Decimal(Xg_1),
        # 6 ------------ 
            modul_unga1=Decimal(modul_unga1),
            koeff_puass1=Decimal(koeff_puass1),
            modul_unga2=Decimal(modul_unga2),
            koeff_puass2=Decimal(koeff_puass2),
            plotnost2=Decimal(plotnost2))
         
#----------------------------------------------------------------     
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


        # Запись GRID с 1 по N-й узел
        u = 0
        k = 0.1
        while u < float(bd.N):
            cox = u * k
            u += 1
            file.write("GRID    {: <8d}        {: <8.1f}\n".format(u, cox))
        file.write("\n")

            # Запись GRID с 100001 по 10000N-й узел контейнера
        u = 0
        k = 0.1
        d0 = 0
        while u < float(bd.N):
            u_1 = 100001 + u
            cox = u * k
            coy = (d0 / 2) + 0.1
            u += 1
            file.write("GRID    {: <8d}        {: <8.1f}{: <8.2f}\n".format(u_1, cox, coy))
        file.write("\n")

        # Запись GRID для баков окилителя с Xo+1000 по (Xo+o)+1000 узел
        k = Decimal('0.1')
        o = ((bd.Xo_1 + bd.Lo_1) / k + 1001)
        o1 = (bd.Xo_1 / k + 1001)
        u = o1
        while u < o + 1:
            cox = (u - 1001) * k
            u += 1
            u = int(u)
            file.write("GRID    {: <8d}        {: <8.1f}\n".format(u, cox))
        file.write("\n")

        # Запись GRID для баков горючего с Xg+1000 по (Xg+g)+1000 узел
        g = ((bd.Xg_1 + bd.Lg_1) / k + 1001)
        g1 = (bd.Xg_1 / k + 1001)
        u = g1
        while u < g + 1:
            cox = (u - 1001) * k
            u += 1
            u = int(u)
            file.write("GRID    {: <8d}        {: <8.1f}\n".format(u, cox))
        file.write("\n\n")

        # Запись CBAR с 1 по N-1-й узел
        u = 0
        Np = 1  # Np - номер параметра балочного элемента (для ракеты =1 )
        while u < float(bd.N):
            u += 1
            u = int(u)
            file.write("CBAR    {: <8d}{: <8d}{: <8d}{: <8d}0.0     1.0     0.0\n".format(u, Np, u, u + 1))
        file.write("\n\n")

        # Запись CBAR с 100001 по 10000N-1-й узел контейнера
        u = 0
        Np = 2  # Np - номер параметра балочного элемента (для контейнера =2 )
        while u < float(bd.N) + 10:
            u += 1
            u = int(u)
            file.write(
                "CBAR    {: <8d}{: <8d}{: <8d}{: <8d}0.0     1.0     0.0\n".format(u + 100000, Np, u + 100000, u + 100001))
        file.write("\n\n")

        # Запись RDE2 для баков окислителя с Xo+1000 по (Xo+o)+1000 узел
        u = o1
        while u < o + 1:
            u += 1
            u = int(u)
            file.write("RBE2    {: <8d}{: <8d}2       {: <8d}\n".format(u + 1000, u - 1000, u))
        file.write("\n")
        file.write("RBE2    {: <8.1f}{: <8.1f}1       {: <8.1f}\n".format(o1 + 2000, o1 - 1000, o1))
        u = o1
        while u < o:
            u += 1
            u = int(u)
            file.write("RBE2    {: <8d}{: <8d}1       {: <8d}\n".format(u + 2001, u, u + 1))
        file.write("\n")

        # Запись RDE2 для баков горючего с Xg+1000 по (Xg+g)+1000 узел
        u = g1
        while u < g + 1:
            u += 1
            u = int(u)
            file.write("RBE2    {: <8d}{: <8d}2       {: <8d}\n".format(u + 1000, u - 1000, u))
        file.write("\n\n")
        file.write("RBE2    {: <8.1f}{: <8.1f}1       {: <8.1f}\n".format(g1 + 2000, g1 - 2000, g1))
        u = g1
        while u < g:
            u += 1
            u = int(u)
            file.write("RBE2    {: <8d}{: <8d}1       {: <8d}\n".format(u + 2001, u, u + 1))
        file.write("\n\n")

        # Запись CONM2 для бака окислителя
        mo_uzla = bd.mo_1 / (o - o1)  # определение сосредоточенной массы узла бака окислителя
        u = o1
        while u < o + 1:
            u += 1
            u = int(u)
            file.write("CONM2   {: <8d}{: <8d}        {: <8.1f}\n".format(u, u, mo_uzla))
        file.write("\n")

        # Запись CONM2 для бака горючего
        mg_uzla = bd.mg_1 / (g - g1)  # определение сосредоточенной массы узла бака горючего
        u = g1
        while u < g + 1:
            u += 1
            u = int(u)
            file.write("CONM2   {: <8d}{: <8d}        {: <8.1f}\n".format(u, u, mg_uzla))
        file.write("\n")

        # Запись CONM2 сосредоточенных масс (ду,су,пн)
        if (bd.m_dy_1 > 0):
            n_dy = ((bd.X_dy_1 / k) + 1)
            file.write("CONM2   {: <8.1f}{: <8.1f}        {: <8.2f}\n".format(n_dy + 7000, n_dy, bd.m_dy_1))
        if (bd.m_cy > 0):
            n_cy = ((bd.X_cy / k) + 1)
            file.write("CONM2   {: <8.1f}{: <8.1f}        {: <8.2f}\n".format(n_cy + 7000, n_cy, bd.m_cy))
        if (bd.m_gch > 0):
            n_gch = ((bd.X_gch / k) + 1)
            file.write("CONM2   {: <8.1f}{: <8.1f}        {: <8.2f}\n".format(n_gch + 7000, n_gch, bd.m_gch))
        file.write("\n")

        # Запись NOLIN1 с 1 по N-й узел
        u = 1
        while u < float(bd.N) + 1:
            u += 1
            u = int(u)
            file.write(
                "NOLIN1  1       {: <8.1f}2       1.00    {: <8.1f}1       {: <8.1f}\n".format(u, u, u + 100))
        file.write("\n\n")

        #Запись TABLED1 (ветровые усилия)
        #если ракета с наземным стартом
        d = d0 = bd.d0
        if (bd.start_rocket == 1):
            po_vozduh = float(1225)
            po_vozduh = Decimal(po_vozduh)
            P_veter = ((po_vozduh * bd.V_sredy * bd.V_sredy) / 2) * (Decimal('0.1') * bd.d0)
            u = 1
            while u < float(bd.N) + 1:
                u += 1
                u = int(u)
                vychitanie = (bd.L + 1) - ((u * k) - k)
                slozhenie = (bd.L + 1) - ((u * k) - k) + k
                file.write("TABLED1 {: <8d}\n        0.00    0.00    {: <8.1f}0.00    {: <8.1f}{: <8.1f}100.0   {: <8.1f}\n        ENDT\n".format(u + 100, vychitanie, slozhenie, P_veter, P_veter))
            file.write("\n")
        else:
            po_vody = float(997)
            po_vody = Decimal(po_vody)
            P_vody = ((po_vody * bd.V_sredy * bd.V_sredy) / 2) * (Decimal('0.1') * bd.d0)
            u = 1
            while u < float(bd.N) + 1:
                u += 1
                u = int(u)
                vychitanie = (bd.L + 1) - ((u * k) - k)
                slozhenie = (bd.L + 1) - ((u * k) - k) + k
                file.write("TABLED1 {: <8d}\n        0.00    0.00    {: <8.1f}0.00    {: <8.1f}{: <8.1f}100.0   {: <8.1f}\n        ENDT\n".format(u + 100, vychitanie, slozhenie, P_vody, P_vody))
            file.write("\n")

        # Запись SPC с 1 по N-й узел
        u = 1
        while u < float(bd.N) + 1:
            u += 1
            u = int(u)
            file.write("SPC     10      {: <8d}345\n".format(u))
        file.write("\n\n")

        # Запись SPC с 100001 по 10000N-й узел контейнера
        u = 1
        while u < float(bd.N) + 11:
            u += 1
            u = int(u)
            file.write("SPC     10      {: <8d}345\n".format(u + 100000))
        file.write("\n\n")

        # Запись SPC окислитель
        u = o1
        while u < o + 1:
            u += 1
            u = int(u)
            file.write("SPC     10      {: <8d}345\n".format(u))
        file.write("\n\n")

        # Запись SPC горючее
        u = g1
        while u < g + 1:
            u += 1
            u = int(u)
            file.write("SPC     10      {: <8d}345\n".format(u))
        file.write("\n\n")



        if (bd.kolichestvo_amort == 2):
            # Запись GRID узлы скольжения

            a1 = (bd.X1 / k)  # узел первого амортизатора
            a2 = (bd.X2 / k)  # узел второго амортизатора


            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 200001, bd.X1, coy))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 200001, bd.X2, coy))
            file.write("\n\n")

            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 200011, bd.X1, coy))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 200011, bd.X2, coy))
            file.write("\n\n")

            coy_kont = coy * 2

            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 300011, bd.X1, coy_kont))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 300011, bd.X2, coy_kont))
            file.write("\n\n")

            # Запись CELAS1 узлов скольжения

            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a1 + 200001, a1 + 1, a1 + 200001))
            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a2 + 200001, a2 + 1, a2 + 200001))
            file.write("\n\n")

            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a1 + 200011, a1 + 200011, a1 + 300011))
            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a2 + 200011, a2 + 200011, a2 + 300011))
            file.write("\n\n")

            # Запись PELAS узлов скольжения (жесткость?)

            file.write("PELAS   2       {: <8.1f}+6\n\n".format(bd.zhestkost_amort))

            # Запись RBE2 узлов скольжения

            i1 = 1

            file.write("RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(a1 + 400001, a1 + 1, i1, a1 + 200001, a1 + 200011, a1 + 300011))
            file.write("RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(a2 + 400001, a2 + 1, i1, a2 + 200001, a2 + 200011, a2 + 300011))
            file.write("\n\n")

            i2 = 2

            file.write("RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(a1 + 400011, a1 + 1, i2, a1 + 300011))
            file.write("RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(a2 + 400011, a2 + 1, i2, a2 + 300011))
            file.write("\n\n")

            # Запись BLSEG

            file.write("BLSEG   1       {: <8.1f}{: <8.1f}\n".format(a1 + 1, a1 + 200001))
            file.write("BLSEG   3       {: <8.1f}{: <8.1f}\n".format(a2 + 1, a2 + 200001))
            file.write("\n")

            file.write("BLSEG   7       {: <8.1f}{: <8.1f}\n".format(a1 + 300011, a1 + 200011))
            file.write("BLSEG   8       {: <8.1f}{: <8.1f}\n".format(a2 + 300011, a2 + 200011))
            file.write("\n\n")

            # Запись BCONP

            file.write("BCONP   1       1       2               1.0     10      1       1\n")
            file.write("BCONP   2       3       2               1.0     10      1       1\n")
            file.write("\n")

            file.write("BCONP   6       7       2               1.0     10      1       3\n")
            file.write("BCONP   7       8       2               1.0     10      1       3\n")

            # Запись SPC опорных узлов контейнера

            file.write("\n\n")
            file.write("SPC     10      {: <8.1f}23456\n".format(a1 + 100001))
            file.write("SPC     10      {: <8.1f}23456\n".format(a2 + 100001))



        elif (bd.kolichestvo_amort == 3):

            # Запись GRID узлы скольжения

            a1 = (bd.X1 / k)  # узел первого амортизатора
            a2 = (bd.X2 / k)  # узел второго амортизатора

            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 200001, bd.X1, coy))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 200001, bd.X2, coy))
            file.write("\n\n")

            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 200011, bd.X1, coy))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 200011, bd.X2, coy))
            file.write("\n\n")

            coy_kont = coy * 2

            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 300011, bd.X1, coy_kont))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 300011, bd.X2, coy_kont))
            file.write("\n\n")

            # Запись CELAS1 узлов скольжения

            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a1 + 200001, a1 + 1, a1 + 200001))
            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a2 + 200001, a2 + 1, a2 + 200001))
            file.write("\n\n")

            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a1 + 200011, a1 + 200011, a1 + 300011))
            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a2 + 200011, a2 + 200011, a2 + 300011))
            file.write("\n\n")

            # Запись PELAS узлов скольжения (жесткость?)

            file.write("PELAS   2       {: <8.1f}+6\n\n".format(bd.zhestkost_amort))

            # Запись RBE2 узлов скольжения

            i1 = 1

            file.write(
                "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(a1 + 400001, a1 + 1, i1,
                                                                                            a1 + 200001, a1 + 200011,
                                                                                            a1 + 300011))
            file.write(
                "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(a2 + 400001, a2 + 1, i1,
                                                                                            a2 + 200001, a2 + 200011,
                                                                                            a2 + 300011))
            file.write("\n\n")

            i2 = 2

            file.write("RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(a1 + 400011, a1 + 1, i2, a1 + 300011))
            file.write("RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(a2 + 400011, a2 + 1, i2, a2 + 300011))
            file.write("\n\n")

            # Запись BLSEG

            file.write("BLSEG   1       {: <8.1f}{: <8.1f}\n".format(a1 + 1, a1 + 200001))
            file.write("BLSEG   3       {: <8.1f}{: <8.1f}\n".format(a2 + 1, a2 + 200001))
            file.write("\n")

            file.write("BLSEG   7       {: <8.1f}{: <8.1f}\n".format(a1 + 300011, a1 + 200011))
            file.write("BLSEG   8       {: <8.1f}{: <8.1f}\n".format(a2 + 300011, a2 + 200011))
            file.write("\n\n")

            # Запись BCONP

            file.write("BCONP   1       1       2               1.0     10      1       1\n")
            file.write("BCONP   2       3       2               1.0     10      1       1\n")
            file.write("\n")

            file.write("BCONP   6       7       2               1.0     10      1       3\n")
            file.write("BCONP   7       8       2               1.0     10      1       3\n")

            # Запись SPC опорных узлов контейнера

            file.write("\n\n")
            file.write("SPC     10      {: <8.1f}23456\n".format(a1 + 100001))
            file.write("SPC     10      {: <8.1f}23456\n".format(a2 + 100001))

        elif (bd.kolichestvo_amort == 4):

            # Запись GRID узлы скольжения

            a1 = (bd.X1 / k)  # узел первого амортизатора
            a2 = (bd.X2 / k)  # узел второго амортизатора

            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 200001, bd.X1, coy))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 200001, bd.X2, coy))
            file.write("\n\n")

            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 200011, bd.X1, coy))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 200011, bd.X2, coy))
            file.write("\n\n")

            coy_kont = coy * 2

            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 300011, bd.X1, coy_kont))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 300011, bd.X2, coy_kont))
            file.write("\n\n")

            # Запись CELAS1 узлов скольжения

            file.write(
                "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a1 + 200001, a1 + 1, a1 + 200001))
            file.write(
                "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a2 + 200001, a2 + 1, a2 + 200001))
            file.write("\n\n")

            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a1 + 200011, a1 + 200011,
                                                                                        a1 + 300011))
            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a2 + 200011, a2 + 200011,
                                                                                        a2 + 300011))
            file.write("\n\n")

            # Запись PELAS узлов скольжения (жесткость?)

            file.write("PELAS   2       {: <8.1f}+6\n\n".format(bd.zhestkost_amort))

            # Запись RBE2 узлов скольжения

            i1 = 1

            file.write(
                "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(a1 + 400001, a1 + 1, i1,
                                                                                            a1 + 200001, a1 + 200011,
                                                                                            a1 + 300011))
            file.write(
                "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(a2 + 400001, a2 + 1, i1,
                                                                                            a2 + 200001, a2 + 200011,
                                                                                            a2 + 300011))
            file.write("\n\n")

            i2 = 2

            file.write("RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(a1 + 400011, a1 + 1, i2, a1 + 300011))
            file.write("RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(a2 + 400011, a2 + 1, i2, a2 + 300011))
            file.write("\n\n")

            # Запись BLSEG

            file.write("BLSEG   1       {: <8.1f}{: <8.1f}\n".format(a1 + 1, a1 + 200001))
            file.write("BLSEG   3       {: <8.1f}{: <8.1f}\n".format(a2 + 1, a2 + 200001))
            file.write("\n")

            file.write("BLSEG   7       {: <8.1f}{: <8.1f}\n".format(a1 + 300011, a1 + 200011))
            file.write("BLSEG   8       {: <8.1f}{: <8.1f}\n".format(a2 + 300011, a2 + 200011))
            file.write("\n\n")

            # Запись BCONP

            file.write("BCONP   1       1       2               1.0     10      1       1\n")
            file.write("BCONP   2       3       2               1.0     10      1       1\n")
            file.write("\n")

            file.write("BCONP   6       7       2               1.0     10      1       3\n")
            file.write("BCONP   7       8       2               1.0     10      1       3\n")

            # Запись SPC опорных узлов контейнера

            file.write("\n\n")
            file.write("SPC     10      {: <8.1f}23456\n".format(a1 + 100001))
            file.write("SPC     10      {: <8.1f}23456\n".format(a2 + 100001))

        else:

            # Запись GRID узлы скольжения

            a1 = (bd.X1 / k)  # узел первого амортизатора
            a2 = (bd.X2 / k)  # узел второго амортизатора

            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 200001, bd.X1, coy))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 200001, bd.X2, coy))
            file.write("\n\n")

            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 200011, bd.X1, coy))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 200011, bd.X2, coy))
            file.write("\n\n")

            coy_kont = coy * 2

            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a1 + 300011, bd.X1, coy_kont))
            file.write("GRID    {: <8.1f}        {: <8f}{: <8.1f}0.00\n".format(a2 + 300011, bd.X2, coy_kont))
            file.write("\n\n")

            # Запись CELAS1 узлов скольжения

            file.write(
                "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a1 + 200001, a1 + 1, a1 + 200001))
            file.write(
                "CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a2 + 200001, a2 + 1, a2 + 200001))
            file.write("\n\n")

            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a1 + 200011, a1 + 200011,
                                                                                        a1 + 300011))
            file.write("CELAS1  {: <8.1f}2       {: <8.1f}2       {: <8.1f}2\n".format(a2 + 200011, a2 + 200011,
                                                                                        a2 + 300011))
            file.write("\n\n")

            # Запись PELAS узлов скольжения (жесткость?)

            file.write("PELAS   2       {: <8.1f}+6\n\n".format(bd.zhestkost_amort))

            # Запись RBE2 узлов скольжения

            i1 = 1

            file.write(
                "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(a1 + 400001, a1 + 1, i1,
                                                                                            a1 + 200001, a1 + 200011,
                                                                                            a1 + 300011))
            file.write(
                "RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}{: <8.1f}{: <8.1f}\n".format(a2 + 400001, a2 + 1, i1,
                                                                                            a2 + 200001, a2 + 200011,
                                                                                            a2 + 300011))
            file.write("\n\n")

            i2 = 2

            file.write("RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(a1 + 400011, a1 + 1, i2, a1 + 300011))
            file.write("RBE2    {: <8.1f}{: <8.1f} {: <8d}{: <8.1f}\n".format(a2 + 400011, a2 + 1, i2, a2 + 300011))
            file.write("\n\n")

            # Запись BLSEG

            file.write("BLSEG   1       {: <8.1f}{: <8.1f}\n".format(a1 + 1, a1 + 200001))
            file.write("BLSEG   3       {: <8.1f}{: <8.1f}\n".format(a2 + 1, a2 + 200001))
            file.write("\n")

            file.write("BLSEG   7       {: <8.1f}{: <8.1f}\n".format(a1 + 300011, a1 + 200011))
            file.write("BLSEG   8       {: <8.1f}{: <8.1f}\n".format(a2 + 300011, a2 + 200011))
            file.write("\n\n")

            # Запись BCONP

            file.write("BCONP   1       1       2               1.0     10      1       1\n")
            file.write("BCONP   2       3       2               1.0     10      1       1\n")
            file.write("\n")

            file.write("BCONP   6       7       2               1.0     10      1       3\n")
            file.write("BCONP   7       8       2               1.0     10      1       3\n")

            # Запись SPC опорных узлов контейнера

            file.write("\n\n")
            file.write("SPC     10      {: <8.1f}23456\n".format(a1 + 100001))
            file.write("SPC     10      {: <8.1f}23456\n".format(a2 + 100001))

        file.write("\n\n")

        # Запись BLSEG

        file.write("BLSEG   2       100001  THRU    {: <8.1f}".format(float(bd.N) + 100010))
        file.write("\n\n")

        # Запись BFRIC

        file.write("BFRIC   10                      0.1")
        file.write("\n\n")

        # Запись CORD2R

        file.write(
            "CORD2R  1               0.0     1.1     0.0     0.0     1.1     -1.0\n        1.0     1.1     0.0")
        file.write("\n\n")

        # Запись CORD2R

        file.write(
            "CORD2R  3               0.0     -1.1    0.0     0.0     -1.1    1.0\n        1.0     -1.1    0.0")
        file.write("\n\n")

        # Запись TABLED1 (тяга)
        if (bd.P12 < 10000000 and bd.P12 > 1000000 or bd.P12 == 1000000):

            file.write("TABLED1 411\n        0.0     0.0     1.0     0.0     {: <8.3f}{: <8.5f}{: <8.3f}{: <8.5f}\n".format(bd.t_p1, bd.P1, bd.t_p2, bd.P2))
            file.write("        {: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}\n".format(bd.t_p3, bd.P3, bd.t_p4, bd.P4, bd.t_p5, bd.P5, bd.t_p6, bd.P6))
            file.write("        {: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}\n".format(bd.t_p7, bd.P7, bd.t_p8, bd.P8, bd.t_p9, bd.P9, bd.t_p10, bd.P10))
            file.write("        {: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}ENDT\n".format(bd.t_p11, bd.P11, bd.t_p12, bd.P12, bd.t_p13, bd.P13))

        elif (bd.P12 > 100000 or bd.P12 == 100000 and bd.P12 < 1000000):

            file.write("TABLED1 411\n        0.0     0.0     1.0     0.0     {: <8.3f}{: <8.0f}{: <8.3f}{: <8.0f}\n".format(bd.t_p1, bd.P1, bd.t_p2, bd.P2))
            file.write("        {: <8.3f}{: <8.0f}{: <8.3f}{: <8.0f}{: <8.3f}{: <8.0f}{: <8.3f}{: <8.0f}\n".format(bd.t_p3, bd.P3, bd.t_p4, bd.P4, bd.t_p5, bd.P5, bd.t_p6, bd.P6))
            file.write("        {: <8.3f}{: <8.0f}{: <8.3f}{: <8.0f}{: <8.3f}{: <8.0f}{: <8.3f}{: <8.0f}\n".format(bd.t_p7, bd.P7, bd.t_p8, bd.P8, bd.t_p9, bd.P9, bd.t_p10, bd.P10))
            file.write("        {: <8.3f}{: <8.0f}{: <8.3f}{: <8.0f}{: <8.3f}{: <8.0f}ENDT\n".format(bd.t_p11, bd.P11, bd.t_p12, bd.P12, bd.t_p13, bd.P13))

        elif (bd.P12 < 100000 and bd.P12 > 10000 or bd.P12 == 10000):

            file.write("TABLED1 411\n        0.0     0.0     1.0     0.0     {: <8.3f}{: <8.1f}{: <8.3f}{: <8.1f}\n".format(bd.t_p1, bd.P1, bd.t_p2, bd.P2))
            file.write("        {: <8.3f}{: <8.1f}{: <8.3f}{: <8.1f}{: <8.3f}{: <8.1f}{: <8.3f}{: <8.1f}\n".format(bd.t_p3, bd.P3, bd.t_p4, bd.P4, bd.t_p5, bd.P5, bd.t_p6, bd.P6))
            file.write("        {: <8.3f}{: <8.1f}{: <8.3f}{: <8.1f}{: <8.3f}{: <8.1f}{: <8.3f}{: <8.1f}\n".format(bd.t_p7, bd.P7, bd.t_p8, bd.P8, bd.t_p9, bd.P9, bd.t_p10, bd.P10))
            file.write("        {: <8.3f}{: <8.1f}{: <8.3f}{: <8.1f}{: <8.3f}{: <8.1f}ENDT\n".format(bd.t_p11, bd.P11, bd.t_p12, bd.P12, bd.t_p13, bd.P13))

        elif (bd.P12 > 1000 and bd.P12 < 10000 or bd.P12 == 1000):

            file.write("TABLED1 411\n        0.0     0.0     1.0     0.0     {: <8.3f}{: <8.2f}{: <8.3f}{: <8.2f}\n".format(bd.t_p1, bd.P1, bd.t_p2, bd.P2))
            file.write("        {: <8.3f}{: <8.2f}{: <8.3f}{: <8.2f}{: <8.3f}{: <8.2f}{: <8.3f}{: <8.2f}\n".format(bd.t_p3, bd.P3, bd.t_p4, bd.P4, bd.t_p5, bd.P5, bd.t_p6, bd.P6))
            file.write("        {: <8.3f}{: <8.2f}{: <8.3f}{: <8.2f}{: <8.3f}{: <8.2f}{: <8.3f}{: <8.2f}\n".format(bd.t_p7, bd.P7, bd.t_p8, bd.P8, bd.t_p9, bd.P9, bd.t_p10, bd.P10))
            file.write("        {: <8.3f}{: <8.2f}{: <8.3f}{: <8.2f}{: <8.3f}{: <8.2f}ENDT\n".format(bd.t_p11, bd.P11, bd.t_p12, bd.P12, bd.t_p13, bd.P13))

        elif (bd.P12 > 10000000 and bd.P12 < 100000000 or bd.P12 == 10000000):

            file.write("TABLED1 411\n        0.0     0.0     1.0     0.0     {: <8.3f}{: <8.5f}{: <8.3f}{: <8.5f}\n".format(bd.t_p1, bd.P1 / 1000, bd.t_p2, bd.P2 / 1000))
            file.write("        {: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}\n".format(bd.t_p3, bd.P3 / 1000, bd.t_p4, bd.P4 / 1000, bd.t_p5, bd.P5 / 1000, bd.t_p6, bd.P6 / 1000))
            file.write("        {: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}\n".format(bd.t_p7, bd.P7 / 1000, bd.t_p8, bd.P8 / 1000, bd.t_p9, bd.P9 / 1000, bd.t_p10, bd.P10 / 1000))
            file.write("        {: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}{: <8.3f}{: <8.4f}ENDT\n".format(bd.t_p11, bd.P11 / 1000, bd.t_p12, bd.P12 / 1000, bd.t_p13, bd.P13 / 1000))

        else:

            file.write("TABLED1 411\n        0.0     0.0     1.0     0.0     {: <8.3f}{: <7.4f}{: <8.3f}{: <7.4f}\n".format(bd.t_p1, bd.P1, bd.t_p2, bd.P2))
            file.write("        {: <8.3f}{: <7.4f}{: <8.3f}{: <7.4f}{: <8.3f}{: <7.4f}{: <8.3f}{: <7.4f}\n".format(bd.t_p3, bd.P3, bd.t_p4, bd.P4, bd.t_p5, bd.P5, bd.t_p6, bd.P6))
            file.write("        {: <8.3f}{: <7.4f}{: <8.3f}{: <7.4f}{: <8.3f}{: <7.4f}{: <8.3f}{: <7.4f}\n".format(bd.t_p7, bd.P7, bd.t_p8, bd.P8, bd.t_p9, bd.P9, bd.t_p10, bd.P10))
            file.write("        {: <8.3f}{: <7.4f}{: <8.3f}{: <7.4f}{: <8.3f}{: <7.4f}ENDT\n".format(bd.t_p11, bd.P11, bd.t_p12, bd.P12, bd.t_p13, bd.P13))

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
        plotnost1 = massa_korpusa / (((Decimal('3.14') * bd.d0 * bd.d0 / Decimal('4')) - (Decimal('3.14') * (bd.d0 - Decimal('0.003')) * (bd.d0 - Decimal('0.003')) / Decimal('4'))) * bd.L)

        file.write("MAT1    1       {: <2.1f}+10          {: <8.2f}{: <8.1f}\n".format(bd.modul_unga1, bd.koeff_puass1, plotnost1))
        file.write("MAT1    2       {: <2.1f}+10          {: <8.2f}{: <8.3f}".format(bd.modul_unga2, bd.koeff_puass2, bd.plotnost2))
        file.write("\n\n")

        # Запись PBARL

        file.write("PBARL   1       1               TUBE2\n        {: <8.2f}0.003".format(bd.d0))
        file.write("\n")
        file.write("PBARL   2       2               TUBE2\n        {: <8.2f}0.0175".format(bd.d0 + Decimal('0.2')))
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

        file.write("GRID    9000            0.0     {: <8.3f}0.0".format((bd.d0 / 2) + Decimal('0.1')))
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
        n_time = Decimal(n_time)
        t_shoda = (bd.t / n_time)  # время схода поясов амортизации

        file.write("TSTEPNL 1       10      0.1     1       ADAPT\n")
        file.write("TSTEPNL 2       {: <8.0f}{: <8.3f}1       ADAPT\n".format(t_shoda, n_time))
        file.write("\n\n")

        file.write("ENDDATA")

        file.close()


        serializer = bdfSerializer(bd)
        return Response(serializer.data, status=HTTP_200_OK)


