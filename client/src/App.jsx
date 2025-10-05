

import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: "50px", fontFamily: "Arial" }}>
      <h1>Poruka iz backend-a:</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;

