from nxtodo.thirdparty import (
    Statuses,
    CompletionError
)

from .access_decorators import (
    user_task_access,
    user_event_access
)
from .logging_decorators import log_complete_query
from .common import (
    get_task,
    get_event
)

SUCCESS = 'Successfully completed {} task'
ERROR = 'Error when completing {} task: '
@log_complete_query(SUCCESS, ERROR)
@user_task_access
def complete_task(user_name, task_id):
    task = get_task(task_id)
    if task.can_complete():
        task.status = Statuses.FULFILLED.value
        task.save()
    else:
        msg = ("You can't complete '{}' task, "
              "because it has uncompleted subtasks")
        raise CompletionError(msg)


@user_event_access
def complete_event(user_name, event_id):
    event = get_event(event_id)
    event.status = Statuses.FULFILLED.value
    event.save()