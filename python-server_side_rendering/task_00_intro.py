#!/usr/bin/python3
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input type: template should be a string.")
        return
    if not isinstance(attendees, list):
        print("Invalid input type: template should be a list of dictionaries.")
        return
    if not template:
        print("Template is empty, no output fils generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for i, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{key}}}", str(value))
        with open(f"output_{i}.txt", "w") as file:
            file.write(content)
