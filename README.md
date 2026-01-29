# AWS Automation Scripts with Boto3

This repository contains a set of Python scripts built using **Boto3** (AWS SDK for Python) to automate and monitor AWS infrastructure components.  
The focus is on practical cloud and DevOps tasks: automation, monitoring, backups, and cleanup.

The scripts are intentionally simple, readable, and task-focused. No magic, no frameworks, just AWS doing AWS things (sometimes nicely).

---

## Technologies Used

- Python 3
- Boto3
- AWS Services:
  - EC2
  - EBS
  - VPC
  - EKS
  - CloudWatch

---

## Scripts Description

### `add-env-tags.py`
Adds environment tags (e.g. `dev`, `staging`, `prod`) to AWS resources.

**Why it matters**
- Better resource organization
- Cost tracking
- Fewer “who created this?” moments

---

### `cleanup-snapshots.py`
Finds and deletes old or unused EBS snapshots.

**Why it matters**
- Reduces storage costs
- Keeps backups clean
- Prevents your AWS bill from becoming emotionally attached to you

---

### `create-vpc.py`
Creates a custom VPC with basic networking configuration.

**Why it matters**
- Automates network setup
- Ensures consistent infrastructure
- Manual VPC creation is fun exactly once

---

### `ec2-status-checks.py`
Checks the health status of EC2 instances.

**Why it matters**
- Detects failing instances
- Improves monitoring
- Lets you act before users start asking questions

---

### `eks-status-checks.py`
Monitors EKS cluster and node status.

**Why it matters**
- Kubernetes visibility
- Early detection of cluster issues
- Because production clusters enjoy breaking silently

---

### `monitor-website.py`
Monitors a website’s availability and response status.

**Why it matters**
- Simple uptime monitoring
- Early downtime detection
- Knowing first is better than apologizing later

---

### `restore-volume.py`
Restores an EBS volume from an existing snapshot.

**Why it matters**
- Disaster recovery
- Data restoration
- Backups only matter when you can restore them

---

### `volume-backups.py`
Creates backups of EBS volumes.

**Why it matters**
- Automated data protection
- Regular snapshots
- Peace of mind, the rarest AWS service

---

## Prerequisites

- Python 3.8 or higher
- AWS account
- AWS credentials configured locally:

```bash
aws configure
