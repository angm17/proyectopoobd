let objetivo = document.getElementById("objetivo");
let cambiante = document.getElementById("cambiante");
let intervaloCambioColor;
let colores = ["red", "blue", "green", "yellow", "purple"];
let round = 0;
let velocidadCambio = 200; // Milisegundos para cambiar de color

function cambiarColorAleatorio() {
    let colorAleatorio = colores[Math.floor(Math.random() * colores.length)];
    cambiante.style.backgroundColor = colorAleatorio;
}

function iniciarJuego() {
    cambiarColorAleatorio(); // Inicia el juego con un color aleatorio
    intervaloCambioColor = setInterval(cambiarColorAleatorio, velocidadCambio);
}

function verificarColor() {
    if (objetivo.style.backgroundColor === cambiante.style.backgroundColor) {
        alert(`¡Correcto! Pasas al round ${round + 2}`);
        round++;
        if(round >= 10) {
            alert("¡Felicidades, has completado el juego!");
            clearInterval(intervaloCambioColor);
        } else {
            cambiarColorObjetivo();
        }
    } else {
        alert("Intenta nuevamente");
    }
}

function cambiarColorObjetivo() {
    objetivo.style.backgroundColor = colores[Math.floor(Math.random() * colores.length)];
    clearInterval(intervaloCambioColor);
    iniciarJuego();
}

document.addEventListener("keydown", function(event) {
    if (event.code === "Space") {
        verificarColor();
    }
});

// Establecer el color inicial del objetivo y comenzar el juego
objetivo.style.backgroundColor = colores[Math.floor(Math.random() * colores.length)];
iniciarJuego();



// let carta = document.getElementById("carta");
// let recuadro = document.getElementById("recuadro");
// let intervalo;
// let velocidad = 8  ; // Píxeles por actualización

// function moverCarta() {
//     let x = parseInt(carta.style.left, 10);
//     x += velocidad;
//     carta.style.left = x + 'px';

//     // Revertir la dirección si alcanza los bordes
//     if (x > window.innerWidth - carta.offsetWidth || x < 0) {
//         velocidad *= -1;
//     }
// }

// function iniciarJuego() {
//     // carta.style.left = '50%'; 
//     carta.style.left = '0px'; // Posición inicial de la carta
//     intervalo = setInterval(moverCarta, 20); // Ajusta el segundo parámetro para controlar la velocidad de la animación
// }

// function verificarAlineacion() {
//     let xCarta = carta.getBoundingClientRect().left + carta.offsetWidth / 2;
//     let xRecuadro = recuadro.getBoundingClientRect().left + recuadro.offsetWidth / 2;

//     // Considera un margen de error para "alineado"
//     const valor = Math.abs(xCarta - xRecuadro);
//     console.log(valor);
//     if (valor <= 10) {
//         clearInterval(intervalo);
//         alert("¡Ganaste!");
//     }
// }

// document.addEventListener("keydown", function(event) {
//     if (event.code === "Space") {
//         verificarAlineacion();
//     }
// });


// // ...

// // Asegurarse de que el juego se reinicie correctamente al cambiar el tamaño de la ventana
// window.onresize = function() {
//     clearInterval(intervalo);
//     iniciarJuego();
// };


// // Iniciar el juego
// iniciarJuego();