# 30-Day Python Roadmap for AI/ML (Beginner → Advanced)

This roadmap is designed for daily execution with concrete tasks, exercises, and project milestones. If you complete it with consistency, you will build the foundation needed to create production-grade AI/ML systems and start your path toward building autonomous agents.

---

## How to Use This Plan

- **Daily time budget**: 2–4 hours on weekdays, 4–6 hours on weekends.
- **Daily structure**:
  1. Learn (30–60 min)
  2. Build (60–120 min)
  3. Exercise (30–60 min)
  4. Reflect + write notes (15 min)
- **Deliverable every day**: push one commit with today’s work.
- **Weekly output**: one mini-project + one written summary.
- **Tools to install by Day 1**: Python 3.11+, VS Code, Jupyter, Git, GitHub account, uv/pip, virtualenv/conda.

---

## Core Stack You’ll Learn

- **Python fundamentals**: syntax, functions, OOP, testing, packaging.
- **Data stack**: NumPy, pandas, matplotlib/seaborn, SQL basics.
- **ML stack**: scikit-learn, model evaluation, feature engineering.
- **DL stack**: PyTorch, neural networks, optimization, transfer learning.
- **LLM/Agent stack**: APIs, embeddings, RAG, tool-calling, memory, orchestration.
- **MLOps**: experiment tracking, deployment, monitoring, reproducibility.

---

## 30-Day Daily Plan (Tasks + Exercises)

## Week 1 — Python + Math + Data Foundations

### Day 1 — Environment + Python Basics
**Learn**
- Python runtime, virtual environments, pip/uv, project structure.
- Variables, data types, control flow, loops.

**Tasks**
- Create repo: `ai-ml-roadmap-30days`.
- Set up `.venv`, install `jupyter`, `numpy`, `pandas`, `matplotlib`, `pytest`.
- Write `hello_ai.py` with input/output and basic logic.

**Exercises**
1. FizzBuzz (1–100).
2. Prime checker.
3. Temperature converter CLI.

**Output**
- One `README.md` with setup instructions.

---

### Day 2 — Functions, Modules, Error Handling
**Learn**
- Functions, arguments, return values, scope.
- Modules/packages, imports, exceptions.

**Tasks**
- Create utility package: `utils/`.
- Add reusable math/string helper functions.

**Exercises**
1. Build a calculator module with tests.
2. Parse a text file and count word frequencies.
3. Handle invalid inputs gracefully.

**Output**
- `pytest` test suite for helper functions.

---

### Day 3 — Data Structures + Complexity Thinking
**Learn**
- Lists, tuples, dicts, sets, stacks/queues.
- Big-O basics (time/space complexity).

**Tasks**
- Implement common operations from scratch.

**Exercises**
1. Remove duplicates preserving order.
2. Two-sum problem.
3. Group anagrams.

**Output**
- `algorithms_basics.ipynb` with complexity notes.

---

### Day 4 — OOP + Clean Code
**Learn**
- Classes, objects, inheritance, composition.
- Clean code practices, typing hints, docstrings.

**Tasks**
- Model a mini “ML Experiment” class with config, fit, evaluate methods.

**Exercises**
1. Build a `BankAccount` class with tests.
2. Build `DatasetLoader` class with input validation.

**Output**
- Typed Python module using `mypy`-friendly patterns.

---

### Day 5 — NumPy Foundations
**Learn**
- Arrays, vectorization, broadcasting, reshaping.
- Why NumPy is faster than loops.

**Tasks**
- Re-implement simple stats with NumPy only.

**Exercises**
1. Normalize a matrix.
2. Compute cosine similarity function.
3. Implement mini linear regression with NumPy.

**Output**
- Notebook: `numpy_for_ml.ipynb`.

---

### Day 6 — pandas + Data Cleaning
**Learn**
- DataFrames, indexing, filtering, joins, groupby.
- Missing value strategies and categorical encoding basics.

