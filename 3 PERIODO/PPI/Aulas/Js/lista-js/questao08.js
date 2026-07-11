const prompt = require("prompt-sync")();

let hora = parseInt(prompt("Digite a hora (0-23): "));

if (hora >= 6 && hora <= 11) console.log("Bom dia");
else if (hora >= 12 && hora <= 17) console.log("Boa tarde");
else if (hora >= 18 && hora <= 23) console.log("Boa noite");
else console.log("Madrugada");
