// 1. Pega os elementos do HTML
const input1 = document.getElementById("numero1");
const input2 = document.getElementById("numero2");
const input3 = document.getElementById("numero3");
const botao = document.getElementById("btnSomar");
const resultado = document.getElementById("resultado");


// 2. Funcao que faz a soma
function somar() {
  // Le os valores dos inputs e converte para numero
  const n1 = Number(input1.value);
  const n2 = Number(input2.value);
  const n3 = Number(input3.value);

  // Faz a soma
  const soma = n1 + n2;

  // Mostra o resultado na tela
  resultado.textContent = "Resultado: " + soma;
}


function somar() {
  const n1 = Number(input1.value);
  const n2 = Number(input2.value);
  const n3 = Number(input3.value);

  const multi = n1 * n2 * n3;


  resultado.textContent = "Resultado: " + multi;
}

function Limpar() {
  const input1 = ""
  const input2 = ""
  const input3 = ""
  const resultado = ""
}


// 3. Quando o botao for clicado, chama a funcao somar
botao.addEventListener("click", somar);
botao.addEventListener("click", Multiplicar);
botao.addEventListener("click", Limpar);
