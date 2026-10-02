import sys
from student_service import StudentService

def print_menu():
    print("\n" + "=" * 35)
    print("      STUDENTS PROJECT (IFPB)")
    print("=" * 35)
    print("1 - Cadastrar estudante")
    print("2 - Remover estudante")
    print("3 - Listar estudantes")
    print("0 - Sair")
    print("=" * 35)

def main():
    service = StudentService()

    while True:
        print_menu()
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            name = input("Nome: ")
            house = input("Casa/Cidade: ")
            try:
                student = service.register_student(name, house)
                print(f"\n[OK] Estudante cadastrado com sucesso! ID: {student.id}")
            except ValueError as error:
                print(f"\n[ERRO] {error}")

        elif choice == "2":
            try:
                student_id = int(input("Informe o ID do estudante a remover: "))
                if service.remove_student(student_id):
                    print(f"\n[OK] Estudante com ID {student_id} removido com sucesso!")
                else:
                    print(f"\n[AVISO] Nenhum estudante encontrado com o ID {student_id}.")
            except ValueError:
                print("\n[ERRO] ID inválido. Digite um número inteiro.")

        elif choice == "3":
            students = service.list_all()
            if not students:
                print("\nNenhum estudante cadastrado.")
            else:
                print("\n--- Lista de Estudantes ---")
                for s in sorted(students, key=lambda x: x.id):
                    print(s)

        elif choice == "0":
            print("\nEncerrando o programa...")
            sys.exit(0)

        else:
            print("\nOpção inválida, tente novamente.")

if __name__ == "__main__":
    main()