#create a form that can input the follow data :
# Date: 2025-12-04
# Task: 
# Description:
# Status:
# Remarks:

# after inputting the data, it should be saved in a file named dar {date}.txt in the following format: (can be more than one task accomplished in a day)

import os
from datetime import datetime

def get_task_input():
    """Collect task information from user input"""
    print("\n=== DAR (Daily Activity Report) Form ===\n")
    
    date = input("Date (YYYY-MM-DD) [default: today]: ").strip() or datetime.now().strftime("%Y-%m-%d")
    task = input("Task: ").strip()
    description = input("Description: ").strip()
    status = input("Status (Completed/In Progress/Pending): ").strip()
    remarks = input("Remarks: ").strip()
    
    return {
        "date": date,
        "task": task,
        "description": description,
        "status": status,
        "remarks": remarks
    }

def save_task(task_data):
    """Save task data to a file named dar_{date}.txt"""
    filename = f"dar_{task_data['date']}.txt"
    
    # Format the task entry
    entry = f"""
Date: {task_data['date']}
Task: {task_data['task']}
Description: {task_data['description']}
Status: {task_data['status']}
Remarks: {task_data['remarks']}
{'='*50}"""
    
    # Append to file (creates if doesn't exist)
    with open(filename, "a") as f:
        f.write(entry + "\n")
    
    print(f"\n✓ Task saved to {filename}")

def main():
    """Main function to run the DAR form"""
    while True:
        task_data = get_task_input()
        save_task(task_data)
        
        another = input("\nAdd another task? (y/n): ").strip().lower()
        if another != 'y':
            print("Thank you for using DAR Form!")
            break

if __name__ == "__main__":
    main()