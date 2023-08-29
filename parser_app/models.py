from django.db import models


class BaseTask(models.Model):
    """ Celery task info"""
    themes = models.CharField(max_length=250)
    count_solution = models.IntegerField()
    name_and_number = models.CharField(max_length=250)
    complexity_task = models.IntegerField()
    is_success = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_and_number


class BaseParsingResult(models.Model):
    """ Parsing result details"""
    task_id = models.ForeignKey(
        BaseTask,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    data = models.TextField(blank=True)
    task_type = models.CharField(blank=True, max_length=64)
