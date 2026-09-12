# Release Verification

Before release:

- [ ] README renders and banner path is `assets/agenticai-banner.png`
- [ ] all 14 curriculum modules exist
- [ ] all six learning pathways exist
- [ ] ten case studies exist
- [ ] ten projects exist
- [ ] examples run without external credentials
- [ ] tests pass
- [ ] imports work
- [ ] relative links pass the checker
- [ ] no `.env` or secrets are committed
- [ ] Docker runs as unprivileged, read-only, no-network by default
- [ ] no arbitrary generated code is executed on the host
- [ ] Mermaid fences are balanced and diagrams use supported syntax
- [ ] CI YAML parses
- [ ] beginner and advanced pathways are internally consistent
- [ ] `git diff` and repository tree contain only intended files
