from confluent_kafka import Producer, Consumer # type: ignore

conf = {
    'bootstrap.servers': 'kafka:9092',   # ключ — имя настройки, значение — адрес
}

producer = Producer(conf)
# consumer = Consumer(conf)