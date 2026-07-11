INSERT INTO cliente (nome, cpf, email) 
VALUES
('Jeferson Queiroga',      '111.111.111-11', 'jefersonqueiroga@ifrn.edu.br'),
('Cauã de Oliveira',    '222.222.222-22', 'cauaoliveira@escolar.ifrn.edu.br'),
('Carla Pereira',  '333.333.333-33', 'carlapereira@.ifrn.edu.br');

INSERT INTO produto (descricao, preco) 
VALUES
('Teclado',      349.99),
('Mouse',           149,99),
('Monitor',  899.90);

INSERT INTO pedido (data_pedido, id_cliente) 
VALUES
('2026-01-20', 1),
('2026-01-21', 1),
('2026-01-21', 2);

INSERT INTO item_pedido (id_pedido, id_produto, quantidade, valor_unitario) 
VALUES
(1, 1, 1, 349.99),
(1, 2, 1, 149.99);

INSERT INTO item_pedido (id_pedido, id_produto, quantidade, valor_unitario) 
VALUES
(2, 3, 1, 899.90);

INSERT INTO item_pedido (id_pedido, id_produto, quantidade, valor_unitario) 
VALUES
(3, 2, 2, 149.99);





