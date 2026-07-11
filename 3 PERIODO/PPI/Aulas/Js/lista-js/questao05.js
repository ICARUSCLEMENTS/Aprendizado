const prompt = require("prompt-sync")();

let celsius = parseFloat(prompt("Digite a temperatura em °C: "));
let fahrenheit = celsius * 9/5 + 32;

console.log(`${celsius}°C equivale a ${fahrenheit}°F`);
