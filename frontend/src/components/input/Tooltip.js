import React from 'react';
import "./style.css";

const Tool = ({ text, children }) => {
  const [showTooltip, setShowTooltip] = React.useState(false);

  const handleMouseEnter = () => {
    setShowTooltip(true);
  };

  const handleMouseLeave = () => {
    setShowTooltip(false);
  };

  return (
    <div className="tooltip-container">
      <div className="input-container">
        {children}
        <span
          className="question-mark"
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          ?
        </span>
        
        {showTooltip && <div className="tooltip">{text}</div>}
      </div>
    </div>
  );
};



export default Tool;