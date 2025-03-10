import redis 

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

while True:
    message = input("Realtime Push Notification - Digite a Mensagem: ")
    r.publish("data_channel", message)