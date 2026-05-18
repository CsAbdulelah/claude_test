# SAP AI Product Expert — Model Case Answers

> These are written as spoken responses, the way you'd actually deliver them in the room.
> Each answer follows the sequence: **Clarify → Frame → Structure → Analyse → Recommend → Trade-offs**

---

## Case 1: AI Feature Prioritisation

### The Prompt
*"SAP is considering adding new AI capabilities to SuccessFactors. How would you decide which features to build first?"*

---

### Step 1 — Clarifying Questions (say these first)

> "Before I dive in, I'd like to clarify a few things to make sure I'm solving the right problem.
>
> First — are we talking about net-new AI features, or enhancing AI capabilities that already exist in SuccessFactors today?
>
> Second — what's the primary customer segment we're optimising for: large enterprise, or the mid-market where SAP is growing with GROW with SAP?
>
> And third — do we have a rough sense of the investment envelope and time horizon — are we planning a 12-month roadmap, or something longer term?
>
> [Wait for answers, then proceed]
>
> Great. I'll assume we're looking at net-new features, primarily for enterprise customers, with a 12-month planning horizon. Let me know if I should adjust any of those."

---

### Step 2 — Frame the Problem

> "The core challenge here is prioritisation under constraints. SuccessFactors covers a wide surface — recruiting, onboarding, performance, learning, compensation, workforce planning. AI could add value in all of those areas, but we can't build everything at once.
>
> I'd define success as: shipping AI features that drive measurable adoption and customer value within 12 months, while strengthening SAP's competitive position against Workday and Oracle HCM."

---

### Step 3 — Structure

> "I'd evaluate potential features across four dimensions:
>
> 1. **User pain severity** — how significant is the problem this feature solves for HR professionals and employees?
> 2. **Data readiness** — does SAP have the data needed to build this reliably? Poor data quality is the most common reason AI features fail in enterprise settings.
> 3. **Competitive differentiation** — does this deepen SAP's moat, or is it table stakes that Workday already has?
> 4. **Risk profile** — particularly important in HR, where AI bias, GDPR, and employee trust are live concerns.
>
> I'd score each candidate feature across these four dimensions and map them on a value-vs-risk matrix."

---

### Step 4 — Analysis: Applying the Framework

> "Let me walk through a few example features to show how this plays out.
>
> **Job Description Generation (Joule-powered)** — High pain (writing JDs is time-consuming and inconsistently done), data is readily available (SAP has job architecture and skills taxonomy data), low risk (generative output reviewed by a human), and differentiated because it's embedded directly in the SuccessFactors workflow rather than a standalone tool. **High priority.**
>
> **AI-Powered Skills Inference** — This is where SAP has a genuine moat. SAP has millions of employee records and can infer skills from job history, learning completions, and performance data. High strategic value for workforce planning. Medium complexity. Risk is explainability — employees need to understand how their skills profile is built. **High priority, with transparency requirements built in.**
>
> **Automated Performance Rating** — High pain, but very high risk. Using AI to generate or influence performance scores touches compensation and career progression. Under the EU AI Act, this likely qualifies as a high-risk AI system. Employees and works councils will push back. **Deprioritise or position only as a decision-support tool with full human override.**
>
> **Attrition Prediction** — Moderate pain, good data availability, but also sensitive. If a manager can see that an employee has an 80% attrition probability, what do they do with that? Risk of discriminatory action. **Medium priority — scope carefully with guardrails.**"

---

### Step 5 — Recommendation

> "My recommendation would be to organise the roadmap into three tiers:
>
> **Tier 1 — Build now (0–6 months):** Features with high value, high data readiness, and low risk. Job description generation, interview question suggestions, onboarding task automation. These build user trust in the AI and drive adoption.
>
> **Tier 2 — Build with guardrails (6–12 months):** Skills inference and talent matching — high value, but requires explainability features and HR admin oversight to be built alongside the AI capability.
>
> **Tier 3 — Defer or pilot only:** Automated performance scoring, pay equity recommendations. High value long-term, but requires regulatory clarity and customer trust to be established first.
>
> This approach lets us ship meaningful AI value quickly while not creating liability or trust issues that could damage the product's reputation."

---

### Trade-offs to Acknowledge

> "The trade-off here is speed vs. safety. Focusing on lower-risk features first means we're not addressing some of the highest-pain problems immediately. The counter-argument is that one high-profile AI bias incident in HR could set back adoption across the entire product — so the conservative sequencing is actually the commercially rational choice."

---

---

## Case 2: AI Adoption / Change Management

### The Prompt
*"A large enterprise customer has rolled out SAP S/4HANA with the embedded AI features, but six months in, nobody is using them. What do you do?"*

---

### Step 1 — Clarifying Questions

