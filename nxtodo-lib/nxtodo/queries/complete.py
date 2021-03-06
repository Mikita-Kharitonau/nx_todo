from nxtodo.queries import (
    get_task,
    get_event
)
from nxtodo.queries import (
    user_task_access,
    user_event_access
)
from nxtodo.common import Statuses
from nxtodo.common.exceptions import CompletionError
from nxtodo.queries.logging_decorators import log_query


@log_query("Successfully completed '{}' task by user '{}'",
           "Error when completing '{}' task by user '{}'")
@user_task_access
def complete_task(user_name, task_id):
    """
    Complete task if it can be completed.
    """
    task = get_task(task_id)
    if task.can_complete():
        task.status = Statuses.FULFILLED.value
        task.save()
    else:
        msg = ("You can't complete '{}' task, "
              "because it has uncompleted subtasks".format(task_id))
        raise CompletionError(msg)


@log_query("Successfully completed '{}' event by user '{}'",
           "Error when completing '{}' event by user '{}'")
@user_event_access
def complete_event(user_name, event_id):
    """
    Complete event if user 'username' has authority to do this.
    """
    event = get_event(event_id)
    event.status = Statuses.FULFILLED.value
    event.save()