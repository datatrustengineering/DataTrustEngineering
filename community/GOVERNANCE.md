---
title: Governance
---

# Governance of Data Trust Engineering (DTE)

The **Data Trust Engineering (DTE)** project is a community-driven movement to replace traditional data governance’s 70-80% failure rate [Gartner, 2025] with engineering-driven trust, certification, and AI-readiness, as outlined in the [Data Trust Engineering Manifesto](/Manifesto.md). Inspired by the [DataOps Manifesto](https://dataopsmanifesto.org)’s principles of collaboration and agility, DTE evolves through open-source contributions on GitHub, starting with artifacts like the [DTE Trust Dashboard](/tools/data-trust-dashboard/DTE_Trust_Dashboard.html). This `GOVERNANCE.md` file defines how our community makes decisions, manages contributions, and resolves conflicts to ensure a transparent, inclusive, and productive #DTERevolution.

Learn more at [datatrustmanifesto.org](https://datatrustmanifesto.org) or join our [Slack org]([Slack Invite Link]).

## Table of Contents
- [Guiding Principles](#guiding-principles)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Decision-Making Process](#decision-making-process)
- [Pull Request (PR) Review and Approval](#pull-request-pr-review-and-approval)
- [Conflict Resolution](#conflict-resolution)
- [Community Engagement](#community-engagement)
- [Evolving Governance](#evolving-governance)
- [Contact](#contact)

## Guiding Principles

DTE’s governance is rooted in the manifesto’s core principles:
- **Transparency**: Decisions are made openly, with clear rationale shared in GitHub Issues, Discussions, or Slack.
- **Collaboration**: Contributions from data professionals, enterprises, SMBs, and hyperscalers shape DTE’s evolution.
- **Alignment**: All decisions support DTE’s mission to certify data systems by use case, risk, and value, ensuring trust and AI-readiness.
- **Inclusivity**: We welcome diverse perspectives while maintaining focus, as enforced by our [CODE_OF_CONDUCT.md](/community/CODE_OF_CONDUCT.md).
- **Agility**: Inspired by DataOps, we prioritize rapid feedback and iterative improvements.

## Roles and Responsibilities

- **Maintainers**:
  - **Who**: Initially, Brian Brewer (bbrewer@infolibcorp.com) and future trusted contributors elevated based on active participation.
  - **Responsibilities**:
    - Review and merge pull requests (PRs) for alignment with the [Manifesto](/Manifesto.md).
    - Moderate discussions, issues, and PRs per [CODE_OF_CONDUCT.md](/community/CODE_OF_CONDUCT.md).
    - Make final decisions on contributions and conflicts, seeking community input where possible.
    - Update repo structure, roadmap, and governance as DTE grows.
  - **Selection**: New maintainers are nominated by existing maintainers based on consistent, high-quality contributions (e.g., multiple merged PRs) and community trust. Nominations are discussed in GitHub Discussions and confirmed by consensus.

- **Contributors**:
  - **Who**: Anyone who submits PRs, issues, or participates in Discussions/Slack, from beginners to experts.
  - **Responsibilities**:
    - Follow [CONTRIBUTING.md](/community/CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](/community/CODE_OF_CONDUCT.md).
    - Propose artifacts (e.g., data quality scripts), case studies, or manifesto updates that advance DTE’s mission.
    - Engage respectfully and respond to feedback during PR reviews.

- **Community Members**:
  - **Who**: Anyone participating in GitHub Discussions, Slack, or X (#DTERevolution).
  - **Responsibilities**:
    - Provide feedback, propose ideas, and share DTE’s mission.
    - Report violations of the Code of Conduct to maintainers.

## Decision-Making Process

Decisions in DTE are made through a **consensus-driven model**, inspired by open-source projects like Rust and Node.js, to balance agility and inclusivity. Key decisions include PR approvals, artifact additions, manifesto updates, and governance changes.

1. **Proposal**:
   - Ideas (e.g., new artifact, principle update) are proposed via GitHub Issues or Slack (#contributions).
   - Use issue templates to ensure clarity (e.g., “New Artifact: Data Lineage Tracker”).

2. **Discussion**:
   - Community members discuss proposals in GitHub Issues, Discussions, or Slack, aiming for consensus.
   - Maintainers moderate to keep discussions on-topic and respectful.

3. **Decision**:
   - For minor changes (e.g., typo fixes, small PRs), maintainers approve or reject based on alignment with the [Manifesto](/Manifesto.md).
   - For major changes (e.g., new principles, governance updates), maintainers seek community input for 5-7 days via Discussions or Slack. If consensus isn’t reached, maintainers make the final call, explaining the rationale publicly.
   - Example: Adding a new manifesto principle requires 2+ maintainer approvals and community feedback.

4. **Documentation**:
   - Decisions are logged in GitHub Issues or Discussions with a clear explanation (e.g., “PR #123 merged to add data quality artifact, aligns with certification principle”).

## Pull Request (PR) Review and Approval

PRs are the primary way to contribute to DTE (e.g., artifacts, case studies, manifesto updates). The process follows [CONTRIBUTING.md](/community/CONTRIBUTING.md):

1. **Submission**:
   - Contributors fork the repo, create a branch, and submit a PR with a clear description (e.g., “Add Great Expectations script for data quality”).
   - Link to a related GitHub Issue for context.

2. **Review Criteria**:
   - **Alignment**: Does the PR advance DTE’s mission (certification, trust, AI-readiness)?
   - **Quality**: Is the code/documentation clear, functional, and well-documented?
   - **Relevance**: Does it fit DTE’s scope (e.g., avoids unrelated tech policies)?
   - Maintainers provide feedback within 5-7 days, requesting changes if needed.

3. **Automated Checks**:
   - Markdown linting (via GitHub Actions) ensures documentation consistency.
   - Code-based artifacts (e.g., Python scripts) should include validation steps or tests.

4. **Approval**:
   - PRs require at least one maintainer approval to merge.
   - Major changes (e.g., manifesto updates) need 2+ approvals and community feedback.
   - Rejected PRs receive polite feedback (e.g., “This is great but outside DTE’s focus on technical trust”).

5. **Merge**:
   - Approved PRs are merged into the main branch, with contributors credited in [CONTRIBUTORS.md](/CONTRIBUTORS.md).

## Conflict Resolution

Conflicts may arise over PRs, principles, or community interactions. We resolve them transparently:
- **Step 1: Discussion**:
  - Address conflicts in GitHub Issues, Discussions, or Slack (#general or #contributions).
  - Maintainers moderate to ensure respectful dialogue per [CODE_OF_CONDUCT.md](/community/CODE_OF_CONDUCT.md).
- **Step 2: Mediation**:
  - If consensus isn’t reached within 5 days, maintainers propose a solution (e.g., trial period for a new principle).
  - Community input is sought via Discussions or Slack.
- **Step 3: Final Decision**:
  - Maintainers make the final call, documenting the rationale in the relevant Issue or Discussion.
  - Example: If two contributors disagree on a PR’s wording, maintainers may merge a compromise version after discussion.
- **Step 4: Enforcement**:
  - Violations of the Code of Conduct (e.g., harassment) are addressed with warnings, content removal, or bans, as outlined in [CODE_OF_CONDUCT.md](/community/CODE_OF_CONDUCT.md).

## Community Engagement

DTE thrives on community input. To participate:
- **GitHub Discussions**: Propose ideas, provide feedback, or discuss artifacts like the Trust Dashboard.
- **Slack**: Join [datatrustengineering]([Slack Invite Link]) for real-time collaboration (#contributions, #trust-dashboard).
- **X**: Share your contributions with #DTERevolution or tag @bbrewer_infolib.
- **Good First Issues**: Start with tasks tagged “good first issue” (e.g., typo fixes, case studies) to build skills and join the community.
- **Recognition**: Contributors are listed in [CONTRIBUTORS.md](/CONTRIBUTORS.md) and highlighted in Slack or X for impactful work.

## Evolving Governance

As DTE grows, this governance model will evolve:
- **Feedback**: Community members can propose governance changes via GitHub Issues or Slack.
- **Updates**: Major changes (e.g., adding new maintainer roles) require 7-10 days of community discussion and 2+ maintainer approvals.
- **Organization Transition**: If the community scales, we may move the repo to a GitHub Organization for shared ownership, with roles defined here.

## Contact
- **Slack**: Join [datatrustengineering](https://join.slack.com/t/datatrustengineering/shared_invite/zt-3br05le6v-pxGSBeJGLpVgOsNM9ejGuw) (#general, #contributions)
- **Website**: [datatrustmanifesto.org](https://datatrustmanifesto.org)
- **Contribute**: Fork the repo, enhance the dashboard, or add DTE tools. See [CONTRIBUTING.md](/community/CONTRIBUTING.md).
- **Learn More**: Read the [DTE Manifesto](/Manifesto.md) for the full vision.
- **Inquiries**: Open a [Contact issue](https://github.com/askbrianfx/DataTrustEngineering/issues/new?template=contact.yml) or use our [contact form](https://forms.gle/S7V4zySe7gPqq56f8) for private questions.

Thank you for shaping DTE’s future. Let’s certify data systems for a trusted, AI-ready world!