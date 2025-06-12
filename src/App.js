import React, { useState, useEffect } from 'react';
import Questionnaire from './components/Questionnaire';
import AlbumCard from './components/AlbumCard';
import './App.css';

const questions = [
  { text: 'Do you want something…', options: ['introspective', 'expansive'] },
  { text: 'Would you prefer…', options: ['vintage warmth', 'cutting-edge clarity'] },
  { text: 'Do you lean toward…', options: ['lush instrumentation', 'barebone minimalism'] },
  { text: 'Are you in the mood for…', options: ['timeless classic', 'underground gem'] },
  { text: 'Do you want to explore…', options: ['guitar-driven', 'electronic textures'] }
];

export default function App() {
  const [step, setStep] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [album, setAlbum] = useState(null);

  const handleAnswer = (ans) => {
    const newAnswers = [...answers, ans];
    setAnswers(newAnswers);
    if (step + 1 === questions.length) {
      fetch('/recommend', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ answers: newAnswers })
      })
        .then((res) => res.json())
        .then(setAlbum)
        .catch(console.error);
    }
    setStep(step + 1);
  };

  return (
    <div className="App">
      {step < questions.length ? (
        <Questionnaire
          question={questions[step].text}
          options={questions[step].options}
          onAnswer={handleAnswer}
        />
      ) : album ? (
        <AlbumCard album={album} />
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}
