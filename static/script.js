document.getElementById("caseForm").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const caso = document.getElementById("caso").value;
    const respuesta_usuario = document.getElementById("respuesta").value;
  
    const respuestaIA = document.getElementById("respuestaIA");
    const resultado = document.getElementById("resultado");
  
    respuestaIA.textContent = "Analizando con IA...";
    resultado.classList.remove("hidden");
  
    try {
      const response = await fetch("/analizar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ caso, respuesta_usuario })
      });
  
      const data = await response.json();
      respuestaIA.innerHTML = marked.parse(data.respuesta_ia);
  
    } catch (error) {
      respuestaIA.textContent = "Ocurrió un error al contactar con la IA.";
      console.error(error);
    }
  });
  