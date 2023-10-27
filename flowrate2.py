

from rich.console import Console
from rich.panel import Panel
console = Console()

console.print(
    Panel.fit(
        " \nHourly Flow Calculator\n ",
        style="bold blue"
    )
)


while True:

    try:
        # Get user inputs
        print("")
        current_units_processed = int(input("Enter current SPA volume: "))
        
        minutes_past_hour = int(input("Enter number of minutes past the hour: "))

        # Calculate the anticipated hourly flow rate
        if minutes_past_hour == 0:
            hourly_flow_rate = current_units_processed
        else:
            hourly_flow_rate = round((current_units_processed / minutes_past_hour) * 60)

        # Print the result
        # print("")
        # console.print(f"Anticipated hourly flow rate: [italic bold red]{hourly_flow_rate:,.0f}[/italic bold red]")
        # print("")
        print("")
        console.print(
            Panel.fit(
                f"Anticipated hourly flow rate: [italic bold red]{hourly_flow_rate:,.0f}[/italic bold red]",
                style="bold blue"
            )
        )
        print("")

    except:
        print("Please enter valid number.")
        continue

    try:
        print("Recalculate?")
        running = input("Enter 'y' for yes, any other key to exit: ")
    
        if running != 'y':
            console.print("[italic bold blue]Goodbye![/italic bold blue]")
            break
        else:
            continue

    except:
        continue
