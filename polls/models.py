from django.db import models
from django.utils.encoding import python_3_unicode_compatible
from django.utils import timezone
# Create your models here.
@python_3_unicode_compatible
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def question_str(self):
        return self.question_text


        

@python_3_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def choice_str(self):
		return self.choice_text
		