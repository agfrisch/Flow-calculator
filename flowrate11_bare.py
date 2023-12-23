from datetime import datetime, timedelta

def get_time_input(prompt):
    while True:
        try:
            time_input = input(prompt)
            time_object = datetime.strptime(time_input, "%H:%M")
            return time_object
        except ValueError:
            try:
                time_object = datetime.strptime(time_input, "%H%M")
                return time_object
            except ValueError:
                print("Please enter a valid time (HH:mm).")

def get_start_time():
    return get_time_input("Enter start time (HH:mm): ")

def get_anticipated_volume():
    try:
        anticipated_volume = int(input("Enter anticipated SPA volume for the day: "))
        return anticipated_volume
    except ValueError:
        print("Please enter a valid number.")
        return None

def calculate_projected_finish_time(start_time, anticipated_volume, anticipated_flow_rate):
    total_pieces_needed = anticipated_volume
    projected_finish_time = start_time + timedelta(minutes=(total_pieces_needed / anticipated_flow_rate) * 60)
    return projected_finish_time + timedelta(minutes=10)

def get_user_inputs():
    try:
        current_spa_volume = int(input("Enter current SPA volume: "))
        current_time = get_time_input("Enter current time (HH:mm): ")
        return current_spa_volume, current_time
    except ValueError:
        print("Please enter valid values.")
        return None, None

def calculate_hourly_flow_rate(start_time, current_spa_volume, current_time):
    time_difference = current_time - start_time
    minutes_past_hour = int(time_difference.total_seconds() / 60)

    if minutes_past_hour == 0:
        hourly_flow_rate = current_spa_volume
    else:
        hourly_flow_rate = round((current_spa_volume / minutes_past_hour) * 60)
    return hourly_flow_rate

def calculate_time_off(new_time, original_time):
    time_difference = new_time - original_time
    hours, remainder = divmod(abs(time_difference.total_seconds()), 3600)
    minutes = remainder // 60

    if time_difference.total_seconds() >= 0:
        return f"+{int(hours)} hours and {int(minutes)} minutes"
    else:
        return f"-{int(hours)} hours and {int(minutes)} minutes"

def main():
    print("\nHourly Flow Calculator\n")

    start_time = get_start_time()
    if start_time is None:
        return

    anticipated_volume = get_anticipated_volume()
    if anticipated_volume is None:
        return

    anticipated_flow_rate = 3000
    projected_finish_time = calculate_projected_finish_time(start_time, anticipated_volume, anticipated_flow_rate)
    
    print(f"Projected Finish Time: {projected_finish_time.strftime('%H:%M')}")

    while True:
        current_spa_volume, current_time = get_user_inputs()
        if current_spa_volume is None or current_time is None:
            continue

        hourly_flow_rate = calculate_hourly_flow_rate(start_time, current_spa_volume, current_time)
        anticipated_flow_rate = hourly_flow_rate  # Update the anticipated flow rate based on actual flow rate
        new_projected_finish_time = calculate_projected_finish_time(start_time, anticipated_volume, anticipated_flow_rate)

        time_off = calculate_time_off(new_projected_finish_time, projected_finish_time)

        print(
            f"Hourly flow rate: {hourly_flow_rate:,.0f}\n"
            f"New Projected Finish Time: {new_projected_finish_time.strftime('%H:%M')}\n"
            f"Time Off: {time_off}\n"
        )

        try:
            print("Recalculate?")
            running = input("Enter 'y' for yes, any other key to exit: ")
        
            if running.lower() != 'y':
                print("Goodbye!")
                break
        except ValueError:
            continue

if __name__ == "__main__":
    main()
