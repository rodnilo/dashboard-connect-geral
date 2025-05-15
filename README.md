# Relatório Power BI em Tela Cheia

Este é um projeto simples que exibe um relatório do Power BI em tela cheia através de um servidor web local.

## Requisitos

- Python 3.x
- Navegador web moderno

## Como Executar

1. Clone este repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd relatorio_deploy_teste
```

2. Execute o servidor:
```bash
python server.py
```

3. O navegador abrirá automaticamente em `http://localhost:1234`

## Estrutura do Projeto

- `index.html`: Página web que exibe o relatório do Power BI em tela cheia
- `server.py`: Servidor web Python simples que serve a página na porta 1234
- `.gitignore`: Configuração do Git para ignorar arquivos desnecessários

## Personalização

Para alterar o relatório exibido, edite o arquivo `index.html` e substitua a URL do iframe pela URL do seu relatório do Power BI.

## Notas

- O servidor deve estar rodando para visualizar o relatório
- Para parar o servidor, pressione `Ctrl+C` no terminal 