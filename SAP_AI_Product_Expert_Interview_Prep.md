# SAP AI Product Expert — Interview Preparation

## What to Expect

- **Two business case scenarios** presented in sequence
- **Interactive format** — ask clarifying questions freely; this is expected and rewarded
- Evaluators are assessing: structured thinking, problem framing, and communication of reasoning
- No single "right answer" — approach and process matter more than conclusions

---

## Core Framework for Any Business Case

Use this sequence to structure your response:

1. **Clarify** — Ask 2–3 scoping questions before diving in
2. **Frame** — Restate the problem in your own words; define success
3. **Structure** — Break the problem into components (use a framework)
4. **Analyse** — Work through each component with data/logic
5. **Recommend** — Give a clear, prioritised recommendation
6. **Acknowledge trade-offs** — Show you've considered risks and alternatives

---

## SAP-Specific Context You Should Know

### SAP's AI Strategy
- **SAP Business AI** is the umbrella brand; embedded AI across all SAP products
- **Joule** is SAP's generative AI copilot — integrated into S/4HANA, SuccessFactors, Ariba, etc.
- SAP differentiates on **business context**: AI trained on SAP's data models and business processes, not generic LLMs
- Key partnerships: Microsoft (Azure OpenAI), Google Cloud, AWS for underlying model infrastructure
- SAP uses the term **"relevant, reliable, responsible AI"** as its guiding principle

### SAP's Core Product Areas (AI is being embedded across all of these)
| Product | Domain |
|---|---|
| S/4HANA | ERP — Finance, Supply Chain, Manufacturing |
| SuccessFactors | Human Experience Management (HXM) |
| Ariba | Procurement & Spend Management |
| Concur | Travel & Expense |
| Customer Experience (CX) | Sales, Service, Commerce, Marketing |
| BTP (Business Technology Platform) | Integration, extension, AI/ML services |

### Key SAP AI Use Cases
- **Finance**: Automated invoice processing, anomaly detection, cash flow forecasting
- **HR**: Candidate matching, skills gap analysis, attrition prediction
- **Supply Chain**: Demand forecasting, disruption prediction, inventory optimisation
- **Procurement**: Supplier risk scoring, spend analytics, contract intelligence
- **Customer Service**: Ticket classification, resolution suggestion, sentiment analysis

---

## Likely Business Case Themes

### Theme 1: AI Feature Prioritisation / Product Roadmap
**Example prompt**: *"SAP wants to add AI capabilities to SuccessFactors. How would you prioritise which features to build first?"*

**Approach**:
- Clarify: target customer segment (SME vs. enterprise), time horizon, existing capabilities
- Framework: Value vs. Effort matrix + strategic fit
- Dimensions to evaluate: user pain severity, data availability, differentiation vs. competitors (Workday, Oracle HCM), regulatory sensitivity (especially in HR)
- Recommend: Start with high-value, lower-risk wins (e.g., job description generation) before high-sensitivity use cases (e.g., performance scoring)

**Key point to raise**: AI in HR requires extra care — bias, explainability, GDPR, and employee trust are all live issues.

---

### Theme 2: AI Adoption / Change Management
**Example prompt**: *"A large enterprise customer is struggling to adopt the AI features in S/4HANA. What would you do?"*

**Approach**:
- Clarify: Which features? What does "struggling" mean — awareness, usage, value realisation?
- Root causes to consider: user trust, workflow integration, training gaps, data quality, IT/governance friction
- Framework: People / Process / Technology
- Actions: Persona-specific training, quick-win use case selection, executive sponsorship, feedback loops
- Metrics: Feature adoption rate, time-to-value, user NPS

---

### Theme 3: Build vs. Buy vs. Partner
**Example prompt**: *"SAP is deciding whether to build its own foundation model or continue partnering with OpenAI/Microsoft. How would you think through this?"*

