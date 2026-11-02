from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:9092'],  # Укажите адрес вашего кластера
    sasl_mechanism='SCRAM-SHA-256',  # Механизм аутентификации (например, SCRAM-SHA-512)
    security_protocol='SASL_SSL',  # Протокол безопасности (SASL_SSL, SSL)
    sasl_plain_username='username',  # Имя пользователя для SASL
    sasl_plain_password='password'  # Пароль для SASL
)
