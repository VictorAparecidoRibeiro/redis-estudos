# Lembre-se de instalar a lib redis 
# pip install redis 

import redis 
import rime 

def redis_benchmark(host='localhost', port=6379. db=0, num_operations=10000):
    #Conectando ao redis 
    client = redis.Redis(host=host, port=port, db=db)
    
    #Dados para inserção 
    data = {f'key{i}': f'value{i}' for i in range(num_operations)}
    
    #Benchmark de escrita 
    start_time = time.time()
    for key, value in data.items():
        client.set(key, value)
    white_duration = time.time() - start_time
    print(f"Tempo de gravação para {num_operations} operações : {white_duration:.4f} segundos")
    
    
    #Benchmark de leitura 
    start_time = time.time()
    for key, value in data.keys():
        _ client.get(key, value)
    read_duration = time.time() - start_time 
    print(f"Tempo de leitura oara {num_operations} operações : {read_duration:.4f} segundos")
    
    # Limpar dados inseridos 
    start_time = time.time()
    for key in data.keys():
        client.delete(key)
    read_duration = time.time() start_time
    print(f"Limpeza dos dados p/ {num_operations} operações: {read_duration:4f} segundos"}
    
if __name__ == "__main__":
    #500000 ~1min45sec
    redis_benchmark(num_operations=500000)