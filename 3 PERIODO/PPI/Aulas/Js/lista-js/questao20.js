function calculadora(a, b, operacao) {
  let resultado;

  switch (operacao) {
    case "soma":
      resultado = a + b;
      break;
    case "subtracao":
      resultado = a - b;
      break;
    case "multiplicacao":
      resultado = a * b;
      break;
    case "divisao":
      if (b === 0) {
        resultado = "Erro: divisão por zero";
      } else {
        resultado = a / b;
      }
      break;
    default:
      resultado = "Operação inválida";
  }

  return resultado;
}

const operacoes = [
  { a: 10, b: 5, op: "soma" },
  { a: 20, b: 4, op: "divisao" },
  { a: 7, b: 0, op: "divisao" },
  { a: 3, b: 8, op: "multiplicacao" }
];

for (let o of operacoes) {
  let resultado = calculadora(o.a, o.b, o.op);
  console.log(`${o.op}(${o.a}, ${o.b}) = ${resultado}`);
}
