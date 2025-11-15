import React, { useState } from "react";
import HeroSection from "./components/herosection";
import UploadSection from "./components/uploadsection";
import ResultSection from "./components/resultsection";
import "./style/App.css";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="app-wrapper">
      <section id="hero">
        <HeroSection />
      </section>

      <section id="upload">
        <UploadSection setResult={setResult} />
      </section>

      <section id="result">
        <ResultSection result={result} />
      </section>
    </div>
  );
}

export default App;
