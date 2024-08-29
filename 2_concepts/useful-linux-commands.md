---
status: backlog
---

# Useful Linux Commands

- checks all mounted drives that are larger than 1GB and are not temporary file systems (`tmpfs`)

```bash
df -H | awk 'NR==1 || ($1 !~ /tmpfs/ && (($2 ~ /G$/ && $2+0 > 1) || ($2 ~ /T$/ && $2+0 >= 1)))'
```
