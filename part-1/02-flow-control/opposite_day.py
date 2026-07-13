def main():
    is_opposite_day()

def is_opposite_day():
    today_is_opposite_day = True

    if today_is_opposite_day == True:
        say_it_is_opposite_day = True
    else:
        say_it_is_opposite_day = False
    
    if today_is_opposite_day == True:
        say_it_is_opposite_day = not say_it_is_opposite_day

    if say_it_is_opposite_day == True:
        print("Today is Opposite Day.")
    else:
        print("Today is not Opposite Day.")

if __name__ == '__main__':
    main()