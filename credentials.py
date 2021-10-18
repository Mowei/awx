DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "dXpYMFFjVUNQbnZZWkJlZ04tWkhuM1k1NUt5RFlXbWFMdVlhSURnTm9NR3o4NzBaSllHWUlLRTJUQk4tMUtpUFdQLU1zVTFoeDNBd3JCMGZTalJpT1ZqOnR0cy5aZFZHd3NIY1FLNUxqODBuaTdFMW9LaCxZTThCWGNXLGFVMXo="