**Tasks**
- Use a public dataset (Titanic/House Prices).
- Perform cleaning and exploratory analysis.

**Exercises**
1. Find top correlations with target.
2. Build 5 meaningful visualizations.
3. Write one-page insight summary.

**Output**
- `eda_report.md` and cleaned CSV.

---

### Day 7 — Math for ML + Weekly Mini-Project
**Learn**
- Linear algebra (vectors, matrices, dot product).
- Intro calculus ideas (gradients intuition).
- Probability basics (mean, variance, distributions).

**Tasks**
- Create formula sheet in your own words.

**Exercises**
1. Compute vector norms and projections manually + NumPy.
2. Implement gradient descent for `y = mx + b`.

**Mini-Project**
- End-to-end notebook: data cleaning + simple regression + interpretation.

---

## Week 2 — Classical Machine Learning Mastery

### Day 8 — ML Workflow Overview
**Learn**
- Problem framing: classification vs regression.
- Train/validation/test split, leakage, baselines.

**Tasks**
- Choose one classification dataset.

**Exercises**
1. Build baseline (majority class / dummy regressor).
2. Compare baseline vs one real model.

---

### Day 9 — Supervised Learning I (Regression)
**Learn**
- Linear regression, regularization (Ridge/Lasso).
- Metrics: MAE, MSE, RMSE, R².

**Tasks**
- Train multiple regression models and compare.

**Exercises**
1. Feature scaling impact test.
2. Residual analysis chart.
3. Error analysis by segment.

---

### Day 10 — Supervised Learning II (Classification)
**Learn**
- Logistic regression, KNN, decision trees.
- Metrics: precision, recall, F1, ROC-AUC.

**Tasks**
- Train at least 3 classifiers.

**Exercises**
1. Confusion matrix deep analysis.
2. Threshold tuning for precision/recall trade-off.

---

### Day 11 — Ensembles
**Learn**
- Random Forest, Gradient Boosting, XGBoost conceptually.

**Tasks**
- Train tree-based models and compare with linear baselines.

**Exercises**
1. Feature importance comparison across models.
2. Interpret one wrong prediction for each model.

---

### Day 12 — Feature Engineering + Pipelines
**Learn**
- One-hot encoding, scaling, imputation pipelines.
- `ColumnTransformer` and `Pipeline` in scikit-learn.

**Tasks**
- Rebuild previous model using a full pipeline.

**Exercises**
1. Add interaction features.
2. Add log transforms for skewed columns.

---

### Day 13 — Validation + Hyperparameter Tuning
**Learn**
- Cross-validation, grid/random search.
- Bias-variance trade-off.

**Tasks**
- Run hyperparameter tuning for top 2 models.

**Exercises**
1. Compare CV score vs holdout score.
2. Plot parameter vs performance.

---

### Day 14 — Week 2 Project (Classical ML App)
**Project**
- Build a complete tabular ML project:
  - EDA
  - preprocessing pipeline
  - model selection + tuning
  - model card (what, data, metrics, limitations)

**Stretch**
- Expose model as FastAPI endpoint.

---

## Week 3 — Deep Learning + NLP + LLM Foundations

### Day 15 — PyTorch Setup + Tensor Basics
**Learn**
- Tensors, autograd, computation graph.

**Tasks**
- Implement linear regression in PyTorch from scratch.

**Exercises**
1. Manual training loop.
2. Compare NumPy vs PyTorch implementation.

---

### Day 16 — Neural Network Basics
**Learn**
- Layers, activations, loss functions, optimizers.

**Tasks**
- Build an MLP for MNIST/Fashion-MNIST.

**Exercises**
1. Experiment with learning rates.
2. Track train vs validation loss.

---

### Day 17 — Training Better Models
**Learn**
- Regularization, dropout, batch norm, early stopping.

**Tasks**
- Improve yesterday’s model with at least 3 techniques.

**Exercises**
1. Build overfitting case then fix it.
2. Plot learning curves.

