import requests
import time

from lxml import etree
from datetime import datetime
from parser_app.models import BaseTask, BaseParsingResult
from parser_app.celery import app

from django.core.cache import cache


def parse_data(celery_task_id: str, themes: str):
    new_task = BaseTask.objects.create(
        name_and_number=celery_task_id,
    )
    new_task.save()
    try:
        response = requests.get(
            f"https://codeforces.com/problemset?order=BY_SOLVED_DESC&tags={themes}"
        )
        if response.status_code == 200:
            tree = etree.HTML(response.content)
            results = tree.xpath("//article/h3/a")
            for cur in results:
                cur_parsing_res = BaseParsingResult.objects.create(
                    task_id=new_task,
                    data=cur.text,
                    task_type=themes
                )
                cur_parsing_res.save()

    except Exception as e:
        print("Error: ", e)
    else:
        new_task.is_success = True
        new_task.save()


@app.task(name='create_task', bind=True)
def create_task(self, themes):
    parse_data(self.request.id, themes)
    return True
