// Obtenemos los elementos del formulario de inicio de sesión
const formInicioSesion = document.querySelector('.formulario_inicio_sesion');
const inputUsuario = document.querySelector('.input_usuario');
const inputPassword = document.querySelector('.input_password');

// Agregamos un evento al formulario cuando se envía
formInicioSesion.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevenimos que el formulario se envíe

  // Validamos si se ingresó un usuario o correo electrónico
  if (inputUsuario.value.trim() === '') {
    alert('Por favor, ingrese un nombre de usuario o correo electrónico.');
    return false;
  }

  // Validamos si se ingresó una contraseña
  if (inputPassword.value.trim() === '') {
    alert('Por favor, ingrese una contraseña.');
    return false;
  }

  // Si todo está bien, enviamos el formulario
  formInicioSesion.submit();
});

  