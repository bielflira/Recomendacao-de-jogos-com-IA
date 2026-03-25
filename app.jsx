import { useState } from "react";
import axios from "axios";

function App() {
  const [jogo, setJogo] = useState("");
  const [resultados, setResultados] = useState([]);

  async function buscar() {
    const res = await axios.post("http://localhost:8000/recomendar", {
      jogo
    });
    setResultados(res.data.recomendacoes);
  }

  return (
    <div>
      <h1>🎮 GameAI</h1>

      <input onChange={(e)=>setJogo(e.target.value)} />
      <button onClick={buscar}>Recomendar</button>

      {resultados.map((j, i) => (
        <div key={i}>{j.name}</div>
      ))}
    </div>
  );
}

export default App;
