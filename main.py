import csv
import re
import concurrent.futures

# Função que realiza a busca no arquivo csv usando regex
def search_csv(filename, search_term):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        pattern = re.compile(search_term)
        for row in reader:
            # Verifica se o padrão de regex está presente na linha atual
            if any(pattern.search(col) for col in row):
                # Retorna a linha em que o padrão foi encontrado
                return row
        # Se o padrão de regex não foi encontrado, retorna None
        return None

if __name__ == '__main__':
    filename = 'large_file.csv'
    
    # Solicita que o usuário informe o padrão de regex para busca
    search_term = input("Digite o padrão de regex para busca: ")
    
    # Executa a busca em paralelo com múltiplos processos
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Cria uma lista de futuros, um para cada processo
        futures = [executor.submit(search_csv, filename, search_term) for _ in range(10)]
        
        # Itera sobre os futuros na ordem de conclusão
        for future in concurrent.futures.as_completed(futures):
            # Se o padrão de regex for encontrado, imprime as informações da linha e interrompe a execução
            result = future.result()
            if result is not None:
                print('Found:', result)
                break
