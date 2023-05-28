document.addEventListener("DOMContentLoaded", function() {
    const selectMetodoPago = document.querySelector("#metodoPago");
    const datosTarjeta = document.querySelector("#datosTarjeta");
    const confirmacion = document.querySelector("#confirmacion");
  
    // Agregar event listener al cambio de valor del select de metodo de pago
    selectMetodoPago.addEventListener("change", function() {
      // Mostrar u ocultar campos de datos de tarjeta según el método de pago elegido
      if (selectMetodoPago.value === "debito" || selectMetodoPago.value === "credito") {
        datosTarjeta.style.display = "block";
      } else {
        datosTarjeta.style.display = "none";
      }
  
      // Mostrar mensaje de confirmación de transferencia bancaria y redirigir a otra página
      if (selectMetodoPago.value === "transferencia") {
        confirmacion.style.display = "block";
        setTimeout(function() {
          window.location.href = "Mensaje-transferencia.html";
        }, 5000);
      } else {
        confirmacion.style.display = "none";
      }
    });
  });
   
  //Arreglar el metodo pago ya que no esta saliendo de forma adecuada los metodos de pago desplegado en el pagina metodo-pago.html//
  //Dentro del metodo de pago hay que agregar alguna clase de mensaje que dara las indicadiones sobre la "reserva de tickets" o metodo de pago por transferencia//
  //este metodo de pago tranferencia tendra un tiempo maximo para hacer la transferencia de 32 horas habiles//