select aluno.nome,aluno.cpf,cidade.nome_cidade,curso.nome_curso from aluno
join cidade ON ( aluno.id_cidade = cidade.id_cidade )
join curso on ( aluno.id_curso = curso.id_curso )