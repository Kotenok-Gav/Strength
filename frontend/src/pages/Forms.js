import { useEffect, useState } from "react";
import axios from "axios";
import Tool from "../components/input/Tooltip";

function Forms() {
  const [bdf, setBdf] = useState([]);

  const [text, setText] = useState();
  const [start_rocket, setStart_rocket] = useState();
  const [t, sett] = useState();
  const [d0, setd0] = useState();
  const [tol_R, settol_R] = useState();
  const [L, setL] = useState();
  const [d0_Kon, setd0_Kon] = useState();
  const [tol_Kon, settol_Kon] = useState();
  const [L_Kon, setL_Kon] = useState();

  const addBdfHandler = () => {
    const postBdf = async () => {
      const postBdfdata = {
        text: text,
        start_rocket: start_rocket,
        t: t,
        d0:d0,
        tol_R:tol_R,
        L:L,
        d0_Kon:d0_Kon,
        tol_Kon:tol_Kon,
        L_Kon:L_Kon
      };
      const { data } = await axios.post(
        "http://127.0.0.1:8000/bdf/",
        postBdfdata
      );
      setBdf([...bdf, data]);
      setText("");
      setStart_rocket("");
      sett("");
      setd0("");
      settol_R("");
      setL("");
      setd0_Kon("");
      settol_Kon("");
      setL_Kon("");
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






















          <button
                onClick={addBdfHandler}
                className="p-5 rounded-3xl bg-slate-700  hover:bg-sky-700 text-xl mx-60 mt-20">
                Создать
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
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Forms;
