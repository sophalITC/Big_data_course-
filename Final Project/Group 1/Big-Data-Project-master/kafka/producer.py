from confluent_kafka import Producer
import csv

# Kafka broker settings
bootstrap_servers = 'localhost:9092'
topic = 'your-topic'

# Producer configuration
producer_config = {
    'bootstrap.servers': bootstrap_servers,
    'client.id': 'python-producer'
}

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Create Kafka producer instance
producer = Producer(producer_config)

# CSV file path
csv_file_path = '/Users/samlyheng/kafka/dataset.csv'

# Produce messages from CSV file
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        message = ','.join(row)
        producer.produce(topic, value=message, callback=delivery_report)
        producer.poll(0.5)  # Handle message delivery reports

# Wait for any outstanding messages to be delivered and delivery reports to be received
producer.flush()