> "A few quick questions to help me frame this well.
>
> When you say nobody is using the AI features — do we have any data on this? Are we seeing zero feature activations in telemetry, or is this anecdotal from the account team?
>
> Which AI features specifically are we talking about — is this broad (Joule, intelligent automation across the board) or concentrated in a specific area like finance or procurement?
>
> And what do we know about why they bought this — was AI a stated priority in the deal, or was it bundled in and not really part of their use case?
>
> [After answers]
>
> Good. I'll work with the assumption that telemetry confirms very low usage across most AI features, and that AI was part of the pitch but not deeply tied to specific business outcomes the customer committed to."

---

### Step 2 — Frame

> "This is fundamentally an adoption problem, not a product problem. The features exist and presumably work — but they haven't been connected to the customer's day-to-day workflows, priorities, or user motivations. The risk is churn at renewal and a negative reference account.
>
> Success here means getting to meaningful, measurable AI usage within 90 days — and ideally turning this customer into a reference case."

---

### Step 3 — Structure (People / Process / Technology)

> "I'd diagnose adoption failures through three lenses: People, Process, and Technology.
>
> **People** — Do users know the features exist? Do they trust them? Are there change management or training gaps?
>
> **Process** — Are the AI features integrated into how people actually work, or do they require users to go out of their way to use them?
>
> **Technology** — Are there configuration or data quality issues causing the features to produce poor outputs, which led users to abandon them early?"

---

### Step 4 — Analysis

> "Starting with People: In large enterprises, AI rollout often stops at the IT team. The business users — the AP clerks, the HR BPs, the procurement managers — may have had one training session at go-live and nothing since. They default to what they know. I'd want to audit what training happened and whether it was role-specific or generic.
>
> On Process: The most common failure mode I've seen is that AI features are positioned as 'also available' rather than embedded in the workflow. If Joule requires a separate login or a context switch, it won't get used. I'd map the top three user journeys for this customer and check whether the AI touchpoint is on the critical path or a detour.
>
> On Technology: If users tried the AI features early and got poor outputs — wrong invoice matches, irrelevant suggestions — they'll have learned to ignore it. I'd pull the early feedback data and check if there were data quality issues at go-live that may since have been resolved but the reputation hasn't recovered."

---

### Step 5 — Recommendation (90-day plan)

> "I'd recommend a focused 90-day adoption sprint structured as follows:
>
> **Weeks 1–2 — Diagnose:** Run a structured discovery with the customer's IT lead, HR/Finance lead, and 5–6 end users. Identify the top two or three use cases where the AI could have the most visible impact. Don't try to fix everything at once.
>
> **Weeks 3–6 — Quick win sprint:** Pick one high-impact use case — say, automated invoice exception handling in finance — and do a white-glove activation: configure it properly, train the relevant users specifically, and set a target metric (e.g., reduce manual exceptions by 30%).
>
> **Weeks 7–10 — Expand:** Use the quick win as social proof internally. Run lunch-and-learns. Get a sponsor in the business (not IT) to champion it. Track and communicate the results.
>
> **Weeks 11–12 — Lock in:** Package the results into a business case for the customer's executive sponsor. Tie AI adoption to their renewal conversation and set targets for the next 6 months.
>
> The goal is to make the AI indispensable to at least one team before trying to scale broadly."

---

### Trade-offs

> "The main tension is between doing this right and doing it fast. A thorough diagnosis takes time, and the account team may want a quick fix. But rushing to push more features without understanding the root cause will just repeat the failure. I'd push for the full diagnostic — it's a 2-week investment that de-risks everything that follows."

---

---

## Case 3: Build vs. Buy vs. Partner

### The Prompt
*"SAP's CEO is asking whether SAP should build its own foundation model or continue partnering with providers like Microsoft/OpenAI and Google. How would you advise?"*

---

### Step 1 — Clarifying Questions

> "This is a big strategic decision, so I want to make sure I'm framing it at the right level.
>
> Are we talking about a general-purpose foundation model, or a domain-specific model trained on SAP business data?
>
> What's the investment appetite — are we talking about a multi-billion-dollar commitment to compete with GPT-5, or a more targeted investment?
>
> And what's the primary driver of this question — is it concern about cost at scale, about differentiation, about data privacy for customers, or about dependency risk?
>
> [After answers]
>
> Good. I'll assume we're asking whether to build a general-purpose LLM to underpin Joule, the investment appetite is significant but not unlimited, and the primary drivers are differentiation and data control."

---

### Step 2 — Frame

> "The core question is: where does SAP's competitive advantage actually live?
>
> If the answer is 'in the model weights themselves,' then building makes sense. If the answer is 'in the business process knowledge, the data, and the workflow integration,' then the model is infrastructure — and you don't build your own electricity grid.
>
> My hypothesis is that SAP's moat is the latter, and I'll work through the logic."

