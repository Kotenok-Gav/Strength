import React from "react";
import Tool from "./input/Tooltip";

const InputField = ({ value, onChange, placeholder, toolTipText, label }) => {
  return (
    <div>
      <p className="pb-3 pl-5 text-xl">{label}</p>
      <div className="flex items-center justify-between bg-slate-700 rounded-3xl px-5">
        <input
          value={value}
          onChange={onChange}
          type="text"
          className="w-full py-2 rounded-xl bg-slate-700 text-white outline-none"
          placeholder={placeholder}
        />
        <Tool text={toolTipText} />
      </div>
      <br />
    </div>
  );
};

export default InputField;
