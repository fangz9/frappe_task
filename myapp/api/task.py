import frappe

@frappe.whitelist(allow_guest=False)
def create_task():
    """Create a Task using JSON payload"""
    data = frappe.form_dict  

    required_fields = ["title", "description", "status", "due_date", "assigned_to"]
    if not all(field in data for field in required_fields):
        return {"error": "Missing required fields"}

    task = frappe.get_doc({
        "doctype": "Task",
        "title": data.get("title"),
        "description": data.get("description"),
        "status": data.get("status"),
        "priority": data.get("priority"),
        "due_date": data.get("due_date"),
        "assigned_to": data.get("assigned_to")  # Ensure this is included
    })
    task.insert()
    return {"message": "Task created successfully", "task": task}

@frappe.whitelist(allow_guest=False)
def get_tasks(limit_start=0, limit_page_length=20):
    """Retrieve a paginated list of Tasks"""
    tasks = frappe.get_list("Task",
        fields=["name", "title", "status", "due_date"],
        limit_start=int(limit_start),
        limit_page_length=int(limit_page_length)
    )
    return {"data": tasks}

@frappe.whitelist(allow_guest=False)
def get_task(task_id):
    """Retrieve a specific Task by ID"""
    try:
        task = frappe.get_doc("Task", task_id)
        return task
    except frappe.DoesNotExistError:
        return {"error": "Task not found"}

@frappe.whitelist(allow_guest=False)
def update_task():
    """Update an existing Task"""
    data = frappe.form_dict  # Read JSON request body

    if "task_id" not in data:
        return {"error": "Task ID is required"}

    try:
        task = frappe.get_doc("Task", data.get("task_id"))

        # Update fields if provided
        if "title" in data:
            task.title = data.get("title")
        if "description" in data:
            task.description = data.get("description")
        if "status" in data:
            task.status = data.get("status")
        if "due_date" in data:
            task.due_date = data.get("due_date")

        task.save()
        return {"message": "Task updated successfully", "task": task}
    except frappe.DoesNotExistError:
        return {"error": "Task not found"}

@frappe.whitelist(allow_guest=False)
def delete_task():
    """Delete a Task"""
    data = frappe.form_dict

    if "task_id" not in data:
        return {"error": "Task ID is required"}

    try:
        frappe.delete_doc("Task", data.get("task_id"))
        return {"message": "Task deleted successfully"}
    except frappe.DoesNotExistError:
        return {"error": "Task not found"}

