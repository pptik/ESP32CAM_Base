import pika

credentials = pika.PlainCredentials('***', '****')
parameters = pika.ConnectionParameters('rmq1.pptik.id',5672, '/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
# channel.exchange_declare(exchange='logs', exchange_type='fanout')
# result = channel.queue_declare(queue='', exclusive=True)
# queue_name = result.method.queue
# channel.queue_bind(exchange='logs', queue=queue_name)

channel.basic_publish(exchange='', routing_key='pkl_juli_2021_1', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
