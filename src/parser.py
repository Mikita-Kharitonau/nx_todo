import argparse


def parse(arguments):
    parser = argparse.ArgumentParser(description='nx_todo')
    subparsers_for_command = parser.add_subparsers(dest='command')

    # Parsing the 'show' command
    parser_show = subparsers_for_command.add_parser('show')
    subparsers_for_show = parser_show.add_subparsers(dest='kind')

    parser_show_task = subparsers_for_show.add_parser('task')
    show_task_group = parser_show_task.add_mutually_exclusive_group(required=True)
    show_task_group.add_argument('-a', '--all', action='store_true')
    show_task_group.add_argument('-t', '--title')
    show_task_group.add_argument('-c', '--category')
    parser_show_task.add_argument('-f', '--full', action='store_true')

    parser_show_event = subparsers_for_show.add_parser('event')
    show_event_group = parser_show_event.add_mutually_exclusive_group(required=True)
    show_event_group.add_argument('-a', '--all', action='store_true')
    show_event_group.add_argument('-t', '--title')
    show_event_group.add_argument('-c', '--category')
    parser_show_event.add_argument('-f', '--full', action='store_true')

    parser_show_all = subparsers_for_show.add_parser('all')
    show_all_group = parser_show_all.add_mutually_exclusive_group(required=True)
    show_all_group.add_argument('-a', '--all', action='store_true')
    show_all_group.add_argument('-t', '--title')
    show_all_group.add_argument('-c', '--category')
    parser_show_all.add_argument('-f', '--full', action='store_true')

    # Parsing the 'add' command
    parser_add = subparsers_for_command.add_parser('add')
    subparsers_for_add = parser_add.add_subparsers(dest='kind')

    parser_add_task = subparsers_for_add.add_parser('task')
    parser_add_task.add_argument('title')
    parser_add_task.add_argument('-D', '--description')
    parser_add_task.add_argument('-r', '--reminder')
    parser_add_task.add_argument('-c', '--category')
    parser_add_task.add_argument('-o', '--owners')
    parser_add_task.add_argument('-d', '--deadline')
    parser_add_task.add_argument('-p', '--priority', type=int)
    parser_add_task.add_argument('-s', '--status')
    parser_add_task.add_argument('-S', '--subtasks')

    parser_add_event = subparsers_for_add.add_parser('event')
    parser_add_event.add_argument('title')
    parser_add_event.add_argument('-D', '--description')
    parser_add_event.add_argument('-r', '--reminder')
    parser_add_event.add_argument('-c', '--category')
    parser_add_event.add_argument('-df', '--datefrom')
    parser_add_event.add_argument('-tf', '--timefrom')
    parser_add_event.add_argument('-dt', '--dateto')
    parser_add_event.add_argument('-tt', '--timeto')
    parser_add_event.add_argument('-t', '--time')
    parser_add_event.add_argument('-P', '--place')
    parser_add_event.add_argument('-p', '--participants')


    # Parsing the 'del' command
    parser_del = subparsers_for_command.add_parser('del')
    subparsers_for_del = parser_del.add_subparsers(dest='kind')

    parser_del_task = subparsers_for_del.add_parser('task')
    del_task_group = parser_del_task.add_mutually_exclusive_group(required=True)
    del_task_group.add_argument('-t', '--title')
    del_task_group.add_argument('-c', '--category')

    parser_del_event = subparsers_for_del.add_parser('event')
    del_event_group = parser_del_event.add_mutually_exclusive_group(required=True)
    del_event_group.add_argument('-t', '--title')
    del_event_group.add_argument('-c', '--category')

    args = parser.parse_args(arguments)
    return args