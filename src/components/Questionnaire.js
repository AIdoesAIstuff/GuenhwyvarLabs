import React from 'react';

export default function Questionnaire({ question, options, onAnswer }) {
  return (
    <div className="question">
      <h2>{question}</h2>
      <div className="options">
        {options.map((opt) => (
          <button key={opt} onClick={() => onAnswer(opt)}>
            {opt}
          </button>
        ))}
      </div>
    </div>
  );
}
