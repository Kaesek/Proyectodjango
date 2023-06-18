// validaciones

$(function () {
  $("formulario").validate({
    rules: {
      email: {
        required: true,
        email: true,
      },
      date: {
        required: true,
        date: true,
      },
      number: {
        required: true,
        minlenght: 9,
        maxlenght: 9,
      },
    },
    messages: {
      email: {
        required: "Ingresa tu correo electrónico",
        email: "Formato de correo no válido",
      },
    },
  });
});

// funcion btn enviar
function alertaenviar() {
  return confirm("¿Estás seguro de enviar el formulario?");
}
