# Frameworks for Security Engineer

This file provides detailed definitions and application guidance for the frameworks used in this prompt.

---

### OWASP Top 10 (2021) Mitigation

**A01 - Broken Access Control**:
```python
# Secure access control implementation
@require_permission('read_sensitive_data')
@validate_resource_ownership
def get_user_data(user_id, requesting_user):
    if requesting_user.id != user_id and not requesting_user.has_admin_role():
        raise PermissionDenied("Access denied")
    
    return UserRepository.get_by_id(user_id)
```

**A03 - Injection**:
```python
# SQL injection prevention
def get_user_by_email(email):
    # Use parameterized queries
    query = "SELECT * FROM users WHERE email = %s"
    return db.execute(query, (email,))

# NoSQL injection prevention
def find_user(user_input):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', user_input):
        raise ValueError("Invalid email format")
    
    return db.users.find_one({"email": user_input})
```

### Zero Trust Implementation

```python
# Zero Trust access evaluation
class ZeroTrustPolicy:
    def evaluate_access_request(self, user, resource, context):
        score = 0
        
        # Identity verification
        if self.verify_strong_authentication(user):
            score += 30
        
        # Device trust
        if self.is_managed_device(context.device):
            score += 25
        
        # Location analysis
        if self.is_trusted_location(context.location):
            score += 20
        
        # Behavioral analysis
        if self.analyze_user_behavior(user, context):
            score += 25
        
        # Determine access decision
        if score >= 80:
            return AccessDecision.ALLOW
        elif score >= 60:
            return AccessDecision.ALLOW_WITH_MFA
        else:
            return AccessDecision.DENY
```

### Threat Intelligence Integration

```python
# Threat intelligence feeds integration
class ThreatIntelligence:
    def __init__(self):
        self.feeds = [
            {'name': 'MISP', 'url': 'https://misp.local/attributes'},
            {'name': 'VirusTotal', 'api_key': 'vt_api_key'},
            {'name': 'AlienVault', 'api_key': 'otx_api_key'}
        ]
    
    def enrich_indicator(self, indicator):
        enrichment_data = {}
        
        for feed in self.feeds:
            try:
                data = self.query_feed(feed, indicator)
                enrichment_data[feed['name']] = data
            except Exception as e:
                logging.error(f"Failed to query {feed['name']}: {e}")
        
        return enrichment_data
    
    def check_ioc_reputation(self, ioc):
        # Check multiple threat intelligence sources
        reputation_score = 0
        sources_checked = 0
        
        for feed in self.feeds:
            result = self.query_reputation(feed, ioc)
            if result:
                reputation_score += result.score
                sources_checked += 1
        
        if sources_checked > 0:
            return reputation_score / sources_checked
        return 0
```

---

---

## Framework Integration Strategies

### Sequential Integration
Frameworks are applied one after another in different stages.

**When to use**: When frameworks build on each other logically.

### Parallel Integration
Multiple frameworks are used simultaneously within the same stage.

**When to use**: When frameworks provide complementary perspectives.

### Selective Integration
User chooses which frameworks to apply based on their specific situation.

**When to use**: When different scenarios require different analytical approaches.

---

## Best Practices

1. **Start Simple**: Don't overwhelm with too many frameworks initially
2. **Explain Why**: Always clarify the purpose and value of each framework
3. **Provide Examples**: Show how frameworks have been applied in similar scenarios
4. **Allow Flexibility**: Let users adapt frameworks to their specific needs
5. **Integrate Naturally**: Frameworks should enhance dialogue, not dominate it

---

## Version Information

- **Version**: 1.0.0
- **Last Updated**: 2025-11-24
- **Related Files**: 
  - Main Prompt: `prompts/copilot/prompts/design-development/security-engineer.md`
  - Examples: `rag/design-development/security-engineer/examples.md`
  - Methodologies: `rag/design-development/security-engineer/methodologies.md`
