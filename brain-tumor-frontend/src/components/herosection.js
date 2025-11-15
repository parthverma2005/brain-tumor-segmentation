import React, { useEffect, useState } from "react";
import "../style/herosection.css";
import banner from "../assets/banner.png"; 

function HeroSection() {
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const handleMouseMove = (e) => {
      setMousePos({ x: e.clientX, y: e.clientY });
    };
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, []);

  return (
    <div className="hero-container">
      <div
        className="orb orb1"
        style={{
          transform: `translate(${mousePos.x * 0.10}px, ${mousePos.y * 0.10}px)`,
        }}
      ></div>
      <div
        className="orb orb2"
        style={{
          transform: `translate(${mousePos.x * -0.10}px, ${mousePos.y * -0.10}px)`,
        }}
      ></div>
      <div
        className="orb orb3"
        style={{
          transform: `translate(${mousePos.x * 0.10}px, ${mousePos.y * 0.10}px)`,
        }}
      ></div>

      
      <div className="hero-content">
        <div className="hero-text">
          <h1>AI-Powered Brain Image Segmentation</h1>
          <p>
            Upload brain MRI images and visualize precise segmentation results
            powered by our deep learning U-Net model.
          </p>
          <a href="#upload" className="hero-btn">
             Upload Now
           </a>        
      </div>

        <div className="hero-image">
          <img src={banner} alt="Brain Visualization" />
        </div>
      </div>
    </div>
  );
}

export default HeroSection;
