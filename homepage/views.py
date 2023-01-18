from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task_data
from datetime import datetime
import pytz
from datetime import timezone


# Create your views here.
@login_required(login_url="login")
def homepage(request):

    if "task_exist" in request.POST:
        # helps to determine what to do, switch task status or delete task
        quest = request.POST.get("assists")
        element_id = request.POST.get("id")
        
        if quest == "delete_task":
            Task_data.objects.filter(id=element_id).delete()
            
        elif quest == "switch_state":
            task = Task_data.objects.get(id=element_id)
            Task_data.objects.filter(id=element_id).update(status=(task.status+1) % 2)

    if "new_task_name" in request.POST:
        task_name = request.POST.get("new_task_name")
        due_date = request.POST.get("date")

        if task_name:

            datetime_object = datetime.strptime(due_date, "%Y-%m-%dT%H:%M")
            tz = pytz.timezone("Asia/Kolkata")
            datetime_object = tz.localize(datetime_object)

            task_db = Task_data(
                name=task_name,
                datetime_iso=due_date,
                datetime=datetime_object,
                status=0,
            )
            task_db.save()
            
    user_id = request.user.id
    tasks = Task_data.objects.filter(user_id=user_id).order_by("datetime")
    
    now = str(datetime.now())
    now = now[:19]
    datetime_object = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
    tz = pytz.timezone("Asia/Kolkata")
    now = tz.localize(datetime_object)

    return render(request, "homepage.html", {"tasks": tasks, "now": now})