**Approach**:
- Clarify: time horizon, investment appetite, strategic intent (differentiation vs. cost)
- Framework: Core vs. Context — is the model itself the differentiator, or is it the business data/context?
- SAP's actual position: SAP's moat is **business process knowledge and data**, not model weights — partnership makes sense for general LLM capability; SAP fine-tunes/grounds on proprietary data
- Risk factors for building: talent, cost, speed-to-market, commoditisation of models
- Recommend: Hybrid — partner for foundational model, invest in fine-tuning + RAG on SAP business data + proprietary workflow integration

---

### Theme 4: New AI Product / Market Entry
**Example prompt**: *"A mid-market manufacturing company asks SAP to build an AI tool to reduce production downtime. How would you approach this as a product?"*

**Approach**:
- Clarify: What's the current downtime cause? What data exists (IoT sensors, maintenance logs)? What's the budget/timeline?
- Problem decomposition: Predictive maintenance vs. real-time anomaly detection vs. root cause analysis
- Data requirements: sensor data, maintenance history, failure labels
- MVP definition: Start with anomaly alerting, then add prediction, then prescription
- Integration: How does it sit within SAP's existing Asset Management / Plant Maintenance modules?
- Go-to-market: Packaged in BTP or embedded in S/4HANA Manufacturing

---

### Theme 5: AI Ethics / Responsible AI
**Example prompt**: *"SAP's HR AI product is flagged for potential bias in candidate screening. What do you do?"*

**Approach**:
- Immediate: Pause the feature, communicate transparently with affected customers
- Investigation: Audit training data, model outputs by demographic group, review feature inputs
- Remediation: Bias mitigation techniques, human-in-the-loop for high-stakes decisions
- Policy: Align to SAP's Responsible AI principles, EU AI Act (HR AI is likely "high-risk" under the Act)
- Prevention: Establish ongoing monitoring, diverse training data curation, third-party audits

---

## Useful Frameworks to Have Ready

| Framework | When to Use |
|---|---|
| Value vs. Effort (2x2) | Feature prioritisation |
| RICE (Reach, Impact, Confidence, Effort) | Roadmap scoring |
| Jobs-to-be-Done | Understanding user needs |
| People / Process / Technology | Adoption and change management |
| Build / Buy / Partner | Make-or-buy decisions |
| MECE issue tree | Structuring any ambiguous problem |
| North Star Metric + guardrail metrics | Defining product success |

---

## Questions to Ask Your Interviewers

Asking smart questions signals curiosity and business acumen:

1. *"What does success look like for this role in the first 90 days?"*
2. *"How does the AI product team interact with SAP's core engineering and go-to-market teams?"*
3. *"Where is SAP seeing the strongest customer pull for Joule today — which product lines or geographies?"*
4. *"How is SAP balancing speed of AI feature delivery with responsible AI requirements, particularly under the EU AI Act?"*
5. *"What does the competitive landscape look like from SAP's perspective — is the bigger threat from Oracle/Workday or from pure-play AI startups?"*

---

## On the Day: Communication Tips

- **Think out loud** — narrate your reasoning as you go; silence makes it hard to assess your thinking
- **Clarify before solving** — spend 1–2 minutes asking scoping questions; it shows structured thinking
- **Use signposting**: *"I'd like to break this into three parts…"* / *"My recommendation is X, for three reasons…"*
- **Be comfortable with ambiguity** — say *"I'd want to validate this assumption, but working with what we have…"*
- **Quantify where possible** — even rough estimates demonstrate commercial thinking
- **End with a clear recommendation** — don't leave things open-ended

---

## Quick SAP Vocabulary

| Term | Meaning |
|---|---|
| Joule | SAP's generative AI copilot |
| BTP | Business Technology Platform — SAP's cloud platform for extensions and integrations |
| S/4HANA | SAP's flagship ERP (successor to SAP ECC) |
| RISE with SAP | SAP's cloud transformation offering |
| GROW with SAP | Cloud ERP offering for mid-market |
| Clean Core | SAP's principle of keeping the ERP core standard, extending via BTP |
| Business AI | SAP's brand for all embedded AI capabilities |

---

Good luck tomorrow — you've got this.