---

### Day 18 — CNN Basics for Vision
**Learn**
- Convolutions, pooling, feature maps.

**Tasks**
- Build a simple CNN image classifier.

**Exercises**
1. Confusion matrix for classes.
2. Visualize sample feature maps.

---

### Day 19 — NLP Fundamentals
**Learn**
- Tokenization, embeddings, sequence models intuition.
- TF-IDF + classical NLP baseline.

**Tasks**
- Text classification on spam/sentiment dataset.

**Exercises**
1. Compare TF-IDF + logistic regression vs simple neural model.
2. Analyze top informative tokens.

---

### Day 20 — Transformers + LLM Concepts
**Learn**
- Self-attention intuition.
- Prompting basics, temperature, context windows.
- Embeddings and vector similarity.

**Tasks**
- Use an LLM API to summarize/classify text.

**Exercises**
1. Write 5 prompts and compare outputs.
2. Build a simple prompt template library.

---

### Day 21 — Week 3 Project (RAG Prototype)
**Project**
- Build mini RAG pipeline:
  - ingest 20–50 docs
  - chunk + embed
  - vector search
  - prompt LLM with retrieved context

**Exercises**
1. Evaluate answer quality on 10 questions.
2. Add citation output from retrieved chunks.

---

## Week 4 — Agent Engineering + MLOps + Deployment

### Day 22 — Agent Architecture Basics
**Learn**
- Agent loop: plan → act → observe → reflect.
- Tools, memory, retrieval, and orchestration patterns.

**Tasks**
- Implement a simple agent with 2 tools:
  - calculator
  - web/doc retriever

**Exercises**
1. Add tool selection logic.
2. Add guardrails for invalid tool calls.

---

### Day 23 — Function Calling + Structured Outputs
**Learn**
- JSON schema outputs, robust parsing.
- Reliable tool invocation patterns.

**Tasks**
- Convert free-form outputs into typed schemas.

**Exercises**
1. Create 3 tool schemas.
2. Add retry logic for malformed outputs.

---

### Day 24 — Multi-step Reasoning + Memory
**Learn**
- Short-term memory vs long-term memory.
- Reflection and self-correction loops.

**Tasks**
- Add conversation memory and task history to agent.

**Exercises**
1. Implement memory pruning.
2. Add “plan first, then execute” mode.

---

### Day 25 — Evaluation for LLM Apps
**Learn**
- Offline eval sets, faithfulness, relevance.
- Cost/latency/quality trade-offs.

**Tasks**
- Build evaluation harness for your RAG/agent app.

**Exercises**
1. Create 25-question benchmark.
2. Track pass/fail + reasons.

---

### Day 26 — MLOps Essentials
**Learn**
- Experiment tracking (MLflow/W&B concepts).
- Data/version control, reproducibility, model registry.

**Tasks**
- Log experiments for one ML model and one LLM pipeline.

**Exercises**
1. Compare 3 experiment runs.
2. Document the best run + why.

---

### Day 27 — Deployment Day
**Learn**
- FastAPI basics, Docker, environment variables, secrets.

**Tasks**
- Deploy one API endpoint for model/agent.

**Exercises**
1. Add health check endpoint.
2. Add request/response logging.
3. Add simple rate limiting.

---

### Day 28 — Monitoring + Safety
**Learn**
- Monitoring: latency, errors, drift.
- Prompt injection basics, output validation, moderation.

**Tasks**
- Add logging + monitoring dashboard (even simple CSV/SQLite logs).

**Exercises**
1. Simulate failure cases.
2. Add fallback behavior.

---

### Day 29 — Capstone Build Day
**Capstone options**
1. AI study assistant agent.
2. Document Q&A agent with citations.
3. Email triage agent with tool calls.
4. Personal coding copilot for your own repo.

**Requirements**
- User interface (CLI or basic web).
- At least 3 tools.
- RAG + memory.
- Evaluation script.
- Deployment-ready structure.

