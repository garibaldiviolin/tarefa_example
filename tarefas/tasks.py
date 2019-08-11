from tarefa_example.celery_app import app


@app.task(bind=True)
def teste_echo(self):
    print('Essa ecoou!\n' * 3)


@app.task(bind=True)
def tarefa_legal(self):
    print('Essa tarefa é bem legal!\n' * 3)


@app.task(bind=True)
def olha_isso(self):
    print('Olha isso aqui!\n' * 3)


@app.task(bind=True)
def agora_vai(self):
    print('Agora vai!!!!!\n' * 3)
