# To run the Big-Data-Project
# KAFKA
1. cd to kafka folder
  run   docker exec -it <kafka_conatiner_id> /bin/sh
2. Go inside kafka installation folder
  cd /opt/kafka_<version>/bin
3. Create topic
  kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic quickstart
4. Run producer.py
   python3 producer.py
5. Run flume-kafka-hdfs.conf to ingest data to hdfs
   flume-ng agent -n agent -c conf -f flume-kafka-hdfs.conf -Dflume.root.logger=INFO,console

# HADOOP
1. Start docker-hadoop container
   cd to docker-hadoop folder
   docker compose up -d
3. Go inside hadoop installation folder
   run  docker exec -it namenode bash
4. go to hadoop webpage
   http://localhost:9870
5. verify the dataset
e.g. hdfs dfs -ls /user/root/student_data

# SPARK
1. Start spark container
   cd to spark folder
   docker compose up
2. Access Jupyter webpage:
e.g. http://127.0.0.1:8888/lab?token=5f27a9c5e9faa2a6f60a4feebfa4452d45fe4beb639ca808

# JUPYTER

*RUN THIS CODE TO LOAD DATA FRON HDFS USING PYSPARK*

    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .appName("SparkExample") \
        .config("spark.eventLog.enabled", "true") \
        .config("spark.eventLog.dir", "file:/home/jovyan/work/logs") \
        .getOrCreate()
    hadoop_namenode_address = "namenode"
    csv_path = f"hdfs://{hadoop_namenode_address}:9000/user/root/student_data/"
    df = spark.read.csv(csv_path, header=True, inferSchema=True)
    df.show(10)
