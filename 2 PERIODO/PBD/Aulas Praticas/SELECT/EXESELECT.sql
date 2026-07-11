    -- q1
select * from artistas;

-- q2
select titulo,ano_lancamento from albuns;

-- q3
select titulo,num_streams from musicas
where num_streams > 2000000000;

-- q4
select nome,pais,genero_musical from artistas
where pais = 'Reino Unido';

-- q5
select titulo,ano_lancamento,num_faixas from albuns
where ano_lancamento > 2020;

-- q6
select nome,ouvintes_mensais from artistas
where ouvintes_mensais > 60000000
order by ouvintes_mensais ASC;

-- q7
select titulo,duracao_segundos from musicas
where duracao_segundos < 221 and duracao_segundos > 179;

-- q8
select nome, pais, genero_musical from artistas
where pais = 'Estados Unidos' or pais = 'Canadá';

-- q9
select titulo, num_faixas, ano_lancamento from albuns
where num_faixas > 15 and ano_lancamento < 2022;

-- q10
select titulo, id_album, num_streams from musicas
where id_album = 1 or id_album = 3
order by num_streams desc;