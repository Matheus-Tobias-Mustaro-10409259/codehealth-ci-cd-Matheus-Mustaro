# CodeHealth CI/CD

Projeto acadêmico para demonstrar conceitos de:

- Integração Contínua (CI)
- Entrega Contínua (CD)
- Gerência de Configuração
- GitHub Actions
- DevOps

## Estrutura de Branches

- main → produção
- develop → integração
- feature/teste-ci → funcionalidades temporárias

## Pipeline CI/CD

O workflow executa automaticamente a cada push na branch `develop`.

Etapas:

1. Build
2. Testes automatizados
3. Relatório de status
4. Deploy em homologação (staging)

## Segurança

O arquivo `config.env` não é versionado para evitar exposição de credenciais.

Variáveis sensíveis devem ser armazenadas utilizando GitHub Secrets.

## Gatilhos

```yaml
on:
  push:
    branches:
      - develop
```
