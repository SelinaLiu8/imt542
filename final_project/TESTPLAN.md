# 🧪 Finance Definition Extractor – Test Plan

## 📌 Purpose

This document outlines the testing strategy for ensuring the quality, accuracy, and performance of the Finance Definition Extractor system. It serves as a living reference to guide development, deployment, and maintenance and to ensure that the system remains reliable for users.

---

## ✅ System Overview

- **Frontend**: React (GitHub Pages hosted)
- **Backend**: Flask API (Azure Web App)
- **Endpoints**:
  - `PUT /input`: Accepts paragraph text
  - `GET /definitions`: Returns structured definitions from Investopedia

---

## 🧪 Test Objectives

- Ensure all key features function as expected
- Verify Investopedia scraping produces correct output
- Confirm response time and stability under realistic and edge-case loads
- Detect and respond to downtime or major functional failure
- Provide clear feedback and traceability in case of error

---

## 🔍 Functional Testing

| Test Case | Description | Method | Expected Result |
|-----------|-------------|--------|-----------------|
| Text Submission | Submit 1–100 words via frontend | UI click + inspect API call | Returns 200 + definitions |
| Empty Input | Submit blank or whitespace | Direct PUT `/input` | 400 error, no crash |
| Single Valid Term | Text: `"liquidity"` | Manual or automated test | Returns correct definition |
| Mixed Valid & Invalid Terms | Text with `"liquidity"`, `"xzyterm"` | Text UI + GET `/definitions` | Valid terms returned, others skipped |
| Definition Fallback | Use a term with no `mntl-sc-block_2-0` but with `short-definition__text_1-0` | Unit test | Definition found via fallback |
| Frontend Error Handling | Kill backend + submit from frontend | Observe behavior | "Failed to fetch definitions" shown |
| CORS Access | Use live GitHub Pages frontend | DevTools Network tab | 200 from Azure API, no CORS errors |

---

## 🚦 Performance Testing

| Test Case | Description | Tool | Target |
|-----------|-------------|------|--------|
| Cold Start | Load backend after idle | Browser or Postman | < 2.5s |
| Normal Load | Submit 5 consecutive paragraphs | Postman | < 2s average |
| Batch Input | Paragraph with 5+ valid terms | GET `/definitions` | < 2s response |
| High Load | Simulate 50 simultaneous users | Locust or Artillery.io | API remains stable |
| Rate Limit | Submit 50+ calls rapidly | Scripted load | 429 (optional), throttling strategy noted |

---

## 📈 Quality Metrics

| Metric | Goal |
|--------|------|
| Accuracy | 100% valid terms return correct definitions |
| Response Time | < 2 seconds for majority of requests |
| API Uptime | 99.9% monthly uptime |
| Frontend Errors | No uncaught exceptions |
| Broken Links | 0 (all Investopedia URLs should resolve) |

---

## ⚠️ Alarms & Monitoring (Planned)

| Alarm | Trigger | Action |
|-------|---------|--------|
| Uptime Ping Failure | No response from backend for 1 min | Alert to dev via email or webhook |
| High Latency | Response time > 5s for 5+ users | Log incident and trigger scale-up |
| 500 Errors Spike | More than 3 in 1 minute | Write to logs + notify maintainer |

Planned tools:
- [UptimeRobot](https://uptimerobot.com/) or [BetterStack](https://betterstack.com/)
- Azure Application Insights (optional)
- GitHub Actions test runner

---

## 🔄 Continuous Testing & Maintenance

- Manual smoke tests on each GitHub push
- GitHub Actions workflow to verify build integrity
- Tests will be expanded to Jest (frontend) + Pytest (backend) in future
- Broken term mapping or scraping issues to be logged and monitored weekly

---

## 📌 Status Summary

| Area | Status |
|------|--------|
| Functional tests | ✅ Implemented (manual + automated) |
| Performance tests | ⚠️ Initial testing complete; scripting planned |
| Alarms/monitoring | 🔜 To be integrated post-MVP |
| Test logging | ✅ Browser console + Flask logs |
| CI/CD validation | ✅ GitHub Actions builds backend on push |

---

## 👥 Team Responsibilities

| Task | Owner |
|------|-------|
| Frontend behavior testing | Selina |
| Backend term/definition accuracy | Dev/analyst lead |
| Deployment checks | Azure monitor + GitHub Actions |
| Weekly QA review | Assigned QA maintainer |

---

## 📦 Future Additions

- Pytest framework for backend endpoint validation
- Frontend Jest tests for component rendering and state flow
- JSON schema validation on returned definition objects
- Error reporting system to notify contributors via GitHub issues

---

