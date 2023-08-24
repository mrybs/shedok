from shedok import Shedule, Sheduler
from datetime import datetime, timedelta

def task(*args):
	print(f'Hello from task {args[0]}')
	print(f'At {datetime.now()}')

app = Sheduler()
now = datetime.now()
app.add(Shedule(task, now+timedelta(seconds=5), 2))
app.add(Shedule(task, now+timedelta(seconds=10), 1))
app.run()

while app.alive:
	pass