const porcentagem = document.getElementById("porcentagem");
const pesoideal = document.getElementById("pesoideal");
const resultado = document.getElementById("resultado");
const situacao = document.getElementById("situacao");
const botao = document.getElementById("calcular");
const input1 = document.getElementById("altura");
const input2 = document.getElementById("peso");

// Função para calcular o IMC
function calcularimc() {
    const alturac = Number(input1.value);
    const pesoc = Number(input2.value);
    // O calculo consiste em dividir o peso da pessoa pelo quadrado da altura da mesma
    const calculo = pesoc/alturac**2;
    // Resultado numeral
    resultado.textContent = calculo.toFixed(1);
    // Representa a situção da pessoa
    // Situações => ("Abaixo do peso", "Normal", "Sobrepeso", "Obesidade de 1º Grau", "Obesidade de 2º Grau", "Obesidade de 3º Grau")
    if (calculo < 18.5) {
        situacao.textContent = "Abaixo do peso";
    } else if (calculo < 25) {
        situacao.textContent = "Normal";
    } else if (calculo < 30) {
        situacao.textContent = "Sobrepeso";
    } else if (calculo < 35) {
        situacao.textContent = "Obesidade de 1º Grau";
    } else if (calculo < 40) {
        situacao.textContent = "Obesidade de 2º Grau";
    } else {
        situacao.textContent = "Obesidade de 3º Grau";
    }
}

// Função para calcular o peso ideal
function PesoIdeal() {
    const alturac = Number(input1.value);
    // valores minimo e maximo
    const pesomn = 18.5*(alturac**2);
    const pesomx = 24.9*(alturac**2);

    pesoideal.textContent = `Peso ideal está entre ${pesomn.toFixed(1)}kg e ${pesomx.toFixed(1)}kg.`;
}

// função para calcular a diferença percentual
function Diferenca() {
    const alturac = Number(input1.value);
    const pesoc = Number(input2.value);

    const pesomn = 18.5 * (alturac ** 2);
    const pesomx = 24.9 * (alturac ** 2);
    // para imprimir o resultado certo tenho que definir se está abaixo ou acima do peso, para isso, tenho que usar o if para distinguir.
    if (pesoc < pesomn) {
        const dif = ((pesomn - pesoc) / pesomn) * 100;
        porcentagem.textContent = `Você está ${dif.toFixed(1)}% abaixo do peso ideal mínimo.`;
    } else if (pesoc > pesomx) {
        const dif = ((pesoc - pesomx) / pesomx) * 100;
        porcentagem.textContent = `Você está ${dif.toFixed(1)}% acima do peso ideal máximo.`;
    } else {
        porcentagem.textContent = "Você está dentro do peso ideal!";
    }
}

// função para chamar todas as outras
function calcularTudo() {
    calcularimc();
    PesoIdeal();
    Diferenca();
}

botao.addEventListener("click", calcularTudo);

