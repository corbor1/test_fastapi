


from confluent_kafka import Producer, Consumer # type: ignore

conf = {'bootstrap.servers': '127.0.0.1:9092'}

producer = Producer(conf)
# consumer = Consumer(conf)