---

### Step 3 — Structure

> "I'd analyse this across four dimensions:
>
> 1. **Differentiation** — Does owning the model create a meaningful competitive advantage?
> 2. **Economics** — What does it cost to build vs. partner, at SAP's scale?
> 3. **Speed** — How does each option affect time-to-market?
> 4. **Risk** — What are the failure modes of each path?"

---

### Step 4 — Analysis

> "**On differentiation:** Foundation model capabilities — reasoning, language understanding, code generation — are rapidly commoditising. GPT-4-level capability will be table stakes within 18 months. The differentiation in enterprise AI is not the model; it's the *context* the model has access to. SAP's advantage is that it holds the business data — the financial transactions, the org structures, the procurement records. A model grounded in that data, with deep knowledge of SAP's data schema and business processes, is genuinely differentiated. That's a fine-tuning and RAG problem, not a foundation model problem.
>
> **On economics:** Training a frontier model costs hundreds of millions of dollars and requires massive GPU clusters and an ML research team that SAP doesn't currently have at that scale. Meanwhile, OpenAI, Google, and Mistral are competing aggressively on API pricing. SAP gets frontier capability at a fraction of the cost by partnering. The build option makes sense if you expect to run inference at such massive scale that the per-token cost of APIs becomes prohibitive — possible, but SAP is not there yet.
>
> **On speed:** Building a frontier model from scratch is a 3–5 year effort at minimum. Every month spent on that is a month Joule isn't improving. Partnering lets SAP focus engineering resources on what actually moves the needle for customers: better workflow integration, better grounding on SAP data, better UX.
>
> **On risk:** The dependency risk of partnering is real — pricing changes, API deprecations, data residency concerns. But this can be managed with a multi-provider strategy (SAP already works with Microsoft, Google, and Mistral). The build risk is equally real: a multi-year, multi-billion investment that may produce a model that's already behind the frontier by the time it ships."

---

### Step 5 — Recommendation

> "My recommendation is: **do not build a general-purpose foundation model. Double down on the proprietary layer.**
>
> Specifically:
>
> 1. **Maintain a multi-provider model strategy** — Microsoft/Azure OpenAI as the primary partner, with Google and open-source (Mistral, Llama) as fallbacks and for specific use cases. This eliminates single-vendor dependency.
>
> 2. **Invest heavily in domain-specific fine-tuning** — Train models on SAP's anonymised transaction data, business process documentation, and support logs. This is where the differentiation lives.
>
> 3. **Build proprietary RAG infrastructure** — The ability to ground Joule in a customer's specific SAP instance in real time is a genuine moat. Invest in the retrieval, context management, and grounding layer.
>
> 4. **Acquire or build a small AI lab focused on business AI research** — Not to compete with OpenAI, but to have the capability to evaluate models, fine-tune, and contribute to the open-source ecosystem (which improves recruitment and credibility).
>
> This gives SAP the benefits of frontier models without the cost and risk of building one, while investing in the layers where SAP can genuinely differentiate."

---

### Trade-offs

> "The risk I'm not dismissing is strategic dependency. If in five years, one provider dominates and raises prices dramatically, SAP is exposed. The multi-provider strategy partially mitigates this, but it's worth revisiting if the market consolidates further. The counter to building remains: by the time a SAP-built model is competitive, the open-source models (Llama, Mistral) will likely be good enough to underpin enterprise use cases anyway — so the dependency risk may resolve itself without SAP needing to build."

---

---

## Case 4: New AI Product for a Customer

### The Prompt
*"A large automotive manufacturer — an SAP customer running S/4HANA — comes to you. They're losing €2M per month to unplanned production downtime. They want SAP to help them solve it with AI. How do you approach this as a product problem?"*

---

### Step 1 — Clarifying Questions

> "This is a great use case — let me ask a few questions before I propose anything.
>
> First, do we know what's causing the downtime? Is it primarily equipment failure, supply chain disruptions (missing parts), or human/process errors?
>
> Second, what data do they already have — are there IoT sensors on the production equipment, and do they have historical maintenance logs with failure records?
>
> Third, are they looking for us to build something custom, or would this be a packaged capability within SAP's existing Asset Management or Plant Maintenance modules in S/4HANA?
>
> And finally — what's the timeline expectation? A quick pilot, or a full production deployment?
>
> [After answers]
>
> Good. I'll assume the primary cause is equipment failure, they have IoT sensor data plus 3+ years of maintenance history, they'd prefer something embedded in S/4HANA rather than a standalone tool, and they want to see a pilot result within 6 months."

---

### Step 2 — Frame

