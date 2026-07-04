import os
import pika
import logging
from uuid import UUID

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

RM_HOST = os.environ.get("RM_HOST", "rabbitmq")
RM_PORT = int(os.environ.get("RM_PORT", "5672"))
RM_USER = os.environ.get("RM_USER", "rmuser")
RM_PASS = os.environ.get("RM_PASS", "rmpassword")
RM_VHOST = os.environ.get("RM_VHOST", "/")


connection_params = pika.ConnectionParameters(
    host=RM_HOST,
    port=RM_PORT,
    virtual_host=RM_VHOST,
    credentials=pika.PlainCredentials(username=RM_USER, password=RM_PASS),
    heartbeat=30,
    blocked_connection_timeout=2
)

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
queue_name = 'ml_task_queue'
channel.queue_declare(queue=queue_name)


def callback(ch, method, properties, body):
    task_id_str = body.decode("utf-8").strip()
    logger.info("Received task_id: '%s'", task_id_str)


# Подписка на очередь и установка обработчика сообщений
channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=False  # Автоматическое подтверждение обработки сообщений
)

logger.info('Waiting for messages. To exit, press Ctrl+C')
channel.start_consuming()