from kafka import KafkaConsumer
from hdfs import InsecureClient
import os

# Set the Kafka bootstrap server and topic
bootstrap_servers = 'localhost:9092'
topic = 'your-topic'

# Set the Hadoop Namenode address
hadoop_namenode_address = "namenode"

# Set the HDFS path
hdfs_path = f"hdfs://{hadoop_namenode_address}:9000/user/root/student_data"

# Connect to HDFS
hdfs_client = InsecureClient(f'http://{hadoop_namenode_address}:9870', user='root')

# Connect to Kafka
consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)

# Consume messages from Kafka
for message in consumer:
    try:
        # Assuming the message value is the content of the text file
        content = message.value.decode('utf-8')

        # Generate a unique file name (you can modify this as needed)
        file_name = f"file_{os.urandom(4).hex()}.txt"

        # Write the file content to HDFS
        with hdfs_client.write(f'{hdfs_path}/{file_name}', encoding='utf-8') as file:
            file.write(content)

        print(f"Ingested message into HDFS: {file_name}")

    except Exception as e:
        print(f"Error processing message: {e}")

    finally:
        consumer.close()
