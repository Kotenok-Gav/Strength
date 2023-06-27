import { useEffect, useState } from "react";
import axios from "axios";
import Tool from "../components/input/Tooltip";

function Forms() {
  const [bdf, setBdf] = useState([]);

// 1 ------------ 
  const [text, setText] = useState("Ангара");
  const [start_rocket, setStart_rocket] = useState(1);
  const [t, sett] = useState(5.673);

// 2 ------------ 
  const [d0, setd0] = useState(3.03);
  const [tol_R, settol_R] = useState(0.007);
  const [L, setL] = useState(21.6);
  const [d0_Kon, setd0_Kon] = useState(3.25);
  const [tol_Kon, settol_Kon] = useState(0.004);
  const [L_Kon, setL_Kon] = useState(25.0);

// 3 ------------ 
  const [kolichestvo_amort, setkolichestvo_amort] = useState(2);
  const [zhestkost_amort, setzhestkost_amort] = useState(567.4);
  const [X1, setX1] = useState(19.5);
  const [X2, setX2] = useState(8.4);
  const [X3, setX3] = useState(2.9);
  const [X4, setX4] = useState();
  const [X5, setX5] = useState();

// 4 ------------ 
  const [V_sredy, setV_sredy] = useState(25);
  const [t_p1 , sett_p1] = useState(0.11);
  const [P1 , setP1] = useState(3676743);
  const [t_p2 , sett_p2] = useState(0.25);
  const [P2 , setP2] = useState(6120857);
  const [t_p3 , sett_p3] = useState(0.5);
  const [P3 , setP3] = useState(9001571);
  const [t_p4 , sett_p4] = useState(0.68);
  const [P4 , setP4] = useState(10460429);
  const [t_p5 , sett_p5] = useState(0.86);
  const [P5 , setP5] = useState(9598857);
  const [t_p6 , sett_p6] = useState(1.00);
  const [P6 , setP6] = useState(10761714);
  const [t_p7 , sett_p7] = useState(1.34);
  const [P7 , setP7] = useState(11697286);
  const [t_p8 , sett_p8] = useState(1.97);
  const [P8 , setP8] = useState(11401286);
  const [t_p9 , sett_p9] = useState(2.42);
  const [P9 , setP9] = useState(10804000);
  const [t_p10 , sett_p10] = useState(3.03);
  const [P10 , setP10] = useState(9313429);
  const [t_p11 , sett_p11] = useState(3.46);
  const [P11 , setP11] = useState(8055429);
  const [t_p12 , sett_p12] = useState(3.68);
  const [P12 , setP12] = useState(7178000);
  const [t_p13 , sett_p13] = useState(3.80);
  const [P13 , setP13] = useState(0);

// 5 ------------ 
  const [m , setm] = useState(120000.6);
  const [m_gch , setm_gch] = useState(20000.6);
  const [X_gch , setX_gch] = useState(19.6);
  const [m_cy , setm_cy] = useState(500.6);
  const [X_cy , setX_cy] = useState(17.2);
  const [m_dy_1 , setm_dy_1] = useState(15000.2);
  const [X_dy_1 , setX_dy_1] = useState(2.1);
  const [mo_1 , setmo_1] = useState(45000.5);
  const [Lo_1 , setLo_1] = useState(8.2);
  const [Xo_1 , setXo_1] = useState(8.2);
  const [mg_1 , setmg_1] = useState(15000.9);
  const [Lg_1 , setLg_1] = useState(3.7);
  const [Xg_1 , setXg_1] = useState(4.0);
  const [L_kon_zakr_1 , setL_kon_zakr_1] = useState(0.0);
  const [tip_zakr_1 , settip_zakr_1] = useState(1345);
  const [L_kon_zakr_2 , setL_kon_zakr_2] = useState(6.8);
  const [tip_zakr_2 , settip_zakr_2] = useState(2345);
  const [L_kon_zakr_3 , setL_kon_zakr_3] = useState(19.3);
  const [tip_zakr_3 , settip_zakr_3] = useState(2345);
  const [L_kon_zakr_4 , setL_kon_zakr_4] = useState();
  const [tip_zakr_4 , settip_zakr_4] = useState();
  const [L_kon_zakr_5 , setL_kon_zakr_5] = useState();
  const [tip_zakr_5 , settip_zakr_5] = useState();

// 6 ------------ 
  const [modul_unga1 , setmodul_unga1] = useState(70000);
  const [koeff_puass1 , setkoeff_puass1] = useState(0.3);
  const [modul_unga2 , setmodul_unga2] = useState(7000);
  const [koeff_puass2 , setkoeff_puass2] = useState(0.3);
  const [plotnost2 , setplotnost2] = useState(2000);


  const handleDownload = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/download/', {
        responseType: 'blob', // Указываем, что ожидаем получить blob-объект в ответе
      });
  
      // Создаем ссылку для скачивания файла
      const url = window.URL.createObjectURL(new Blob([response.data]));
  
      // Создаем временную ссылку и автоматически запускаем скачивание
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', '1.txt');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } catch (error) {
      console.error('Ошибка при скачивании файла:', error);
    }
  };
  


  const addBdfHandler = () => {
    const postBdf = async () => {
      const postBdfdata = {

// 1 ------------ 
        text: text,
        start_rocket: start_rocket,
        t: t,

// 2 ------------ 
        d0:d0,
        tol_R:tol_R,
        L:L,
        d0_Kon:d0_Kon,
        tol_Kon:tol_Kon,
        L_Kon:L_Kon,

// 3 ------------ 
        kolichestvo_amort:kolichestvo_amort,
        zhestkost_amort:zhestkost_amort,
        X1:X1,
        X2:X2,
        X3:X3,
        X4:X4,
        X5:X5,

// 4 ------------ 
        V_sredy:V_sredy,
        t_p1:t_p1,
        P1:P1,
        t_p2:t_p2,
        P2:P2,
        t_p3:t_p3,
        P3:P3,
        t_p4:t_p4,
        P4:P4,
        t_p5:t_p5,
        P5:P5,
        t_p6:t_p6,
        P6:P6,
        t_p7:t_p7,
        P7:P7,
        t_p8:t_p8,
        P8:P8,
        t_p9:t_p9,
        P9:P9,
        t_p10:t_p10,
        P10:P10,
        t_p11:t_p11,
        P11:P11,
        t_p12:t_p12,
        P12:P12,
        t_p13:t_p13,
        P13:P13,

// 5 ------------
        m:m,
        m_gch:m_gch,
        X_gch:X_gch,
        m_cy:m_cy,
        X_cy:X_cy,
        m_dy_1:m_dy_1,
        X_dy_1:X_dy_1,
        mo_1:mo_1,
        Lo_1:Lo_1,
        Xo_1:Xo_1,
        mg_1:mg_1,
        Lg_1:Lg_1,
        Xg_1:Xg_1,
        L_kon_zakr_1:L_kon_zakr_1,
        tip_zakr_1:tip_zakr_1,
        L_kon_zakr_2:L_kon_zakr_2,
        tip_zakr_2:tip_zakr_2,
        L_kon_zakr_3:L_kon_zakr_3,
        tip_zakr_3:tip_zakr_3,
        L_kon_zakr_4:L_kon_zakr_4,
        tip_zakr_4:tip_zakr_4,
        L_kon_zakr_5:L_kon_zakr_5,
        tip_zakr_5:tip_zakr_5,

// 6 ------------ 
        modul_unga1:modul_unga1,
        koeff_puass1:koeff_puass1,
        modul_unga2:modul_unga2,
        koeff_puass2:koeff_puass2,
        plotnost2:plotnost2,

      };
      const { data } = await axios.post(
        "http://127.0.0.1:8000/bdf/",
        postBdfdata
      );
      setBdf([...bdf, data]);

// 1 ------------ 
      setText("");
      setStart_rocket("");
      sett("");

// 2 ------------ 
      setd0("");
      settol_R("");
      setL("");
      setd0_Kon("");
      settol_Kon("");
      setL_Kon("");

// 3 ------------ 
      setkolichestvo_amort("");
      setzhestkost_amort("");
      setX1("");
      setX2("");
      setX3("");
      setX4("");
      setX5("");

// 4 ------------ 
      setV_sredy("");
      sett_p1("");
      setP1("");
      sett_p2("");
      setP2("");
      sett_p3("");
      setP3("");
      sett_p4("");
      setP4("");
      sett_p5("");
      setP5("");
      sett_p6("");
      setP6("");
      sett_p7("");
      setP7("");
      sett_p8("");
      setP8("");
      sett_p9("");
      setP9("");
      sett_p10("");
      setP10("");
      sett_p11("");
      setP11("");
      sett_p12("");
      setP12("");
      sett_p13("");
      setP13("");

// 5 ------------
      setm("");
      setm_gch("");
      setX_gch("");
      setm_cy("");
      setX_cy("");
      setm_dy_1("");
      setX_dy_1("");
      setmo_1("");
      setLo_1("");
      setXo_1("");
      setmg_1("");
      setLg_1("");
      setXg_1("");
      setL_kon_zakr_1("");
      settip_zakr_1("");
      setL_kon_zakr_2("");
      settip_zakr_2("");
      setL_kon_zakr_3("");
      settip_zakr_3("");
      setL_kon_zakr_4("");
      settip_zakr_4("");
      setL_kon_zakr_5("");
      settip_zakr_5("");

// 6 ------------ 
      setmodul_unga1("");
      setkoeff_puass1("");
      setmodul_unga2("");
      setkoeff_puass2("");
      setplotnost2(""); 
    };
    postBdf();
  };

  useEffect(() => {
    const fetchBdf = async () => {
      const { data } = await axios.get("http://127.0.0.1:8000/bdf/");
      setBdf(data);
    };
    fetchBdf();
  }, []);

  return (
    <div className="section">
      <div className="container">
        <div className="flex flex-col w-full p-10">
          <h1 className="text-3xl text-center pb-5">BDF файл</h1>

{/* 1 ------------------------------------------------------------------ */}

          <p className="pb-3 pl-5 text-2xl">1  Общие данные</p>
          {/* ------------------------------------------------------------------ */}
          {/* 1.1 */}
          <p className="pb-3 pl-5 text-xl">1.1  Название проекта</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={text}
              onChange={e => setText(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="Ангара"
            />
            <Tool text="Укажите название проекта"></Tool>
          </div>

          <br></br>

          {/* 1.2 */}
          <p className="pb-3 pl-5 text-xl">1.2 Определение старта ракеты</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={start_rocket}
              onChange={e => setStart_rocket(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="0"
            />
            <Tool text="Введите 0, если старт подводный,     1 - наземный"></Tool>
          </div>

          <br></br>

          {/* 1.3 */}
          <p className="pb-3 pl-5 text-xl">1.3 Время выхода ракеты из контейнера в секундах </p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t}
              onChange={e => sett(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="5.673"
            />
            <Tool text="c точностью до тысячных"></Tool>
          </div>

          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <br></br>


{/* 2 ------------------------------------------------------------------ */}

          <p className="pb-3 pl-5 text-2xl">2  Геометрические характеристики</p>
          {/* ------------------------------------------------------------------ */}
          {/* 2.1.1 */}
          <p className="pb-3 pl-5 text-xl">2.1.1 Диаметр ракеты</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={d0}
              onChange={e => setd0(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="3.03"
            />
            <Tool text="м, с точностью до сотых"></Tool>
          </div>

          <br></br>

          {/* 2.1.2 */}
          <p className="pb-3 pl-5 text-xl">2.1.2 Эквивалентная толщина стенки ракеты </p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={tol_R}
              onChange={e => settol_R(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="0.007"
            />
            <Tool text="м, с точностью до тысячных"></Tool>
          </div>

          <br></br>

          {/* 2.1.3 */}
          <p className="pb-3 pl-5 text-xl">2.1.3 Длина ракеты</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={L}
              onChange={e => setL(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="21.6"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          {/* 2.2.1 */}
          <p className="pb-3 pl-5 text-xl">2.2.1 Диаметр контейнера</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={d0_Kon}
              onChange={e => setd0_Kon(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="3.25"
            />
            <Tool text="м, с точностью до сотых"></Tool>
          </div>

          <br></br>

          {/* 2.2.2 */}
          <p className="pb-3 pl-5 text-xl">2.2.2 Эквивалентная толщина стенки контейнера </p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={tol_Kon}
              onChange={e => settol_Kon(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="0.004"
            />
            <Tool text="м, с точностью до тысячных"></Tool>
          </div>

          <br></br>

          {/* 2.2.3 */}
          <p className="pb-3 pl-5 text-xl">2.2.3 Длина контейнера</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={L_Kon}
              onChange={e => setL_Kon(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="25.0"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <br></br>


{/* 3 ------------------------------------------------------------------ */}


          <p className="pb-3 pl-5 text-2xl">3  Геометрические характеристики</p>
          {/* ------------------------------------------------------------------ */}
          {/* 3.1 */}
          <p className="pb-3 pl-5 text-xl">3.1 Количество опорно-ведущих поясов (ОВП)</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={kolichestvo_amort}
              onChange={e => setkolichestvo_amort(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="1"
            />
            <Tool text="Введите число от 1 до 5"></Tool>
          </div>

          <br></br>

          {/* 3.2 */}
          <p className="pb-3 pl-5 text-xl">3.2 Жесткость ОВП</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={zhestkost_amort}
              onChange={e => setzhestkost_amort(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="567.4"
            />
            <Tool text="МН/м (с точностью до десятых)"></Tool>
          </div>

          <br></br>

          {/* 3.3.1 */}
          <p className="pb-3 pl-5 text-xl">3.3.1 Расстояние: от нижнего края ракеты до верхнего (первого) пояса амортизации</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={X1}
              onChange={e => setX1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="10.5"
            />
            <Tool text="в м с точностью до десятых"></Tool>
          </div>

          <br></br>

          {/* 3.3.2 */}
          <p className="pb-3 pl-5 text-xl">3.3.2 Расстояние: от нижнего края ракеты до второго пояса амортизации</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={X2}
              onChange={e => setX2(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="8.4"
            />
            <Tool text="в м с точностью до десятых"></Tool>
          </div>

          <br></br>

          {/* 3.3.3 */}
          <p className="pb-3 pl-5 text-xl">3.3.3 Расстояние: от нижнего края ракеты до третьего пояса амортизации</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={X3}
              onChange={e => setX3(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="6.9"
            />
            <Tool text="в м с точностью до десятых"></Tool>
          </div>

          <br></br>

          {/* 3.3.4 */}
          <p className="pb-3 pl-5 text-xl">3.3.4 Расстояние: от нижнего края ракеты до четвертого пояса амортизации</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={X4}
              onChange={e => setX4(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="5.1"
            />
            <Tool text="в м с точностью до десятых"></Tool>
          </div>

          <br></br>

          {/* 3.3.5 */}
          <p className="pb-3 pl-5 text-xl">3.3.5 Расстояние: от нижнего края ракеты до пятого пояса амортизации</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={X5}
              onChange={e => setX5(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="3.7"
            />
            <Tool text="в м с точностью до десятых"></Tool>
          </div>

          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <br></br>


{/* 4 ------------------------------------------------------------------ */}


          <p className="pb-3 pl-5 text-2xl">4  Граничные и начальные условия</p>
          {/* ------------------------------------------------------------------ */}
          {/* 4.1 */}
          <p className="pb-3 pl-5 text-xl">4.1 Скорость бокового набегающего потока</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={V_sredy}
              onChange={e => setV_sredy(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="32.4"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>
          <br></br>


          {/* 4.2 */}
          <p className="pb-3 pl-5 text-xl">4.2 Задание тяги двигателя (Н) в зависимости от времени (с)</p>
          <p className="pb-3 pl-5 text-xl">Время 1 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p1}
              onChange={e => sett_p1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="0.11"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 1 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P1}
              onChange={e => setP1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="3676743"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 2 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p2}
              onChange={e => sett_p2(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="0.25"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 2 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P2}
              onChange={e => setP2(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="6120857"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 3 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p3}
              onChange={e => sett_p3(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="0.5"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 3 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P3}
              onChange={e => setP3(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="9001571"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 4 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p4}
              onChange={e => sett_p4(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="0.68"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 4 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P4}
              onChange={e => setP4(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="10460429"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 5 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p5}
              onChange={e => sett_p5(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="0.86"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 5 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P5}
              onChange={e => setP5(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="9598857"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 6 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p6}
              onChange={e => sett_p6(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="1.00"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 6 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P6}
              onChange={e => setP6(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="10761714"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 7 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p7}
              onChange={e => sett_p7(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="1.34"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 7 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P7}
              onChange={e => setP7(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="11697286"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 8 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p8}
              onChange={e => sett_p8(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="1.97"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 8 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P8}
              onChange={e => setP8(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="11401286"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 9 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p9}
              onChange={e => sett_p9(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="2.42"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 9 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P9}
              onChange={e => setP9(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="10804000"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 10 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p10}
              onChange={e => sett_p10(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="3.03"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 10 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P10}
              onChange={e => setP10(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="9313429"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 11 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p11}
              onChange={e => sett_p11(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="3.46"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 11 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P11}
              onChange={e => setP11(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="8055429"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 12 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p12}
              onChange={e => sett_p12(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="3.68"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 12 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P12}
              onChange={e => setP12(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="7178000"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Время 13 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={t_p13}
              onChange={e => sett_p13(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="3.80"
            />
            <Tool text="м/с"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">Тяга 13 точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={P13}
              onChange={e => setP13(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="0"
            />
            <Tool text="Н"></Tool>
          </div>

          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <br></br>

{/* 5 ------------------------------------------------------------------ */}


          <p className="pb-3 pl-5 text-2xl">5 Распределение масс конструкции</p>
          {/* ------------------------------------------------------------------ */}
          {/* 5.1 */}
          <p className="pb-3 pl-5 text-xl">5.1 Стартовая масса ракеты</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={m}
              onChange={e => setm(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="120 000.6"
            />
            <Tool text="кг, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.2 Масса ГЧ</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={m_gch}
              onChange={e => setm_gch(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="20 000.6"
            />
            <Tool text="кг, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.3 Расстояние от нижнего края ракеты до точки приложения массы ГЧ</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={X_gch}
              onChange={e => setX_gch(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="9.6"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.4 Масса СУ ракеты</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={m_cy}
              onChange={e => setm_cy(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="17 000.6"
            />
            <Tool text="кг, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.5 Расстояние от нижнего края ракеты до точки приложения массы СУ</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={X_cy}
              onChange={e => setX_cy(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="8.9"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.6 Масса ДУ 1 ступени</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={m_dy_1}
              onChange={e => setm_dy_1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="23 000.2"
            />
            <Tool text="кг, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.7 Расстояние от нижнего края ракеты до точки приложения массы ДУ 1 ступени</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={X_dy_1}
              onChange={e => setX_dy_1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="1.1"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.8 Масса окислителя 1 ступени</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={mo_1}
              onChange={e => setmo_1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="24 000.5"
            />
            <Tool text="кг, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.9 Длина бака окислителя 1 ступени</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={Lo_1}
              onChange={e => setLo_1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="3.2"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.10 Расстояние от нижнего края ракеты до нижнего днища бака окислителя 1 ступени</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={Xo_1}
              onChange={e => setXo_1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="5.2"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.11 Масса горючего 1 ступени</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={mg_1}
              onChange={e => setmg_1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="25 000.9"
            />
            <Tool text="кг, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.12 Длина бака горючего 1 ступени</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={Lg_1}
              onChange={e => setLg_1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="3.7"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.13 Расстояние от нижнего края ракеты до нижнего днища бака горючего 1 ступени</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={Xg_1}
              onChange={e => setXg_1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="2.0"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.14.1 Расстояние от нижнего края контейнера до первой точки крепления</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={L_kon_zakr_1}
              onChange={e => setL_kon_zakr_1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="0.0"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.14.2 Тип закрепления первой точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={tip_zakr_1}
              onChange={e => settip_zakr_1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="1345"
            />
            <Tool text="Вертикальное(1345), Горизонтальное(2345), Заделка(123456)"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.15.1 Расстояние от нижнего края контейнера до второй точки крепления</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={L_kon_zakr_2}
              onChange={e => setL_kon_zakr_2(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="2.8"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.15.2 Тип закрепления второй точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={tip_zakr_2}
              onChange={e => settip_zakr_2(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="1345"
            />
            <Tool text="Вертикальное(1345), Горизонтальное(2345), Заделка(123456)"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.16.1 Расстояние от нижнего края контейнера до третьей точки крепления</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={L_kon_zakr_3}
              onChange={e => setL_kon_zakr_3(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="6.3"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.16.2 Тип закрепления третьей точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={tip_zakr_3}
              onChange={e => settip_zakr_3(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="1345"
            />
            <Tool text="Вертикальное(1345), Горизонтальное(2345), Заделка(123456)"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.17.1 Расстояние от нижнего края контейнера до четвертой точки крепления</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={L_kon_zakr_4}
              onChange={e => setL_kon_zakr_4(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="9.3"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.17.2 Тип закрепления четвертой точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={tip_zakr_4}
              onChange={e => settip_zakr_4(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="1345"
            />
            <Tool text="Вертикальное(1345), Горизонтальное(2345), Заделка(123456)"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.18.1 Расстояние от нижнего края контейнера до пятой точки крепления</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={L_kon_zakr_5}
              onChange={e => setL_kon_zakr_5(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="13.5"
            />
            <Tool text="м, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">5.18.2 Тип закрепления пятой точки</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={tip_zakr_5}
              onChange={e => settip_zakr_5(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="1345"
            />
            <Tool text="Вертикальное(1345), Горизонтальное(2345), Заделка(123456)"></Tool>
          </div>

          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <br></br>

{/* 6 ------------------------------------------------------------------ */}


          <p className="pb-3 pl-5 text-2xl">6 Свойства конструкционных материалов</p>
          <p className="pb-3 pl-5 text-2xl">6.1 Ракета</p>
          {/* ------------------------------------------------------------------ */}
          {/* 6.1 */}
          <p className="pb-3 pl-5 text-xl">6.1.1 Модуль Юнга (упругости)</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={modul_unga1}
              onChange={e => setmodul_unga1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="234.5"
            />
            <Tool text="МПа, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">6.1.2 Коэффициент Пуассона</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={koeff_puass1}
              onChange={e => setkoeff_puass1(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="7.45"
            />
            <Tool text="с точностью до сотых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-2xl">6.2 Контейнер</p>
          <p className="pb-3 pl-5 text-xl">6.2.1 Модуль Юнга (упругости)</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={modul_unga2}
              onChange={e => setmodul_unga2(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="682.4"
            />
            <Tool text="МПа, с точностью до десятых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">6.2.2 Коэффициент Пуассона</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={koeff_puass2}
              onChange={e => setkoeff_puass2(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="6.28"
            />
            <Tool text="с точностью до сотых"></Tool>
          </div>

          <br></br>

          <p className="pb-3 pl-5 text-xl">6.2.3 Плотность</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={plotnost2}
              onChange={e => setplotnost2(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="349"
            />
            <Tool text="кг/м3 точностью до целых"></Tool>
          </div>






          <button
                onClick={addBdfHandler}
                className="p-5 rounded-3xl bg-slate-700  hover:bg-sky-700 text-xl mx-60 mt-20">
                Создать
          </button>


          

          <button
                onClick={handleDownload}
                className="p-5 rounded-3xl bg-slate-700  hover:bg-sky-700 text-xl mx-60 mt-20">
                Скачать
          </button>



          <div className="mt-5 flex flex-col space-y-5 sm:space-y-0 sm:grid sm:grid-cols-2 sm:gap-10 lg:grid-cols-3">
            {bdf?.map((bdf, index) => (
              <div
                key={bdf.id}
                className="max-w-md mx-auto w-full p-5 h-full rounded-xl bg-blue-500 flex items-center justify-between"
              >
                <p>{bdf.text}</p>
                <p>{bdf.start_rocket}</p>
                <p>{bdf.t}</p>
                <p>{bdf.d0}</p>
                <p>{bdf.tol_R}</p>
                <p>{bdf.L}</p>
                <p>{bdf.d0_Kon}</p>
                <p>{bdf.tol_Kon}</p>
                <p>{bdf.L_Kon}</p>
                <p>{bdf.kolichestvo_amort}</p>
                <p>{bdf.zhestkost_amort}</p>
                <p>{bdf.X1}</p>
                <p>{bdf.X2}</p>
                <p>{bdf.X3}</p>
                <p>{bdf.X4}</p>
                <p>{bdf.X5}</p>

                <p>{bdf.V_sredy}</p>
                <p>{bdf.t_p0}</p>
                <p>{bdf.P0}</p>
                <p>{bdf.t_p1}</p>
                <p>{bdf.P1}</p>
                <p>{bdf.t_p2}</p>
                <p>{bdf.P2}</p>
                <p>{bdf.t_p3}</p>
                <p>{bdf.P3}</p>
                <p>{bdf.t_p4}</p>
                <p>{bdf.P4}</p>
                <p>{bdf.t_p5}</p>
                <p>{bdf.P5}</p>
                <p>{bdf.t_p6}</p>
                <p>{bdf.P6}</p>
                <p>{bdf.t_p7}</p>
                <p>{bdf.P7}</p>
                <p>{bdf.t_p8}</p>
                <p>{bdf.P8}</p>
                <p>{bdf.t_p9}</p>
                <p>{bdf.P9}</p>
                <p>{bdf.t_p10}</p>
                <p>{bdf.P10}</p>
                <p>{bdf.t_p11}</p>
                <p>{bdf.P11}</p>
                <p>{bdf.t_p12}</p>
                <p>{bdf.P12}</p>
                <p>{bdf.t_p13}</p>
                <p>{bdf.P13}</p>

                <p>{bdf.dl_1}</p>
                <p>{bdf.nap_zak_1}</p>
                <p>{bdf.zhestkost_opor_1}</p>

                <p>{bdf.dl_2}</p>
                <p>{bdf.nap_zak_2}</p>
                <p>{bdf.zhestkost_opor_2}</p>

                <p>{bdf.dl_3}</p>
                <p>{bdf.nap_zak_3}</p>
                <p>{bdf.zhestkost_opor_3}</p>

                <p>{bdf.m}</p>
                <p>{bdf.m_gch}</p>
                <p>{bdf.X_gch}</p>
                <p>{bdf.m_cy}</p>
                <p>{bdf.X_cy}</p>
                <p>{bdf.m_dy_1}</p>
                <p>{bdf.X_dy_1}</p>
                <p>{bdf.mo_1}</p>
                <p>{bdf.Lo_1}</p>
                <p>{bdf.Xo_1}</p>
                <p>{bdf.mg_1}</p>
                <p>{bdf.Lg_1}</p>
                <p>{bdf.Xg_1}</p>

                <p>{bdf.modul_unga1}</p>
                <p>{bdf.koeff_puass1}</p>
                <p>{bdf.modul_unga2}</p>
                <p>{bdf.koeff_puass2}</p>
                <p>{bdf.plotnost2}</p>

              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Forms;
