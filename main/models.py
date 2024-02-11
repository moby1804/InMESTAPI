from django.db import models
import datetime
from users.models import Cohort, IMuser


# Create your models here.

class Course(models.Model):
  name=models.CharField(max_length=1000)
  descripton = models.TextField(default='N/A', blank=True, null=True)
  date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
  date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
  
  
  def __str__(self):
      return f"{self.name}"
    
# ClassSchedule (title, description, start_date_and_time, end_date_and_time, is_repeated, repeat_frequency, is_active, organizer, cohort [should reference Cohort model], venue)
# ClassAttendance(class_schedule [Should reference ClassSchedule model], attendee [should reference IMUser model], is_present, date_created, date_modified, author [should reference IMUser model])
# Query (title, description, submitted_by [should reference IMUser], assigned_to [should reference IMUser], resolution_status [PENDING, IN_PROGRESS, DECLINED, RESOLVED], date_created, date_modified, author [should reference IMUser model])
# # QueryComment (query [should reference Query model], comment, date_created, date_modified, author [should reference IMUser model])

class ClassSchedule(models.Model):
      title = models.CharField(max_length=30)
      description = models.TextField(blank=True, null=True)
      state_date_and_time = models.IntegerField()
      end_date_and_time = models.IntegerField()
      is_repeated = models.BooleanField()
      repeat_frequency = models.IntegerField()
      is_active = models.BooleanField()
      organizer = models.CharField(max_length=30)
      cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='cohort_schedule')
      venue = models.CharField(max_length=40, null=True)
      
      def __str__(self):
          return self.title
        
class ClassAttendance(models.Model):
      class_schedule = models.ManyToManyField(ClassSchedule, related_name='attendance_schedule')
      attendee = models.ForeignKey(IMuser,on_delete =models.CASCADE, related_name='attendee_name')
      is_present = models.BooleanField()
      date_created = models.DateTimeField(auto_now_add=True)
      date_modified = models.DateTimeField(auto_now=True)
      author = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name='attendance_author')
      
      def __str__(self):
           return self.attendee
      
class Query(models.Model):
      title = models.CharField(max_length=30)
      description = models.TextField(blank=True, null= True)
      submitted_by = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name='user_query')
      assigned_to = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name ='assignQuery_user')
      resolution_status = models.CharField(max_length=30, choices=[
        ('PENDING', 'PENDING'), ('IN_PROGRESS','IN_PROGRESS'), ('DECLINED', 'DECLINED'), ('RESOLVED', 'RESOLVED')
      
     ]
    )
      date_created = models.DateTimeField(auto_now_add=True)
      date_modified = models.DateTimeField(auto_now=True)
      author = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name='query_author')
      
      def __str__(self):
          return self.title
      
class QueryComment(models.Model):
      query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='query_title')
      comment = models.CharField(max_length=2000)
      date_created = models.DateTimeField(auto_now_add=True)
      date_modified = models.DateTimeField(auto_now=True)
      author = models.ForeignKey(IMuser, on_delete=models.CASCADE, related_name='comment_author')
      
      def __str__(self):
          return self.comment
      
        
        