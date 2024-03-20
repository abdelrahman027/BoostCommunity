from .models import Employee,Performance,Client
employeesCount = Employee.objects.all().count()
clientCount = Client.objects.all().count()

PerformanceAsc = Performance.objects.all().order_by("TotalPoints")
PerformanceDes = Performance.objects.all().order_by("-TotalPoints")

conversation = [
    "Hello",#me
    "Hi there!",#bot
    "How are you doing?",#me
    "I'm doing great.",#bot
    "That is good to hear",#me
    "Thank you.",#bot
    "You're welcome.",#me
    "How many employees in Boost ?",
    f"Right now as far as i know around {employeesCount} employees are working in the company",
    "Best employee ?",
    f"the best Employee right now is {PerformanceDes[0].Employee} with Total points of {PerformanceDes[0].TotalPoints}",
    "Lowest employee ?",
    f"the Lowest Employee right now is {PerformanceAsc[0].Employee} with Total points of {PerformanceAsc[0].TotalPoints}",
    "How many clients we have ?",
    f"Currently we have {clientCount} Clients",
    "How can i use this website ?",
    "well, if you are a regular employee you can view your tasks and know the deadlines and priority , you can add your activity during the day of working and you can view trainers and courses we have and much more, else if you are an admin I am all yours :D ",
]