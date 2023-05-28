// Archivo: eventos.js

function mostrarEventos(categoria) {
    // Limpia el contenedor de eventos
    const eventosContainer = document.getElementById('eventos-container');
    eventosContainer.innerHTML = '';

    // Realiza una petición AJAX para obtener los eventos de la categoría seleccionada
    // Puedes utilizar jQuery.ajax o la API fetch para realizar la petición

    // Supongamos que obtienes la respuesta en formato JSON con el siguiente formato:
    // [{ "titulo": "Evento 1", "descripcion": "Descripción del evento 1" }, ...]

    // Luego de obtener los eventos, recorre el array y crea los elementos HTML correspondientes
    const eventos = [
        { "titulo": "Evento 1", "descripcion": "Descripción del evento 1" },
        { "titulo": "Evento 2", "descripcion": "Descripción del evento 2" },
        { "titulo": "Evento 3", "descripcion": "Descripción del evento 3" }
    ];

    for (const evento of eventos) {
        const eventoElement = document.createElement('div');
        eventoElement.innerHTML = `
            <h3>${evento.titulo}</h3>
            <p>${evento.descripcion}</p>
        `;
        eventosContainer.appendChild(eventoElement);
    }
}
