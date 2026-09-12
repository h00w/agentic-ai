roles = {
    "product_manager": "Define acceptance criteria",
    "researcher": "Collect evidence",
    "developer": "Implement",
    "tester": "Verify",
    "reviewer": "Approve or return defects",
}
for role, responsibility in roles.items():
    print(f"{role:16} -> {responsibility}")
