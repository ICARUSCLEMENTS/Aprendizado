-- q1

select disciplina.nome,disciplina.carga_horaria from disciplina;

-- q2
select disciplina.nome,disciplina.carga_horaria from disciplina
where carga_horaria = 60;

-- q3
select disciplina.nome from disciplina
where id_curso = 1;

-- q4
select disciplina.nome,disciplina.carga_horaria from disciplina
where carga_horaria > 39 and carga_horaria < 61;

-- q5
select aluno.nome,cidade.nome from aluno
join cidade on (aluno.id_cidade = cidade.id_cidade);

-- q6
select aluno.nome,aluno.email,cidade.nome from aluno
join cidade on (aluno.id_cidade = cidade.id_cidade)
where cidade.sigla_estado = 'RN';

-- q7
select aluno.nome,cidade.nome from aluno
join cidade on (aluno.id_cidade = cidade.id_cidade)
where cidade.populacao > 100000;

-- q8
select professor.nome,professor.titulacao,cidade.nome from professor
join cidade on (professor.id_cidade = cidade.id_cidade)
where titulacao = 'Doutor';

-- q9
select aluno.nome,curso.nome_curso from matricula
join aluno on (matricula.id_aluno = aluno.id_aluno)
join curso on (matricula.id_curso = curso.id_curso)

-- q10
select aluno.nome,curso.nome_curso,matricula.ano from matricula
join aluno on (matricula.id_aluno = aluno.id_aluno)
join curso on (matricula.id_curso = curso.id_curso)
where ano = 2024

-- q11
select disciplina.nome, disciplina.carga_horaria, curso.nome_curso from disciplina
join curso on (disciplina.id_curso = curso.id_curso)
where disciplina.carga_horaria = 60;


-- q12
select disciplina.nome, professor.nome, oferta.horario from oferta
join disciplina on (oferta.id_disciplina = disciplina.id_disciplina)
join professor on (oferta.id_professor = professor.id_professor)
where oferta.semestre = 1 and oferta.ano = 2024

-- q13
select aluno.nome, inscricao.nota_final, inscricao.frequencia from inscricao
join aluno on (inscricao.id_aluno = aluno.id_aluno)
where inscricao.situacao = 'Aprovado';

-- q14
select aluno.nome, disciplina.nome from inscricao
join aluno on (inscricao.id_aluno = aluno.id_aluno)
join oferta on (inscricao.id_oferta = oferta.id_oferta)
join disciplina on (oferta.id_disciplina = disciplina.id_disciplina);


-- q15
select aluno.nome, disciplina.nome, inscricao.nota_final from inscricao
join aluno on (inscricao.id_aluno = aluno.id_aluno)
join oferta on (inscricao.id_oferta = oferta.id_oferta)
join disciplina on (oferta.id_disciplina = disciplina.id_disciplina)
where inscricao.situacao = 'Aprovado';


-- q16
select aluno.nome, disciplina.nome, professor.nome from inscricao
join aluno on (inscricao.id_aluno = aluno.id_aluno)
join oferta on (inscricao.id_oferta = oferta.id_oferta)
join disciplina on (oferta.id_disciplina = disciplina.id_disciplina)
join professor on (oferta.id_professor = professor.id_professor);

-- q17
select aluno.nome, curso.nome_curso, disciplina.nome, inscricao.situacao from inscricao
join aluno on (inscricao.id_aluno = aluno.id_aluno)
join oferta on (inscricao.id_oferta = oferta.id_oferta)
join disciplina on (oferta.id_disciplina = disciplina.id_disciplina)
join matricula on (aluno.id_aluno = matricula.id_aluno)
join curso on (matricula.id_curso = curso.id_curso)
where curso.nome_curso = 'Técnico em Informática' and inscricao.situacao = 'Aprovado';

-- q18
select count(*) from matricula
join curso on (matricula.id_curso = curso.id_curso)
where curso.nome_curso = 'Técnico em Informática';

-- q19
select count(*) from inscricao
join oferta on (inscricao.id_oferta = oferta.id_oferta)
join disciplina on (oferta.id_disciplina = disciplina.id_disciplina)
where inscricao.situacao = 'Aprovado' and disciplina.nome = 'Projeto de Banco de Dados';