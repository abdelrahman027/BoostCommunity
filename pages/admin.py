from django.contrib import admin
from .models import Department, JobTitle, Employee, Status, Task, TaskProgress, Performance, Badge, Salesman, Trainer, Course, SalesmanCourseAssignment, TrainerCourseAssignment, EmployeeBadge, Meeting, TaskQualityRating, EmployeeSkill, TaskDeliverable
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
class ExportExcelMixin:
    def export_as_excel(modeladmin, request, queryset):
        # Implementation of export logic
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'
        # Your export logic here
        return response

    export_as_excel.short_description = "Export selected items as Excel"

class ExportWordMixin:
    def export_as_word(modeladmin, request, queryset):
        # Implementation of export logic
        response = HttpResponse(content_type='application/ms-word')
        response['Content-Disposition'] = 'attachment; filename="exported_data.docx"'
        # Your export logic here
        return response

    export_as_word.short_description = "Export selected items as Word"

class DepartmentAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('DepartmentID', 'DepartmentName')
    search_fields = ['DepartmentName']
    actions = ['export_as_excel', 'export_as_word']

class JobTitleAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('JobTitleID', 'JobTitleName', 'Responsibilities', 'Qualifications')
    search_fields = ['JobTitleName', 'Responsibilities', 'Qualifications']
    actions = ['export_as_excel', 'export_as_word']

class EmployeeAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('EmployeeID', 'display_employee_image', 'FirstName', 'LastName', 'Email', 'Phone', 'Department', 'JobTitle', 'HireDate', 'user')
    search_fields = ['FirstName', 'LastName', 'Email', 'Phone']
    list_filter = ['Department', 'JobTitle', 'HireDate']
    list_editable = ['Email', 'Phone', 'Department', 'JobTitle', 'HireDate', 'user']
    list_display_links = ['FirstName', 'LastName']

    def display_employee_image(self, obj):
        # Assuming you have a 'EmployeePhoto' field in your model that stores the image URL
        if obj.EmployeePhoto:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.EmployeePhoto.url))
        return None

    display_employee_image.short_description = 'Employee Image'
class StatusAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('StatusID', 'StatusName', 'StatusDescription')
    search_fields = ['StatusName', 'StatusDescription']
    actions = ['export_as_excel', 'export_as_word']

class TaskAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('TaskID', 'Employee', 'TaskName', 'Description', 'Deadline', 'TaskDuration', 'TaskPriority')
    search_fields = ['TaskName', 'Description', 'TaskPriority']
    list_filter = ['Employee', 'TaskPriority']
    list_editable = ['Description', 'Deadline', 'TaskDuration', 'TaskPriority']
    list_display_links = ['TaskName']
    actions = ['export_as_excel', 'export_as_word']

class TaskProgressAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('ProgressID', 'Task', 'Status', 'StartDate', 'EndDate', 'Comments')
    search_fields = ['Task__TaskName', 'Status__StatusName', 'Comments']
    list_filter = ['Status', 'StartDate', 'EndDate']
    list_editable = ['Status', 'StartDate', 'EndDate', 'Comments']
    list_display_links = ['Task']
    actions = ['export_as_excel', 'export_as_word']

class PerformanceAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('PerformanceID', 'Employee', 'TaskPoints', 'QualityPoints', 'HoursWorkedPoints', 'MeetingAttendancePoints', 'TotalPoints', 'Badge')
    search_fields = ['Employee__FirstName', 'Employee__LastName']
    list_filter = ['TaskPoints', 'QualityPoints', 'HoursWorkedPoints', 'MeetingAttendancePoints', 'TotalPoints', 'Badge']
    list_editable = ['TaskPoints', 'QualityPoints', 'HoursWorkedPoints', 'MeetingAttendancePoints', 'TotalPoints', 'Badge']
    list_display_links = ['Employee']
    actions = ['export_as_excel', 'export_as_word']

class BadgeAdmin(ImportExportModelAdmin):
    list_display = ('BadgeID', 'display_badge_image', 'BadgeName', 'Description', 'BadgeImage')
    search_fields = ['BadgeName', 'Description']
    list_editable = ['Description']
    list_display_links = ['BadgeName']

    def display_badge_image(self, obj):
        # Assuming you have a 'BadgeImage' field in your model that stores the image URL
        if obj.BadgeImage:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.BadgeImage.url))
        return None

    display_badge_image.short_description = 'Badge Image'
# Repeat the pattern for other models...
# ... (previous code)

class SalesmanAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('SalesmanID', 'Employee', 'SalesTarget', 'SalesAchievement', 'SalesProgress')
    search_fields = ['Employee__FirstName', 'Employee__LastName']
    list_editable = ['SalesTarget', 'SalesAchievement', 'SalesProgress']
    list_display_links = ['Employee']
    actions = ['export_as_excel', 'export_as_word']

class TrainerAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('TrainerID', 'FirstName', 'LastName', 'Phone', 'Qualifications', 'Certificates')
    search_fields = ['FirstName', 'LastName', 'Phone', 'Qualifications', 'Certificates']
    list_editable = ['Phone', 'Qualifications', 'Certificates']
    list_display_links = ['FirstName', 'LastName']
    actions = ['export_as_excel', 'export_as_word']

class CourseAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('CourseID', 'CourseName', 'Description', 'StartDate', 'EndDate', 'PublicCourse', 'CourseMaterialsURL')
    search_fields = ['CourseName', 'Description']
    list_editable = ['Description', 'StartDate', 'EndDate', 'PublicCourse', 'CourseMaterialsURL']
    list_display_links = ['CourseName']
    actions = ['export_as_excel', 'export_as_word']

class SalesmanCourseAssignmentAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('AssignmentID', 'Salesman', 'Course', 'AssignmentDate')
    search_fields = ['Salesman__Employee__FirstName', 'Salesman__Employee__LastName', 'Course__CourseName']
    list_editable = ['Course', 'AssignmentDate']
    list_display_links = ['Salesman']
    actions = ['export_as_excel', 'export_as_word']

class TrainerCourseAssignmentAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('AssignmentID', 'Trainer', 'Course', 'AssignmentDate')
    search_fields = ['Trainer__FirstName', 'Trainer__LastName', 'Course__CourseName']
    list_editable = ['Course', 'AssignmentDate']
    list_display_links = ['Trainer']
    actions = ['export_as_excel', 'export_as_word']

# Continue the pattern for other models...
# ... (previous code)

class EmployeeBadgeAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('EmployeeBadgeID', 'Employee', 'Badge', 'DateEarned')
    search_fields = ['Employee__FirstName', 'Employee__LastName', 'Badge__BadgeName']
    list_editable = ['Badge', 'DateEarned']
    list_display_links = ['Employee']
    actions = ['export_as_excel', 'export_as_word']

class MeetingAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('MeetingID', 'Employee', 'MeetingDate', 'AttendanceStatus', 'MinutesDuration')
    search_fields = ['Employee__FirstName', 'Employee__LastName', 'AttendanceStatus']
    list_editable = ['MeetingDate', 'AttendanceStatus', 'MinutesDuration']
    list_display_links = ['Employee']
    actions = ['export_as_excel', 'export_as_word']

class TaskQualityRatingAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('RatingID', 'Task', 'QualityRating', 'Reviewer')
    search_fields = ['Task__TaskName', 'QualityRating', 'Reviewer__FirstName', 'Reviewer__LastName']
    list_editable = ['QualityRating', 'Reviewer']
    list_display_links = ['Task']
    actions = ['export_as_excel', 'export_as_word']

class EmployeeSkillAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('SkillID', 'Employee', 'SkillName', 'SkillLevel')
    search_fields = ['Employee__FirstName', 'Employee__LastName', 'SkillName']
    list_editable = ['SkillName', 'SkillLevel']
    list_display_links = ['Employee']
    actions = ['export_as_excel', 'export_as_word']

class TaskDeliverableAdmin(ImportExportModelAdmin, ExportExcelMixin, ExportWordMixin):
    list_display = ('DeliverableID', 'Task', 'DeliverableName', 'DeliverableDescription', 'DeliverableFile')
    search_fields = ['Task__TaskName', 'DeliverableName', 'DeliverableDescription']
    list_editable = ['DeliverableName', 'DeliverableDescription']
    list_display_links = ['Task']
    actions = ['export_as_excel', 'export_as_word']

# Register your models with the customized admin classes
admin.site.register(EmployeeBadge, EmployeeBadgeAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(TaskQualityRating, TaskQualityRatingAdmin)
admin.site.register(EmployeeSkill, EmployeeSkillAdmin)
admin.site.register(TaskDeliverable, TaskDeliverableAdmin)
admin.site.register(Salesman, SalesmanAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(SalesmanCourseAssignment, SalesmanCourseAssignmentAdmin)
admin.site.register(TrainerCourseAssignment, TrainerCourseAssignmentAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(JobTitle, JobTitleAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskProgress, TaskProgressAdmin)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Badge, BadgeAdmin)
admin.site.site_header= "Boost Community"
admin.site.site_title="Boost Community"