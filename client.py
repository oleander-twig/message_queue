from marshal import load
from urllib import response
import pika
import uuid
import pickle


class Client(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)
    
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
    
    def call(self, message):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=pickle.dumps(message))
        while self.response is None:
            self.connection.process_data_events()
        return pickle.loads(self.response)
        
start_link = input("Starting point: ")
finish_link = input("Ending point: ")
message = [start_link, finish_link]

sender_client = Client()
[number, path] = sender_client.call(message)

print(" [.] Got ", number, "There is a path: ", path)
