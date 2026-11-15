/**
 * Archivo: recursos_estaticos/js/funciones_interfaz.js
 * Proyecto: Sistema Web Urban 45 - Gimnasio Smart
 * Curso: Lenguajes de Programación - UTP
 * Descripción: Funciones sencillas en JavaScript para mejorar la comodidad
 *              del usuario en los formularios de demostración.
 */

/**
 * Completa automáticamente los datos de un usuario de demostración
 * en la pantalla de inicio de sesión (Guía, PDF pp. 67 y 70).
 */
function cargarUsuarioDemo(correo, rol) {
    const campoCorreo = document.getElementById("campo_correo");
    const campoRol = document.getElementById("campo_rol");

    if (campoCorreo) {
        campoCorreo.value = correo;
    }
    if (campoRol) {
        campoRol.value = rol;
    }
}

/**
 * Completa datos de prueba válidos en el formulario de registro de cliente
 * para facilitar la demostración en vivo durante la exposición.
 */
function autocompletarClienteEjemplo() {
    const campos = {
        "id_nombre": "Roberto",
        "id_apellidos": "Mendoza Vargas",
        "id_dni": "74859612",
        "id_telefono": "984512369",
        "id_correo": "roberto.mendoza@email.com"
    };

    for (const idCampo in campos) {
        const elemento = document.getElementById(idCampo);
        if (elemento) {
            elemento.value = campos[idCampo];
        }
    }
}
