from agentic_ai.sandbox import SandboxPlan, validate_code_for_demo

code = "print(sum([1, 2, 3]))"
allowed, reason = validate_code_for_demo(code)
print("static gate:", allowed, reason)
print("required isolation:", SandboxPlan())
print("NOTE: this demo does not execute model-generated code on the host.")
