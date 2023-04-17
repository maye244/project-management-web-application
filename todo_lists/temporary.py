# counts_data = Todo.objects.annotate(
    #     to_do_count = Count('pk', filter=Q(status='to_do')),
    #     in_progress_count = Count('pk', filter=Q(status='in_progress')),
    #     done_count = Count('pk', filter=Q(status='done'))
    #     )
    #     
    #      todos = project.todo_set.filter(status='to_do')
    # progresses = project.todo_set.filter(status='in_progress')
    # dones = project.todo_set.filter(status='done')