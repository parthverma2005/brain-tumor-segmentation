import React, { useState } from "react";
import axios from "axios";
import "../style/uploadsection.css";

function UploadSection({ setResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please select an image");

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const API_URL = process.env.REACT_APP_BACKEND_URL;

      const res = await axios.post(`${API_URL}/predict`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setResult(res.data);
    } catch (err) {
      console.error("Upload Error:", err);
      alert("Error uploading image. Check backend logs.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section id="upload" className="upload-section">
      <div className="upload-container">
        <h2>Upload MRI Scan</h2>
        <div className="upload-box">
          <input 
            type="file" 
            onChange={(e) => setFile(e.target.files[0])} 
          />
          <button onClick={handleUpload} disabled={loading}>
            {loading ? "Analyzing..." : "Analyze with AI"}
          </button>
        </div>

        {file && (
          <div className="preview">
            <h4>Preview:</h4>
            <img
              src={URL.createObjectURL(file)}
              alt="Uploaded MRI"
              className="preview-img"
            />
          </div>
        )}
      </div>
    </section>
  );
}

export default UploadSection;
