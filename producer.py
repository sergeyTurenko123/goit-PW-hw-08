import pika
from bson import json_util
from models2 import Contact
import faker
from random import choice

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_mock', queue='task_queue')

def main():
    NAME = 50
    EMAIL = 50
    def generate_fake_data(name, email):
        fake_name = []
        fake_email = []

        fake_data = faker.Faker()

        for _ in range(name):
            fake_name.append(fake_data.name())
        for _ in range(email):
            fake_email.append(f"{fake_data.last_name()}@{fake_data.domain_name()}")
        return fake_name, fake_email

    names, emails = generate_fake_data(NAME, EMAIL)

    for name in names:
        message = Contact(name=name, email=choice(emails), log=False).save()

    for contact in Contact.objects():
        channel.basic_publish(
            exchange='task_mock',
            routing_key='task_queue',
            body=json_util.dumps(contact.id).encode(),
            properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
        print(" [x] Sent %r" % message)
    connection.close()
    
    
if __name__ == '__main__':
    main()
    