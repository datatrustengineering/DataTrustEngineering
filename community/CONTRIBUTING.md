---
title: Contributing to Data Trust Engineering (DTE)
---

Welcome to the **Data Trust Engineering (DTE)** community! We're building a movement to replace traditional data governance’s 70-80% failure rate [Gartner, 2025] with engineering-driven trust, certification, and AI-readiness. Inspired by the [DataTrustManifesto.org](https://datatrustmanifesto.org)’s agility and collaboration, DTE invites data professionals, enterprises, SMBs, and hyperscalers to contribute to our open-source ecosystem. Whether you're enhancing the [DTE Trust Dashboard](/tools/data-trust-dashboard/DTE_Trust_Dashboard), proposing new artifacts, or sharing case studies, your contributions shape the #DTERevolution.

This guide explains how to contribute to the `DataTrustEngineering` repository, ensuring a productive, inclusive community. Join us at [datatrustmanifesto.org](https://datatrustmanifesto.org) or our [Slack org]([Slack Invite Link]).

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [What Can You Contribute?](#what-can-you-contribute)
- [How to Contribute](#how-to-contribute)
- [Pull Request Process](#pull-request-process)
- [Community Guidelines](#community-guidelines)
- [Recognition](#recognition)
- [Questions or Ideas?](#questions-or-ideas)

## Code of Conduct

All contributors must follow our [CODE_OF_CONDUCT.md](/community/CODE_OF_CONDUCT), based on the Contributor Covenant. Be respectful, constructive, and focused on DTE’s mission to certify data systems by use case, risk, and value. Harassment, off-topic rants, or disruptive behavior will be addressed by maintainers to keep our community welcoming.

## What Can You Contribute?

DTE is a community-driven movement, and we welcome contributions that align with our [Manifesto](/Manifesto) and advance trust, engineering rigor, and AI-readiness. Examples include:

- **Artifacts**: Tools and scripts for data quality (e.g., Great Expectations configs), lineage (e.g., Apache Atlas scripts), or AI governance (e.g., Fairlearn integrations). See `/tools`.
- **Manifesto Updates**: Refine or propose principles in `/Manifesto.md` to strengthen DTE’s vision.
- **Case Studies**: Share real-world DTE applications (e.g., “Reduced AI bias by 15%”) in `/docs/case-studies`. Use our [template](/docs/case-studies/template).
- **Patterns and Guides**: Document DTE best practices (e.g., data quality patterns) in `/docs/patterns`.
- **Trust Dashboard Enhancements**: Add metrics, APIs (e.g., Evidently AI, MLflow), or UI improvements to `/tools/data-trust-dashboard`.
- **Documentation**: Improve clarity, fix typos, or add tutorials in `/docs`.

**Good First Issues**: New to DTE? Start with issues tagged “good first issue” (e.g., typo fixes, adding a case study). These are great for building skills and joining the #DTERevolution!

## How to Contribute

1. **Explore the Repo**:
   - Read the [README.md](/README) and [Manifesto.md](/Manifesto) to understand DTE’s goals.
   - Check `/tools` and `/docs` for existing artifacts and inspiration.

2. **Discuss Your Idea**:
   - Open a GitHub Issue to propose your contribution (e.g., “New artifact: Data quality validator”). Use our issue templates for clarity.
   - Join our [Slack org]([Slack Invite Link]) (#contributions channel) to brainstorm with the community.

3. **Fork and Clone**:
   ```bash
   git clone https://github.com/[YourUsername]/DataTrustEngineering.git
   cd DataTrustEngineering
   ```
   - Fork the repo on GitHub to create your own copy.

4. **Make Changes**:
   - Create a branch: `git checkout -b feature/your-contribution-name`.
   - Add your contribution (e.g., a script in `/tools`, a case study in `/docs/case-studies`).
   - Commit with a clear message: `git commit -m "Add data quality pattern for Great Expectations"`.

5. **Push and Submit a PR**:
   - Push to your fork: `git push origin feature/your-contribution-name`.
   - Open a Pull Request (PR) to the main branch, describing your changes and linking to the relevant issue.

## Pull Request Process

We review PRs to ensure alignment with DTE’s principles (trust, certification, AI-readiness). Follow these steps:

1. **Create a PR**:
   - Use a descriptive title (e.g., “Add lineage tracker script using Apache Atlas”).
   - Link to the related GitHub Issue (e.g., “Closes #123”).
   - Explain your changes and how they advance DTE’s mission.

2. **Review Process**:
   - Maintainers will review within 5-7 days, checking for:
     - Alignment with the [DTE Manifesto](/Manifesto).
     - Code/documentation quality (e.g., markdown linting, functional scripts).
     - Relevance to DTE’s goals (e.g., supports certification, cloud-native architectures).
   - Expect feedback (e.g., “Can you add an example for SMBs?”). Revise as needed.

3. **Automated Checks**:
   - PRs undergo markdown linting (via GitHub Actions) for documentation consistency.
   - Code-based artifacts (e.g., Python scripts) should include basic tests or validation steps.

4. **Approval and Merge**:
   - Approved PRs are merged into the main branch.
   - If a PR doesn’t fit, we’ll provide feedback and close it politely (e.g., “This is great, but it’s outside DTE’s scope of technical trust”).

## Community Guidelines

- **Stay On-Topic**: Contributions should support DTE’s focus on certifying data systems for trust, AI-readiness, and cloud scalability. Off-topic ideas (e.g., unrelated tech policies) may be redirected.
- **Be Collaborative**: Engage in GitHub Discussions or Slack (#contributions) before submitting large PRs to align with community goals.
- **Respect Feedback**: Maintainers may request changes to ensure quality. Respond constructively to keep the #DTERevolution moving forward.
- **Avoid Chaos**: Follow the [CODE_OF_CONDUCT.md](/community/CODE_OF_CONDUCT). Disruptive behavior (e.g., spamming issues) may lead to warnings or blocks.

## Recognition

Your contributions shape DTE! We recognize contributors by:
- Listing you in `CONTRIBUTORS.md` with your permission.
- Highlighting impactful PRs in Slack (#contributions) and X (#DTERevolution).
- Offering roles like “DTE Community Guide” for active contributors, boosting your portfolio.

## Questions or Ideas?

- **GitHub Issues**: Open an issue for questions, ideas, or feedback.
