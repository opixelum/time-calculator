def add_time(start, duration, day=None):
    # Defining the days of the week for later use
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    # Splitting the start time into hours, minutes, and period (AM/PM)
    start_hours, start_minutes = map(int, start.split()[0].split(':'))
    period = start.split()[1].lower()
    
    # Splitting the duration into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(':'))
    
    # Calculating the new hours and minutes
    new_minutes = (start_minutes + duration_minutes) % 60
    hours_carry = (start_minutes + duration_minutes) // 60
    new_hours = start_hours + duration_hours + hours_carry
    
    # Calculating the number of days passed and the new period (AM/PM)
    days_passed = 0
    while new_hours >= 12:
        new_hours -= 12
        if period == "pm":
            days_passed += 1
        period = "pm" if period == "am" else "am"
    
    # Correcting for the case where the hour becomes 0
    if new_hours == 0:
        new_hours = 12
    
    # Constructing the new time string
    new_time = f"{new_hours}:{str(new_minutes).zfill(2)} {'AM' if period == 'am' else 'PM'}"
    
    # If a starting day is provided, calculate the new day
    if day:
        current_day_index = days_of_week.index(day.lower())
        new_day_index = (current_day_index + days_passed) % 7
        new_time += f", {days_of_week[new_day_index].capitalize()}"
    
    # Adding the number of days passed to the new time string
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"
    
    return new_time