> "The customer's goal is to reduce unplanned downtime — €2M per month is a significant number, and even a 30% reduction is €7.2M annually. That's a compelling business case for an AI investment.
>
> The product challenge is: how do we turn raw sensor and maintenance data into actionable predictions that maintenance teams will actually trust and act on?
>
> I'd approach this as three sequential problems: detect, predict, and prescribe."

---

### Step 3 — Structure (Detect → Predict → Prescribe)

> "**Detect** — Identify anomalies in real-time sensor data that indicate a machine is behaving abnormally. This is the foundation; without reliable anomaly detection, prediction is meaningless.
>
> **Predict** — Using historical failure patterns and current sensor readings, estimate the probability and time horizon of a failure for each asset. This is what enables planned intervention before the failure occurs.
>
> **Prescribe** — Recommend the specific maintenance action: which technician should do what, which parts to order, and the optimal time to schedule the maintenance window to minimise production impact.
>
> For a 6-month pilot, I'd focus on Detect and Predict. Prescribe requires more complex integration with spare parts inventory (Ariba) and workforce scheduling — I'd scope that for phase two."

---

### Step 4 — Analysis

> "**On data:** The foundation of this is data quality. I'd run a data readiness assessment in the first 4 weeks: do the sensors capture the right signals? Are the maintenance logs structured enough to extract failure labels? Are failure events correctly timestamped relative to sensor readings? In my experience, this is where most predictive maintenance projects get delayed — the data exists but isn't clean enough to train on.
>
> **On the model:** For anomaly detection, unsupervised approaches (autoencoders, isolation forests) work well when labelled failure data is scarce. For failure prediction, if we have 3+ years of labelled data, a gradient boosting model (XGBoost) with sensor time-series features is typically robust and explainable enough for maintenance engineers to trust. Explainability matters — if a technician gets an alert saying 'Machine 7 will fail in 48 hours,' they need to see *why* (e.g., 'vibration frequency has been trending up for 6 days').
>
> **On integration:** This needs to live inside the S/4HANA Plant Maintenance module, not a separate dashboard. If maintenance teams have to open a different tool to see AI predictions, they won't. The alert needs to appear in their existing workflow — creating a maintenance order automatically when confidence exceeds a threshold.
>
> **On trust and adoption:** Predictive maintenance AI often fails not because the model is wrong, but because maintenance teams don't trust it. I'd recommend a 'shadow mode' period in the pilot — the model makes predictions, the team sees them but acts on their own judgment, and we track whether the model was right. After 6–8 weeks of shadow mode with good accuracy, teams typically start acting on the predictions."

---

### Step 5 — Recommendation

> "My recommended approach:
>
> **Phase 1 — Pilot (0–6 months):** Focus on 2–3 critical production lines. Run a 4-week data readiness assessment. Build an anomaly detection and failure prediction model. Deploy in shadow mode for 6–8 weeks to build trust. Measure: model accuracy (precision/recall on failure prediction), and whether predicted maintenance events would have prevented actual downtime incidents.
>
> **Phase 2 — Scale and Prescribe (6–18 months):** If pilot KPIs are met, expand to all production lines. Add prescriptive recommendations — integrate with Ariba for parts ordering, SuccessFactors for technician scheduling. Build a feedback loop so technicians' actions and outcomes continuously improve the model.
>
> **Packaging:** Position this as an extension of SAP's existing Predictive Asset Insights product, delivered via BTP and embedded in S/4HANA — not a custom build. This means it's maintainable, upgradeable, and can be packaged for other automotive and manufacturing customers. The €2M/month problem at this one customer is almost certainly shared by dozens of other SAP manufacturing accounts.
>
> **Success metric:** 25–30% reduction in unplanned downtime within 12 months of full deployment. At €2M/month baseline, that's €6–7M annual value — strong ROI even at significant implementation cost."

---

### Trade-offs

> "The main trade-off is customisation vs. reusability. The customer will want something deeply tailored to their specific machines and processes — but if we over-customise, we build a one-off solution SAP can't sell to anyone else. The right balance is a configurable product with strong default models and the ability to fine-tune on customer-specific data. I'd push back on any request for custom model architectures — the value is in the data and the integration, not in inventing new ML approaches."

---

---

## Cross-Case Reminders

- **Always clarify before solving.** Two minutes of scoping questions saves you from solving the wrong problem.
- **Signpost your structure.** Say "I'll break this into three parts" before you start — it signals organised thinking.
- **Quantify wherever possible.** "30% reduction" is more credible than "significant reduction."
- **End with a clear recommendation.** Don't leave the answer open-ended — take a position, then acknowledge the trade-offs.
- **Relate back to SAP's context.** Show you understand where SAP's moat lies: business process depth, data, workflow integration — not generic AI.
