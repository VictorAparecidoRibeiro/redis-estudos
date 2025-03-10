import redis 

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

# Cria o objeto pubsub
pubsub - r.pubsub()

# Usa o .subscribe() para fazer a subscription no topico e escutar por mensagens
pubsub.subscribe('data_channel')

# .listen() retorna um generator que pode ser iterado p/ escutar mensagens do publisher

for message in pubsub.listen():
    print(message)