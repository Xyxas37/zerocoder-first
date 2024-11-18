class Task ():
    def __init__(self, task, date, status):
        self.task = task
        self.date = date
        self.status = status


    def addtask(self):
        ts = input(f"введите задачу")
        self.task = ts
        return self.task

    def done(self):
        if self.status == "выполнено":
            print(f'выполненные задачи - {self.task} ')

    def n_done(self):
        if self.status == "не выполнено":
            print(f'список текущих задач - {self.task} ')

t1 = Task (task="попить воды", date="1 день" , status="выполнено")
t2 = Task (task="сделать домашку ", date="1 день" , status="не выполнено")
t3 = Task (task="нарисовать картину", date="13 дней" , status="не выполнено")
t4 = Task (task="заработать миллион", date="138 дней" , status="выполнено")

t2.addtask()

t1.done()
t2.done()
t3.done()
t4.done()

t1.n_done()
t2.n_done()
t3.n_done()
t4.n_done()