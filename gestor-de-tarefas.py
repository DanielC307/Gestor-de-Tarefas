# Back dev-Daniel

print("\n==============================")
print("\nGESTOR DE TAREFAS DO SEU ZÉ")
print("\n==============================")

lista = []
cont = 0
    
def tarefas(id, descricao, data, status):
    return {
        "id": id,
        "descricao": descricao,
        "data": data,
        "status": status
    }

# def cadastro():

#     descricao = input("\nDescrição da Tarefa: ")
#     data = input("\n Data dd/mm/aa : ")
#     status = "Tarefa cadastrada"

#     tarefa = tarefas( cont, descricao, data, status)

#     return tarefa


print("\n1) Cadastrar atividade")
print("\n2) Listar Atividades")
print("\n3) Concluir Atividade")
print("\n4) Reabri Atividade")
print("\n0) sair")

while True:
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        cont += 1
        descricao = input("\nDescrição da Tarefa: ")
        data = input("\n Data dd/mm/aa : ")
        status = "Tarefa cadastrada"
        nova_tarefa = tarefas(cont, descricao, data, status)
        lista.append(nova_tarefa)
        continue
    
    if opcao == 0:
        print(lista)
        break
   
    

       
    
        





# Front dev-Edu