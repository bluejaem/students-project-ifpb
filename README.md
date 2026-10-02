# Students Project (IFPB)

Projeto prático de consolidação em Programação Orientada a Objetos (POO) desenvolvido para o **Curso de Extensão em Python para Análise de Dados** ofertado pelo **IFPB (Instituto Federal da Paraíba – Campus Cabedelo Centro)**.

## Tecnologias e Conceitos
- **Linguagem:** Python 3
- **POO:** Modelagem de classes, encapsulamento com `@property` e setters, tratamento e lançamento de exceções (`ValueError`), representação textual amigável (`__str__`).
- **Persistência de Dados:** Serialização binária com o módulo nativo `pickle` (`students.pkl`).
- **Auditoria / Logs:** Rastreamento temporal de operações de cadastro e remoção em arquivo de log (`operations.log`).

## Estrutura do Projeto
```text
Students-Project/
├── student.py           # Modelo de domínio da entidade Student
├── student_service.py   # Regras de negócio, persistência binária e logs
├── student_register.py  # Interface interativa de linha de comando (CLI)
├── .gitignore
└── README.md