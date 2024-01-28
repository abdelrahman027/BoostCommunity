from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
from django.db import models

class Department(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=255)
    def __str__(self):
        return self.DepartmentName
class JobTitle(models.Model):
    JobTitleID = models.AutoField(primary_key=True)
    JobTitleName = models.CharField(max_length=255)
    Responsibilities = models.TextField()
    Qualifications = models.TextField()
    def __str__(self):
        return self.JobTitleName  
class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField()
    Phone = models.CharField(max_length=20)
    Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    JobTitle = models.ForeignKey(JobTitle, on_delete=models.SET_NULL, null=True)
    HireDate = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    EmployeePhoto = models.ImageField(upload_to='employee_photos/', null=True, blank=True)
    def __str__(self):
        return self.FirstName      
class Status(models.Model):
    StatusID = models.AutoField(primary_key=True)
    StatusName = models.CharField(max_length=255)
    StatusDescription = models.TextField()
    def __str__(self):
        return self.StatusName  
class Task(models.Model):
    TaskID = models.AutoField(primary_key=True)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    TaskName = models.CharField(max_length=255)
    Description = models.TextField()
    Deadline = models.DateField()
    TaskDuration = models.IntegerField()
    TaskPriority = models.CharField(max_length=10)
    def __str__(self):
        return self.TaskName  
class TaskProgress(models.Model):
    ProgressID = models.AutoField(primary_key=True)
    Task = models.ForeignKey(Task, on_delete=models.CASCADE)
    Status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Comments = models.TextField()
    def __str__(self):
        return str(self.Status) 
class Performance(models.Model):
    PerformanceID = models.AutoField(primary_key=True)
    Employee = models.OneToOneField(Employee, on_delete=models.CASCADE)  # OneToOneField instead of ForeignKey
    TaskPoints = models.IntegerField()
    QualityPoints = models.IntegerField()
    HoursWorkedPoints = models.IntegerField()
    MeetingAttendancePoints = models.IntegerField()
    TotalPoints = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)    
    Badge = models.ForeignKey('Badge', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.Employee.FirstName} - TaskPoints: {self.TaskPoints}'

class Badge(models.Model):
    BadgeID = models.AutoField(primary_key=True)
    BadgeName = models.CharField(max_length=255)
    Description = models.TextField()
    BadgeImage = models.ImageField(upload_to='badge_images/', null=True, blank=True)
    def __str__(self):
        return self.BadgeName
class Salesman(models.Model):
    SalesmanID = models.AutoField(primary_key=True)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    SalesTarget = models.DecimalField(max_digits=10, decimal_places=2)
    SalesAchievement = models.DecimalField(max_digits=10, decimal_places=2)
    SalesProgress = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f'{self.Employee.FirstName} - Sales Target: {self.SalesTarget}'

class Trainer(models.Model):
    TrainerID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20)
    Qualifications = models.TextField()
    Certificates = models.TextField()
    def __str__(self):
        return self.FirstName  
class Course(models.Model):
    CourseID = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=255)
    Description = models.TextField()
    StartDate = models.DateField()
    EndDate = models.DateField()
    PublicCourse = models.BooleanField()
    CourseMaterialsURL = models.URLField()
    def __str__(self):
        return self.CourseName  
class SalesmanCourseAssignment(models.Model):
    AssignmentID = models.AutoField(primary_key=True)
    Salesman = models.ForeignKey(Salesman, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    AssignmentDate = models.DateField()
    def __str__(self):
        return f'Salesman: {self.Salesman.Employee.FirstName} - Course: {self.Course.CourseName} - AssignmentID: {self.AssignmentID}'

class TrainerCourseAssignment(models.Model):
    AssignmentID = models.AutoField(primary_key=True)
    Trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    AssignmentDate = models.DateField()
    def __str__(self):
        return f'Trainer: {self.Trainer.FirstName} - Course: {self.Course.CourseName} - AssignmentID: {self.AssignmentID}'
class EmployeeBadge(models.Model):
    EmployeeBadgeID = models.AutoField(primary_key=True)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Badge = models.ForeignKey(Badge, on_delete=models.SET_NULL, null=True)
    DateEarned = models.DateField()
    def __str__(self):
        return f'{self.Employee.FirstName} - Badge: {self.Badge.BadgeName} - BadgeID: {self.EmployeeBadgeID}'

class Meeting(models.Model):
    MeetingID = models.AutoField(primary_key=True)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    MeetingDate = models.DateField()
    AttendanceStatus = models.BooleanField()
    MinutesDuration = models.IntegerField()
    def __str__(self):
        return f'{self.Employee.FirstName} - Attendance: {self.AttendanceStatus}'
class TaskQualityRating(models.Model):
    RatingID = models.AutoField(primary_key=True)
    Task = models.ForeignKey(Task, on_delete=models.CASCADE)
    QualityRating = models.IntegerField()
    Reviewer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Task: {self.Task.TaskName} - Quality Rating: {self.QualityRating}'
# ... (remaining code)
class EmployeeSkill(models.Model):
    SkillID = models.AutoField(primary_key=True)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    SkillName = models.CharField(max_length=255)
    SkillLevel = models.IntegerField()
    def __str__(self):
        return f'{self.Employee.FirstName} - Skill: {self.SkillName} - Level: {self.SkillLevel}'

class TaskDeliverable(models.Model):
    DeliverableID = models.AutoField(primary_key=True)
    Task = models.ForeignKey(Task, on_delete=models.CASCADE)
    DeliverableName = models.CharField(max_length=255)
    DeliverableDescription = models.TextField()
    DeliverableFile = models.FileField(upload_to='deliverables/',default='default_file.pdf')
    def __str__(self):
        return self.DeliverableName  
    