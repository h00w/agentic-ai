# Security Policy

## Reporting

Please do not disclose exploitable vulnerabilities in a public issue. Contact **hendar@hendarmawan.se** with a concise reproduction, affected path/version, impact, and suggested mitigation when available.

## Security design principles

- least privilege and explicit tool allowlists
- defense in depth
- human approval for high-impact actions
- no direct host execution of model-generated code
- input and output validation
- sandboxing and resource limits
- secrets through environment/configuration systems, never source control
- network restrictions for execution environments
- auditable tool calls and policy decisions
- bounded retries, token budgets, rate limits, and action limits

The educational sandbox example is intentionally conservative and demonstrates policy decisions without granting arbitrary host capabilities.
