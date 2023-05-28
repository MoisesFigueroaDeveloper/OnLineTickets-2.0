const transferenciaBtn = document.getElementById("transferenciaBtn");

// agregar un manejador de eventos click
transferenciaBtn.addEventListener("click", function(event) {
  // hacer la lógica de transferencia aquí...
  
  // mostrar el elemento de confirmación
  const confirmacion = document.getElementById("confirmacion");
  confirmacion.style.display = "block";
});