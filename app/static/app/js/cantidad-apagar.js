function mostrarFormulario(seccion, precio) {
    var formulario = document.getElementById("formulario");
    var seccionElemento = document.getElementById("seccion");
    var precioTotalElemento = document.getElementById("precio-total");
  
    // Mostrar el formulario
    formulario.style.display = "block";
  
    // Configurar la sección y el precio
    seccionElemento.innerText = seccion;
    precioTotalElemento.innerText = precio;
  
    // Configurar el botón de "Calcular total"
    var calcularTotalBoton = document.getElementById("calcular-total");
    calcularTotalBoton.onclick = function() {
      // Obtener la cantidad de entradas y calcular el precio total
      var cantidadEntradas = parseInt(document.getElementById("cantidad").value);
      var precioTotal = cantidadEntradas * precio;
  
      // Mostrar el precio total en la página
      precioTotalElemento.innerText = precioTotal;
    };
  }
  

