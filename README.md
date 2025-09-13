Este projeto tem como principal objetivo desenvolver uma ferramenta de email automática que, através de um ficheiro google sheets, envie um conjunto de emails pré-formatados pelo utilizador. Vale realçar que o programa apenas deve ser usado quando o forms associado ao ficheiro de google sheets for efetivamente fechado.

Como usar este ficheiro??
- A alteração da mensagem do email pode ser alterada em "module.py" na função define_message.
- A alteração do assunto do email pode ser alterado no ficheiro "subject_df.txt".
- O url do ficheiro google sheets deve ser alterado no ficheiro "url_df.txt", exclusivamente aplicando o código do meio.
- Os campos/colunas mapeados no ficheiro google sheets devem ser pensados e alterados consoante a mensagem, contactar o criador do código para fazer essa alteração devido a necessidade de mudar em mais do que um único ficheiro.
- O email do utilizador deve ser trocado no ficheiro "sharemail.py" na variável email.
- O código de login deve ser alterado consoante o email de utilizador no ficheiro "sharemail.py" dentro do metodo login.
- A importância do email pode ser alterada de duas formas distintas no ficheiro "module.py" pelo message["X-Priority"] e pelo message["Importance"] sendo respetivamente "1" e "High" os que fornecem a maior importância.

Qualquer dúvida contactar o criador: ricardoferreira2006@hotmail.com