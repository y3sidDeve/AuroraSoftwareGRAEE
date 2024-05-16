
// Logica de la Tabla clientes
new DataTable('#tabla_persona', {

    responsive: true,
    paging: true, // Activa la paginación
    // personalizar los estilos de paginacion
    lengthChange: true,
    pageLength: 10,
    searching: true,
    bFilter: true,
    bInfo: true,
    ordering: true,
    language: {
        // Configura los textos y mensajes de paginación según tus necesidades
        "lengthMenu": "Mostrar _MENU_ registros",
        "zeroRecords": "No se encontraron resultados",
        "info": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        // ...otros mensajes...
    },

    "drawCallback": function (settings) {
        //$('li.page-item.active').addClass("active-st");
        $('.page-link').addClass("text-dark");
        $('.page-item.active .page-link').addClass("bg-info rounded text-white border-info");
    }


});

new DataTable('#tabla_empresa', {

    responsive: true,
    paging: true, // Activa la paginación
    // personalizar los estilos de paginacion
    lengthChange: true,
    pageLength: 10,
    searching: true,
    bFilter: true,
    bInfo: true,
    ordering: true,
    language: {
        // Configura los textos y mensajes de paginación según tus necesidades
        "lengthMenu": "Mostrar _MENU_ registros",
        "zeroRecords": "No se encontraron resultados",
        "info": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        // ...otros mensajes...
    },

    "drawCallback": function (settings) {
        //$('li.page-item.active').addClass("active-st");
        $('.page-link').addClass("text-dark");
        $('.page-item.active .page-link').addClass("bg-info rounded text-white border-info");
    }


});

const flexSwitchCheckDefault = document.getElementById('flexSwitchCheckDefault');
const tipoClienteRow = document.getElementById('tipoClienteRow');
const tipoClienteTexto = document.getElementById('tipoClienteTexto');

flexSwitchCheckDefault.addEventListener('change', function () {
    const formPersona = document.getElementById('form_persona');
    const formCliente = document.getElementById('form_empresa');


    if (this.checked) {
        tipoClienteTexto.innerText = 'Empresa';
        formPersona.style.display = 'none';
        formCliente.style.display = 'block';
    } else {
        tipoClienteTexto.innerText = 'Persona';
        formPersona.style.display = 'block';
        formCliente.style.display = 'none';
    }
});

$(document).ready(function () {
    var tabla_1 = $('#tabla_persona').DataTable();
    var tabla_2 = $('#tabla_empresa').DataTable();

    $('#flexSwitchTable').change(function () {
        if ($(this).is(':checked')) {
            $('#tabla_persona').hide();
            $('#tabla_empresa').show();
            if ($.fn.DataTable.isDataTable('#tabla_persona')) {
                tabla_1.destroy();
            }
            if (!$.fn.DataTable.isDataTable('#tabla_empresa')) {
                tabla_2 = $('#tabla_empresa').DataTable();
            }
        } else {
            $('#tabla_empresa').hide();
            $('#tabla_persona').show();
            if ($.fn.DataTable.isDataTable('#tabla_empresa')) {
                tabla_2.destroy();
            }
            if (!$.fn.DataTable.isDataTable('#tabla_persona')) {
                tabla_1 = $('#tabla_persona').DataTable();
            }
        }
    });
});



