# Data Trust Engineering (DTE) Trust Dashboard

Welcome to the **Data Trust Engineering (DTE) Trust Dashboard**, a flagship artifact of the *Data Trust Engineering* movement. This open-source dashboard visualizes key AI governance metrics in real-time, embodying DTE’s principles of trust, engineering rigor, and AI-readiness as outlined in the [Data Trust Manifesto](https://datatrustmanifesto.org). The dashboard empowers data teams to build trusted, scalable systems, addressing the 70-85% failure rates of traditional data governance (Gartner, 2025).

## About Data Trust Engineering (DTE)

Data Trust Engineering (DTE) is a revolutionary, engineering-driven approach to data management that represents a complete pivot from traditional data governance frameworks. Unlike governance’s bureaucratic, process-heavy models, which conflate compliance (e.g., GDPR, HIPAA, SOC, EU AI Act) with technical data management, DTE decouples these concerns entirely. Compliance is handled by legal and audit teams using tools like OneTrust, freeing DTE to focus on certifying datasets for trust, quality, lineage, security, and AI-readiness. This shift addresses the 70-80% failure rate of traditional governance [Gartner, 2025] by prioritizing technical trust over rigid policies, enabling scalable, cloud-native, and AI-ready systems. Built on the [Data Trust Manifesto](https://datatrustmanifesto.org)’s principles—trust, engineering rigor, adaptability, enablement, cloud-native design, certification by use case/risk/value, technical debt management, and community collaboration—DTE empowers data professionals to deliver reliable systems for high-stakes use cases like AI training and regulatory reporting in 2025’s 175-zettabyte data landscape [Statista, 2025]. By leveraging tools like Fairlearn, Evidently AI, and MLflow, DTE certifies datasets based on their specific use case, risk profile, and business value, fostering a vendor-neutral, community-driven evolution of data management. Read the full [DTE Manifesto](/Manifesto) to join the #DTERevolution.

## The DTE Trust Dashboard 

The DTE Trust Dashboard is a practical, open-source tool that brings DTE to life. It offers two implementations:
- **HTML Version** (`DTE_Trust_Dashboard.html`): Built with [Chart.js](https://www.chartjs.org) for lightweight, static visualization.
- **Streamlit Version** (`app.py`): Built with [Streamlit](https://streamlit.io) and [Plotly](https://plotly.com) for interactive, Python-based visualization.

Both versions monitor key AI governance metrics:
- **AI Fairness**: Bar chart showing fairness scores across protected attributes (e.g., gender, age), ensuring equitable outcomes. Integrates with [Fairlearn](https://fairlearn.org).
- **Model Explainability**: Bar chart visualizing feature importance across models, enhancing transparency. Compatible with [Evidently AI](https://evidentlyai.com).
- **Guardrails Adherence**: Radar chart visualizing adherence to DTE principles (trust, certification, observability) across privacy, ethics, robustness, transparency, and accountability. Supports certification by use case, risk, and value, per the Data Trust Manifesto.
- **GenAI Safety**: Bar chart monitoring toxicity, bias, hallucination, privacy leakage, and factual accuracy for generative AI. Integrates with Evidently AI.
- **Model Performance**: Line chart tracking accuracy, F1 score, and AUC-ROC over time, ensuring reliability. Integrates with [MLflow](https://mlflow.org).

**Data Trust Integration**:
- **Trust**: Transparent, real-time metrics build confidence for enterprises, users, and AI systems (Data Trust Manifesto principle).
- **Collaboration**: Open-source and extensible, inviting community contributions to evolve the dashboard (Data Trust Manifesto principle).
- **Engineering Rigor**: Built with robust, lightweight tools (Chart.js for HTML, Plotly for Streamlit), compatible with [Apache Superset](https://superset.apache.org) for scalability (Data Trust Manifesto principle).

The dashboards are housed in `/tools/data-trust-dashboard/` and can be extended with APIs or additional metrics.

## Getting Started

### HTML Version
1. **Run the Dashboard**:
   - Open `DTE_Trust_Dashboard.html` in a browser for a local preview.
   - Host on GitHub Pages or a web server for team access.
   - For production, integrate with APIs (e.g., Evidently AI for explainability, MLflow for performance) to replace simulated data.

2. **Explore the Code**:
   - File: `DTE_Trust_Dashboard.html`
   - Tech Stack: HTML, JavaScript, Chart.js
   - Customization: Modify Chart.js configurations or add metrics (e.g., bias-variance tradeoffs) via pull requests.

### Streamlit Version
1. **Run the Dashboard**:
   - Follow `instructions.md` for detailed setup.
   - Briefly:
     ```bash
     cd /Users/brianbrewer/Code/datatrustengineering/static/tools/data-trust-dashboard
     python3 -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     pip install -r requirements.txt
     streamlit run app.py
     ```
   - Open `http://localhost:8501` in a browser.
   - For production, deploy to [Streamlit Community Cloud](https://streamlit.io/cloud) or integrate with APIs.

2. **Explore the Code**:
   - File: `app.py`
   - Tech Stack: Python, Streamlit, Plotly, Pandas, NumPy
   - Customization: Modify Plotly charts or add metrics via pull requests.

3. **Integrate with Tools**:
   - **Data Quality**: Use [Great Expectations](https://greatexpectations.io) for automated validation.
   - **Lineage**: OpenLineage
   - **AI Governance**: Connect to Fairlearn (fairness), Evidently AI (explainability/drift), MLflow (performance), or [SDV](https://sdv.dev) (synthetic data).

## Contributing

Join the #DTERevolution by contributing to the DTE Trust Dashboard! We welcome:
- Enhancements to either dashboard (e.g., API integration, new metrics).
- Case studies showing DTE in action (add to `/docs/case-studies`).
- Tools or patterns for data quality, lineage, or AI governance (add to `/tools`).

See [CONTRIBUTING.md](/CONTRIBUTING.md) for guidelines. Submit pull requests to `/tools/data-trust-dashboard` or start a discussion on [X](https://x.com) with #DTERevolution.

## Why It Matters

Traditional data governance fails 70-85% of the time (Gartner, 2025) due to bureaucracy and misalignment with modern data needs. The DTE Trust Dashboard, guided by the [Data Trust Manifesto](https://datatrustmanifesto.org)’s focus on trust, engineering rigor, and AI-readiness, empowers data teams to:
- Build **trust** with transparent metrics for fairness and observability.
- Enable **AI-readiness** by monitoring explainability and performance.
- Scale with **cloud-native** architectures, aligning with shared responsibility models.
- Foster **collaboration**, inviting community contributions to evolve DTE.

## Setup Instructions

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/[YourUsername]/DataTrustEngineering.git
   ```
2. **Navigate to the Dashboard**:
   ```bash
   cd tools/data-trust-dashboard
   ```
3. **Run the HTML Version**:
   - Open `DTE_Trust_Dashboard.html` in a browser or deploy to a server.
   - Customize data sources by updating the `refreshData()` function with API endpoints.
4. **Run the Streamlit Version**:
   - See `instructions.md` for detailed steps, including virtual environment setup and dependency installation.
   - Run `streamlit run app.py` and access `http://localhost:8501`.
   - Customize data sources by updating `app.py` with API calls (e.g., Fairlearn, Evidently AI, MLflow).

## Community and Support

- **Slack**: Join [datatrustengineering](https://join.slack.com/t/datatrustengineering/shared_invite/zt-3br05le6v-pxGSBeJGLpVgOsNM9ejGuw) (#general, #contributions)
- **Website**: [datatrustmanifesto.org](https://datatrustmanifesto.org)
- **Contribute**: Fork the repo, enhance the dashboard, or add DTE tools. See [CONTRIBUTING.md](/community/CONTRIBUTING).
- **Learn More**: Read the [DTE Manifesto](/Manifesto.md) for the full vision.
- **Inquiries**: Open a [Contact issue](https://github.com/DataTrustEngineering/DataTrustEngineering/issues/new?template=contact.yml) or use our [contact form](https://forms.gle/S7V4zySe7gPqq56f8) for private questions.

## License

This project is licensed under the MIT License. See [LICENSE.md](/LICENSE) for details.

## Community Resources

- [DTE Manifesto](manifesto.md): Our vision for trusted, AI-ready data systems.  
- [Contributing Guide](community/CONTRIBUTING.md): How to submit artifacts, case studies, or updates.  
- [Code of Conduct](community/CODE_OF_CONDUCT.md): Standards for a respectful community.  
- [Governance](community/GOVERNANCE.md): How we make decisions and manage contributions.  
- [Case Study Template](docs/case-studies/template.md): Share your DTE success story.  
- [Contributors](community/CONTRIBUTORS.md): Meet the community shaping DTE.  
- [Support](SUPPORT.md): How to get help or contact us.  
- [Security](SECURITY.md): Report vulnerabilities or sensitive issues.  
- [Report Issues & Propose Features](https://github.com/datatrustengineering/DataTrustEngineering/issues): Submit bug reports or suggest new artifacts.  



## Acknowledgments

The DTE Trust Dashboard is a cornerstone of the [Data Trust Manifesto](https://datatrustmanifesto.org), driving a collaborative, automation-driven approach to data management. We thank the DTE community for inspiring and contributing to the #DTERevolution.

#DTERevolution