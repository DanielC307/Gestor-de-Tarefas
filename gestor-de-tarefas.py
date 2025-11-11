print("\n==============================")
print("\nGESTOR DE TAREFAS")
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

print("\n1) Cadastrar atividade")
print("\n2) Listar Atividades")
print("\n3) Concluir Atividade")
print("\n4) Reabri Atividade")
print("\n0) sair")

while True:
    try:     
        opcao = int(input("\nEscolha uma opção: "))
        
        if opcao == 1:
            cont += 1
            descricao = input("\nDescrição da Tarefa: ")
            data = input("\n Data dd/mm/aa : ")
            status = "A Fazer"
            nova_tarefa = tarefas(cont, descricao, data, status)
            lista.append(nova_tarefa)
            continue
    
        if opcao == 2:
            print("\n===================================")
            print("\nLISTA DE TAREFAS")
            print("\n===================================\n")   
            
            if len(lista) == 0:
            
             print("Nenhuma Tarefa a ser feita")  
             
            else:
            
                for listar in lista:
                    print(f"\nID: {listar['id']}")
                    print(f"\nDescrição: {listar['descricao']}")
                    print(f"\nData: {listar['data']}")
                    print(f"\nStatus: {listar['status']}")
                    print("\n---------------------------------")
                    
            continue   
    
        if opcao == 3:
            
            identificador = int(input("\nDigite o id da tarefa que deseja concluir: "))
            encontrada = False
            
            for listar in lista:
                if identificador == listar['id']:
                    encontrada = True
                    listar['status'] = 'Concluido'
                    print(f"\nA tarefa {listar['id']} foi {listar['status']}")
                    
            if encontrada == False:
                    
                print("\nTarefa não encontrada!!!")
            
                continue
        
        if opcao == 4:
            
            identificador = int(input("\nDigite o id da tarefa que deseja reabrir: "))
            encontrada = False
            
            for listar in lista:
                encontrada = True
                if identificador == listar['id']:
                    listar['status'] = 'A fazer'
                    print(f"\nA tarefa {listar['id']} foi reaberta")
                else:
            
                    print("Tarefa não encontrada!!!")
            
                    continue
                
            if encontrada == False:
                    
                print("\nTarefa não encontrada!!!")
            
                continue
    
        if opcao == 0:
            print("\n==============================")
            print("RELATÓRIO FINAL")
            print("==============================")


            concluidas = []
            pendentes = []

            for tarefa in lista:
                if tarefa['status'] == 'Concluido':
                   concluidas.append(tarefa)
                elif tarefa['status'] == 'A Fazer':
                    pendentes.append(tarefa)

            print("\nTarefas Concluídas:")
            

            if len(concluidas) == 0:
                print("(nenhuma)")
            else:
              for tarefa in concluidas:
                    print(f"- [{tarefa['id']}] {tarefa['descricao']} ({tarefa['data']})")

            print("\nTarefas Pendentes:")
          
            if len(pendentes) == 0:
              print("(nenhuma)")
            else:
              for tarefa in pendentes:
                  print(f"- [{tarefa['id']}] {tarefa['descricao']} ({tarefa['data']})")

            print("\n---------------------------------")
            print(f"Total concluídas: {len(concluidas)}")
            print(f"Total pendentes: {len(pendentes)}")
            print("---------------------------------")
            break   

    except ValueError:
        
        print("\nDIGITE APENAS OS NUMEROS DO MENU!!!")