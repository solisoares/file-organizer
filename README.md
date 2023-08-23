# Organizador de Arquivos
Este é um pequeno projeto em Python que tem como objetivo organizar arquivos em uma pasta em subpastas separadas de acordo com a extensão do arquivo.

## Requisitos
* [Python 3.5 ou superior](https://www.python.org/downloads/)
* ``pathlib``, ``os`` (já incluídos na biblioteca padrão do Python) e ``filetype`` (uma biblioteca leve para inferência do tipo de arquivo quando o mesmo não tem extensão)
* Este código foi testado no Linux e Windows. Não há garantia de que funcionará em outros sistemas operacionais.

## Como usar
1. Baixe ou clone o repositório em sua máquina local
2. Instale as dependências: ``pip install -r requirements.txt``
3. Abra o arquivo ``organize_files.py`` em um editor de texto
4. Defina as extensões de arquivos para cada tipo de arquivo que deseja organizar. Por exemplo, se quiser adicionar mais tipos de imagem, basta incluir a extensão correspondente na lista ``IMAGE_EXT``.
5. Execute o arquivo ``organize_files.py`` e especifique o caminho absoluto para a pasta que deseja organizar.

## Personalização
Este script é fácil de personalizar para suas necessidades específicas. Basta adicionar mais tipos de arquivo editando as listas de extensões e também alterar os nomes das subpastas para algo mais apropriado para você. 

## Contribuições
Se você gostaria de contribuir para este projeto, sinta-se à vontade para abrir uma issue ou pull request. Ficarei feliz em discutir suas ideias e melhorias para este projeto.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/vilelas/file-organizer/blob/main/LICENSE) para mais detalhes.