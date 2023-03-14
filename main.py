import csv
import concurrent.futures

# Função que realiza a busca no arquivo csv
def search_csv(filename, search_term):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            # Verifica se o termo de busca está presente na linha atual
            if search_term in row:
                # Retorna a linha em que o termo foi encontrado
                return row
        # Se o termo de busca não foi encontrado, retorna None
        return None

if __name__ == '__main__':
    filename = 'large_file.csv'
    
    # Solicita que o usuário informe o termo de busca
    search_term = input("Digite o termo de busca: ")
    
    # Executa a busca em paralelo com múltiplos processos
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Cria uma lista de futuros, um para cada processo
        futures = [executor.submit(search_csv, filename, search_term) for _ in range(10)]
        
        # Itera sobre os futuros na ordem de conclusão
        for future in concurrent.futures.as_completed(futures):
            # Se o termo for encontrado, imprime as informações da linha e interrompe a execução
            result = future.result()
            if result is not None:
                print('Found:', result)
                break
