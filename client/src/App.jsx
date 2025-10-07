
import BookTable from "./book/BookComponent";
import "./styles/App.scss";

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

      <>

   <div>
     <BookTable/>

       </div>
      </>
  );
}

export default App;

