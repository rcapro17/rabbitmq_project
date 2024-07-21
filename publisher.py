import pika

#create a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

#create a channel
channel = connection.channel()

#if the queue does not exist
#create a queue
channel.queue_declare(queue="hello")


#publish the message
channel.basic_publish(exchange="", routing_key="hello", body="hello_world msg #1")
print("[x] Sent Hello World")

#close the connection
connection.close()