# Memory Engineering Checklist

- [ ] Memory needs identified from workflow and architecture analysis
- [ ] Each selected memory type has documented business justification
- [ ] No unnecessary memory types added (minimal complexity principle)
- [ ] Retrieval patterns defined for every memory type with performance expectations
- [ ] Persistence strategy addresses durability, availability, and performance requirements
- [ ] Governance rules established: retention, privacy, cleanup, access control
- [ ] Checkpoint strategy defined for workflows with steps exceeding 60 seconds
- [ ] Memory capacity limits and overflow behavior specified
- [ ] Memory interaction patterns documented (how types compose)
- [ ] Compliance requirements fully addressed (if applicable)
