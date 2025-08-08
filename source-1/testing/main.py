def do_stuff(num=0):
    try:
        if num:
         return int(num) + 5
        else:
            return '_Please provide a valid number_'
    except ValueError as err:
        return err
