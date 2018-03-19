from celery import shared_task
from django_celery_results.task import OperationTask


@shared_task(bind=True, base=OperationTask)
def test_task(self):
    return True
