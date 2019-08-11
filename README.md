# Para chamar os workers (que consomem a fila)
celery -A tarefa_example.celery_app worker -l debug


# Para chamar o beat (os que tem a agenda de tarefas)
celery beat -A tarefa_example.celery_app -l DEBUG


