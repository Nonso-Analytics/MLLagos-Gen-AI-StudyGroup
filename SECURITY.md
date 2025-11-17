# Security Checklist for Third-Party API Integration

When working with external APIs like Google Gemini, OpenAI, or similar services, keeping your keys secure, managing costs, and protecting user privacy aren't just best practices—they're essential. Here's your practical guide to staying safe.

**API Key Management**
Your API key is like your house key. You wouldn't leave it under the doormat, right? Same logic applies here.
DO:

Store keys in environment variables using .env files
Use .env.example files to show required configuration without exposing real keys
Add .env to .gitignore to prevent accidental commits
Rotate keys every 90 days or immediately if you suspect exposure
Use different keys for development, testing, and production
Revoke compromised keys immediately through your provider's dashboard
Use secrets management tools like AWS Secrets Manager or HashiCorp Vault for production

DON'T:

Never hardcode API keys in your source code
Never commit keys to Git—check your history if you're unsure
Never share keys via email or chat (use secure password managers instead)
Never expose keys in client-side code
Never log API keys in application logs
Never use production keys in demos or screenshots

Quick Security Check:
Before committing code, run this to search for potential exposed keys:
bashgit grep -i "api_key\|apikey\|secret\|password" --exclude=*.md
If You Accidentally Expose a Key:

Revoke it immediately in your provider dashboard
Generate a new key and update your environment
Remove it from git history using BFG Repo-Cleaner
Consider it permanently compromised—even if you delete it, assume someone saw it


**Usage Cost Management**
API calls cost money, and those costs can add up fast. Here's how to stay in control.
Monitor & Set Limits:

Set spending limits in your API dashboard (Google AI Studio, OpenAI)
Enable billing alerts at key thresholds (50%, 80%, 100% of budget)
Review usage regularly—daily for production, weekly for development
Implement rate limiting in your application to control API calls
Use cheaper models for testing (gemini-2.5-flash costs less than gemini-pro)
Cache responses when appropriate to avoid duplicate API calls

Application-Level Controls:
python# Set limits per user/session
MAX_REQUESTS_PER_USER = 100  # per day
MAX_TOKENS_PER_REQUEST = 2000

# Implement caching to reduce costs
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_api_call(question):
    return cli.ask(question)
Track Your Spending:

Log API requests (without sensitive data) to monitor patterns
Calculate cost per request based on token usage
Project monthly costs from current trends
Use free tiers for development and testing


**Privacy & Data Protection**
What you send to third-party APIs matters. Once data leaves your application, you lose control over it.
What Gets Sent to APIs:
Remember:

All prompts and responses are processed by the API provider
Providers may use your data to improve their models
Data may be stored temporarily or permanently
Data may cross international borders

User Data Guidelines:

Minimize data collection—only send what's necessary
Sanitize inputs before sending to external services
Never send PII (Personally Identifiable Information) unless absolutely required
Inform users that their data is processed by third parties
Comply with regulations—GDPR, CCPA, HIPAA based on your location
Review the API provider's privacy policy and terms of service

Data Classification Guide:
SAFE to send:

General knowledge questions
Public information
Anonymized data
Synthetic test data

NEVER send:

Passwords or credentials
Credit card numbers
Social security numbers
Health records
Private communications
Proprietary business information
Any regulated or confidential data

Example: Input Sanitization
pythondef sanitize_input(question: str) -> str:
    """Remove potential PII patterns before API call"""
    import re
    # Remove email addresses
    question = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 
                      '[EMAIL]', question)
    # Remove phone numbers
    question = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE]', question)
    # Remove credit card patterns
    question = re.sub(r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b', 
                      '[CARD]', question)
    return question
User Consent Best Practices:

Display clear privacy notices
Get explicit consent for data processing
Provide opt-out mechanisms
Allow users to request data deletion