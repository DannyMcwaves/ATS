# config file for Celery Daemon

# default RabbitMQ broker
broker_url = 'amqp://'

# using a more persistent database for backend purposes.
result_backend = 'mongodb://localhost:27017/ats'

# enable utc timezone configuration.
enable_utc = True

# the color of the worker logs.
worker_log_color = '#cc3366'
