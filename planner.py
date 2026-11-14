def add_study_task(tasks, title, minutes):
    """Add a study task when the title and duration are valid."""
    title = title.strip()

    if title == "":
        print("Task title is required")
        return tasks

    if minutes <= 0:
        print("Minutes must be positive")
        return tasks

    tasks.append({"title": title, "minutes": minutes})
    return tasks