---

### Day 30 — Finalization + Portfolio + Next 90 Days
**Tasks**
- Polish README, architecture diagram, demo video.
- Write project retrospective:
  - what worked
  - biggest bottlenecks
  - next improvements

**Exercises**
1. Record 5-minute walkthrough.
2. Create a “future roadmap” for 3 months.

**Deliverables**
- Portfolio-ready GitHub repo.
- Deployed demo link.
- Technical write-up.

---

## Daily Practice Template (Use Every Day)

- **Concept revision (15 min)**: rewrite key idea from memory.
- **Coding drill (30 min)**: 1 algorithm/data task.
- **Main build (90+ min)**: roadmap task of the day.
- **Debug challenge (20 min)**: intentionally break and fix code.
- **Learning journal (10 min)**:
  - What I learned
  - What confused me
  - What I’ll improve tomorrow

---

## Beginner → Advanced Progression Milestones

### By Day 7 (Beginner+)
- Comfortable with Python syntax, modules, and NumPy/pandas basics.

### By Day 14 (Intermediate)
- Able to execute full classical ML workflow with proper validation.

### By Day 21 (Intermediate+)
- Can build neural models and a basic RAG prototype.

### By Day 30 (Advanced Practitioner)
- Can design and deploy an AI agent system with tool use, evaluation, and monitoring.

---

## Book List (Python + AI/ML + Agents)

## Python Foundations
1. **Python Crash Course** — Eric Matthes (best beginner practical start).
2. **Fluent Python (2nd Ed.)** — Luciano Ramalho (advanced Python mastery).
3. **Effective Python (2nd Ed.)** — Brett Slatkin (best practices).

## Math + ML Fundamentals
4. **Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow (3rd Ed.)** — Aurélien Géron.
5. **Introduction to Statistical Learning (ISLR, Python edition resources available)** — James et al.
6. **Mathematics for Machine Learning** — Deisenroth, Faisal, Ong.

## Deep Learning
7. **Deep Learning with Python (2nd Ed.)** — François Chollet.
8. **Dive into Deep Learning** — Zhang, Lipton, Li, Smola (free online + code-first).
9. **Understanding Deep Learning** — Prince.

## LLMs, NLP, and Agents
10. **Natural Language Processing with Transformers** — Tunstall, von Werra, Wolf.
11. **Designing Machine Learning Systems** — Chip Huyen.
12. **AI Engineering** — Chip Huyen.
13. **Build a Large Language Model (From Scratch)** — Sebastian Raschka.
14. **Generative AI with LangChain** (practical agent workflows; pick latest edition).

## MLOps + Production
15. **Machine Learning Engineering** — Andriy Burkov.
16. **Building Machine Learning Powered Applications** — Emmanuel Ameisen.
17. **Practical MLOps** — Noah Gift, Alfredo Deza.

---

## Optional Weekly Challenge Track (For Faster Growth)

- **Week 1 Challenge**: solve 20 Python problems on LeetCode/HackerRank.
- **Week 2 Challenge**: Kaggle competition submission (tabular).
- **Week 3 Challenge**: fine-tune a small transformer model.
- **Week 4 Challenge**: deploy capstone and collect real user feedback.

---

## What You Need to Build “Agents Like ChatGPT” in Reality

To build advanced agents in the future, focus on these long-term competencies beyond 30 days:

1. **Strong Python/software engineering** (testing, architecture, APIs).
2. **ML fundamentals** (modeling, metrics, generalization).
3. **LLM application design** (prompting, retrieval, tool-use, memory).
4. **Systems skills** (databases, queues, caching, distributed systems).
5. **MLOps and safety** (monitoring, evals, guardrails, incident response).
6. **Product thinking** (use-case selection, UX, cost/performance trade-offs).

If you continue for 3–6 months after this roadmap with consistent projects, you can realistically build highly capable domain-specific AI agents.
