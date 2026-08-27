# Metrics của MatrAIx và UXAgent

## 1. Sơ đồ cây đầy đủ

```text
Metrics
├── MatrAIx
│   ├── Deterministic / Programmatic Checks
│   │   ├── Objective Final States
│   │   ├── Payloads
│   │   ├── Constraints
│   │   ├── Side Effects
│   │   └── Task-completion Rate
│   │
│   ├── User Experience / Interaction
│   │   ├── Retention Rate
│   │   ├── Purchase Rate
│   │   ├── Satisfaction Rating
│   │   └── Efficiency
│   │       ├── Task Completion Time
│   │       └── Session Duration
│   │
│   ├── Subjective Measures
│   │   ├── Empathy
│   │   ├── Plausibility
│   │   ├── Clarity
│   │   └── Persona Adherence
│   │
│   ├── Controlled Behavioral Adherence
│   │   ├── Politeness
│   │   ├── Humor
│   │   └── Code Comment Style
│   │
│   └── Extraction Quality
│       ├── M1 — Claim Validity
│       ├── M2 — No Over-claiming
│       ├── M3 — Coverage
│       ├── M4 — Internal Consistency
│       └── M5 — Overall Fidelity & Plausibility
│
└── UXAgent
    ├── Standardized Usability Metrics
    │   ├── SUS Score
    │   └── Post-Study Survey
    │       ├── Ease of Use
    │       ├── Usefulness
    │       └── Feature Effectiveness
    │
    ├── Quantitative Interaction Metrics
    │   ├── Total Actions
    │   └── Filter Clicks
    │
    └── Qualitative / Cognitive Metrics
        ├── Action Trace
        │   ├── Clicks
        │   ├── Scrolling
        │   └── Form Submission
        │
        ├── Reasoning Trace
        │   ├── Observations
        │   ├── Planning
        │   ├── Reflections
        │   └── Wonders
        │
        └── Interactive Interviews
            ├── Contextual Feedback
            ├── Memory-based Questions
            └── Point-in-time Evaluation
```

## 2. Bản rút gọn

```text
                    METRICS
                       │
          ┌────────────┴────────────┐
          │                         │
       MatrAIx                   UXAgent
          │                         │
   ┌──────┼──────┬──────┐      ┌────┼────┐
   │      │      │      │      │    │    │
Program  UX   Subjective Behavioral  │  Cognitive
 Checks       Measures  Adherence    │
   │      │      │      │            │
   ├─Final States ├─Retention ├─Politeness
   ├─Payloads     ├─Purchase  ├─Humor
   ├─Constraints  ├─Satisfaction └─Code Style
   ├─Side Effects └─Efficiency
   └─Task Completion

   └─Extraction Quality
      ├─M1 Claim Validity
      ├─M2 No Over-claiming
      ├─M3 Coverage
      ├─M4 Consistency
      └─M5 Fidelity

                              UXAgent
                                │
                  ┌─────────────┼─────────────┐
                  │             │             │
                Usability    Interaction   Cognitive
                  │             │             │
                ├─SUS        ├─Actions     ├─Action Trace
                └─Survey     └─Filter      ├─Reasoning Trace
                                Clicks      └─Interviews
```

## 3. Năm nhóm metric chính

```text
Metrics
├── Task / Goal Success
├── Interaction / Efficiency
├── Usability / Satisfaction
├── Behavioral / Cognitive Quality
└── Fidelity / Consistency
```

### Định hướng của từng hệ thống

- **MatrAIx:** Task Success + Behavioral Adherence + Fidelity
- **UXAgent:** Usability + Interaction + Cognitive Analysis