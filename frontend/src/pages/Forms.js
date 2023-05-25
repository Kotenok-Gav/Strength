import { useEffect, useState } from "react";
import axios from "axios";
import Tool from "../components/input/Tooltip";

function Forms() {
  const [bdf, setBdf] = useState([]);
  const [text, setText] = useState("");
  const [start_rocket, setStart_rocket] = useState("");

  const addBdfHandler = () => {
    const postBdf = async () => {
      const postBdfdata = {
        text: text,
        start_rocket: start_rocket,
      };
      const { data } = await axios.post(
        "http://127.0.0.1:8000/bdf/",
        postBdfdata
      );
      setBdf([...bdf, data]);
      setText("");
      setStart_rocket("");
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

          {/* 1 */}
          <p className="pb-3 pl-5 text-xl">Название проекта</p>
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

          {/* 2 */}
          <p className="pb-3 pl-5 text-xl">Введите 0, если старт подводный,     1 - наземный</p>
          <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5 ">
            <input
              value={start_rocket}
              onChange={e => setStart_rocket(e.target.value)}
              type="text"
              className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
              placeholder="0"
            />
            <Tool text="Укажите название проекта"></Tool>
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
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Forms;
