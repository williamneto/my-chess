
/matchs/new - Requisição para iniciar nova partida partida 
- Gera um ID da nova partida e cria o registro no banco
- retorna o link para a partida

/matchs/{match_id} - Requisição para entrar em uma partida
- Verifica se o match_id é válido, se não for retorna 404
- Verifica se dois jogadores já foram atribuidos
    - Se sim, verifica se o IP da requisição é de um dos jogadores atribuidos
        - Se não for, retorna 404
    - Se não, atribui mais um jogador salvando o IP da requisição
- Retorna dados da partida
