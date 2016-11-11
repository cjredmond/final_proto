def group_stuff(queryset):
    assign = []
    for number,team in enumerate(queryset):
        assign.append([number,team])
    print(assign)

#group_stuff(['connor','jack','dolan','bill','steve','dzus'])


# def sched(group_stuff):
#     change = group_stuff
#     amount = len(group_stuff)
#     matchups = []
#     blank = []
#
#     for item in change:
#         new = item
#         change.remove(item)
#         blank.append(new)
#         for item in change:
#             matchups.append([new,item])
#
#
#     print(blank)
#     print(matchups)


sched(['connor','jack','dolan','bill','steve','dzus'])
