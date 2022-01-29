# 1 минута = 60 сек. 1 час = 3600 сек. 1 день = 86400сек. 1 год = 31536000.
def convert_time(duration: int) -> str:
    if duration<60:
        new_time=[duration,'сек']
    elif duration<3600:
        new_time=[duration//60, 'мин', duration%60, 'сек']
    elif duration<86400:
        new_time=[duration//3600,'час', duration%3600//60, 'мин', duration%3600%60, 'сек']
#    elif duration<31536000:
    else:
        new_time=[duration//86400, 'дн', duration%86400//3600,'час', duration%86400%3600//60, 'мин', duration%86400%3600%60,'сек']
    return new_time
duration =31645000
result = convert_time(duration)
print(result)

