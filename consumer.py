import pika
from models2 import Contact
import time
import json
import smtplib

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    # smtpObj = smtplib.SMTP(['localhost', 5672])
    # sender = [contact.email for contact in Contact.objects(id=message["$oid"])]
    # smtpObj.sendmail(sender, ['to@example.com'], message)
    contact=Contact.objects(id=message["$oid"])
    contact.update(log=True)
    print(f" [x] Received {message}")
    time.sleep(1)
    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()
