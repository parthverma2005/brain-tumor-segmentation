import React from "react";
import "../style/resultsection.css";

function ResultSection({ result }) {
  if (!result) return null;
  const confidencePercent = (result.confidence*100).toFixed(2);
  return (
    <section id="result">
      <div className="result-container">
        <h2 className="result-model">Model: U-Net</h2>
        <p className="result-confidence">Confidence: {confidencePercent}%</p>

        <div className="confidence-bar">
          <div className="fill" style={{ width: `${confidencePercent}%` }}></div>
        </div>

        <h3 className="result-subtitle">Segmented Output:</h3>
        <img
          src={`data:image/png;base64,${result.overlay}`}
          alt="Segmentation Result"
          className="result-img"
        />
      </div>
    </section>
  );
}

export default ResultSection;
