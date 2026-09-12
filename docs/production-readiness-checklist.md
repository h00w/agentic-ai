# Production Readiness Checklist

- [ ] API contracts and schemas are versioned
- [ ] state model and idempotency strategy documented
- [ ] retries use bounded exponential backoff where appropriate
- [ ] timeouts and circuit breakers exist for dependencies
- [ ] fallbacks and degraded modes are tested
- [ ] step/token/cost/rate/concurrency budgets are enforced
- [ ] secrets are externalized
- [ ] tool permissions are explicit and least-privileged
- [ ] golden evaluation suite passes release thresholds
- [ ] safety tests pass
- [ ] traces, metrics and logs provide incident evidence
- [ ] health checks, alerts and on-call ownership exist
- [ ] rollback is tested
- [ ] privacy/governance approvals are complete
