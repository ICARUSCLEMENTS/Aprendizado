pontuacaop = 10
local nome = "João"
local icaroecalvo = false
inteligencia = 0

pontuacaoBaixa = 20
pontuacaoMedia = 50
pontuacaoAlta = 100


nome = io.read("*line")

print("Seu nome é " .. nome)

-- serve para dar bônus dependendo do nome da pessoa.
function DarBonusPorNome()
    if (nome == "Icaro") then
        pontuacaop = pontuacaop + 10
    elseif(nome == "João") then
        pontuacaop = pontuacaop - 50
    end
end

-- vai mudar o nivel de inteligencia da pessoa baseada na pontuação
function MudaInteligenciaPorPontuacao()
    if(pontuacaop < pontuacaoBaixa) then
        inteligencia = 1
    elseif(pontuacaop >= pontuacaoBaixa and pontuacaop < pontuacaoAlta) then
        inteligencia = 2
    elseif(pontuacaop >= pontuacaoAlta) then
        inteligencia = 3
    end
end

function MudarInteligenciaPorLoop(maxPontos)
    contaPontos = maxPontos
    
    for i = 0, pontuacaop, 1
    do
        
        if(i == contaPontos) then
            inteligencia = inteligencia + 1
            contaPontos = contaPontos + maxPontos
        
        end
        
    end
    
end

  
-- adiciona uma pontuação desejada ao seu total.
function AddPontuacao(pontos)
    
    DarBonusPorNome()
    
    pontuacaop = pontuacaop + pontos
    return pontuacaop
    
end


print("Minha pontuação é: " .. AddPontuacao(1))

MudarInteligenciaPorLoop(5)

print("E minha inteligência é: " .. inteligencia)