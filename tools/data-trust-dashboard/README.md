# Data Trust Engineering (DTE) Trust Dashboard

Welcome to the **Data Trust Engineering (DTE) Trust Dashboard**, a practical open-source tool that demonstrates DTE principles through interactive data visualization. This dashboard provides hands-on examples of monitoring AI governance metrics, helping data teams implement trust and reliability in their AI systems.

## About Data Trust Engineering (DTE)

Data Trust Engineering (DTE) provides practical patterns and tools that help data teams implement trust and reliability in AI and analytics systems. DTE offers engineering-driven approaches that work alongside existing data governance frameworks, focusing on actionable implementations rather than theoretical frameworks. By emphasizing collaboration and shared knowledge, DTE helps organizations build more reliable AI systems through proven patterns and community-developed tools.

## The DTE Trust Dashboard

The DTE Trust Dashboard is a working example that demonstrates practical monitoring approaches. It offers two implementations:

- **HTML Version** (`DTE_Trust_Dashboard.html`): Built with [Chart.js](https://www.chartjs.org) for lightweight, static visualization.
- **Streamlit Version** (`app.py`): Built with [Streamlit](https://streamlit.io) and [Plotly](https://plotly.com) for interactive, Python-based visualization.

Both versions demonstrate key monitoring approaches:

- **AI Fairness**: Bar chart showing fairness scores across protected attributes (e.g., gender, age), ensuring equitable outcomes. Integrates with [Fairlearn](https://fairlearn.org).
- **Model Explainability**: Bar chart visualizing feature importance across models, enhancing transparency. Compatible with [Evidently AI](https://evidentlyai.com).
- **Guardrails Adherence**: Radar chart visualizing adherence to DTE principles (trust, certification, observability) across privacy, ethics, robustness, transparency, and accountability.
- **GenAI Safety**: Bar chart monitoring toxicity, bias, hallucination, privacy leakage, and factual accuracy for generative AI. Integrates with Evidently AI.
- **Model Performance**: Line chart tracking accuracy, F1 score, and AUC-ROC over time, ensuring reliability. Integrates with [MLflow](https://mlflow.org).

**Practical Integration**:
- **Trust**: Transparent metrics help teams understand and improve their AI systems.
- **Collaboration**: Open-source and extensible, encouraging community contributions and improvements.
- **Engineering Focus**: Built with robust, accessible tools that can be adapted to different environments.

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
   - Customization: Modify Chart.js configurations or add metrics via pull requests.

### Streamlit Version
1. **Run the Dashboard**:
   - Follow `instructions.md` for detailed setup.
   - Briefly:
     ```bash
     cd tools/data-trust-dashboard
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
   - **Lineage**: OpenLineage for metadata tracking
   - **AI Governance**: Connect to Fairlearn (fairness), Evidently AI (explainability/drift), MLflow (performance), or [SDV](https://sdv.dev) (synthetic data).

### Docker Deployment (Optional)
```bash
# Quick start with Docker
docker-compose up --build

# Or run individual containers
docker build -t dte-dashboard .
docker run -p 8501:8501 dte-dashboard
```

## Contributing

Help improve the DTE Trust Dashboard! We welcome community contributions that enhance its practical value:

- Enhancements to either dashboard (e.g., API integration, new metrics).
- Documentation improvements and usage examples.
- Integration with additional monitoring tools.
- Performance optimizations and accessibility improvements.

See [CONTRIBUTING.md](/CONTRIBUTING.md) for guidelines. Submit pull requests to `/tools/data-trust-dashboard` or start a discussion on GitHub.

## Why It Matters

The DTE Trust Dashboard provides practical value by:

- **Building Understanding**: Clear visualizations help teams grasp complex AI governance concepts.
- **Enabling AI-Readiness**: Demonstrates monitoring approaches that support reliable AI deployment.
- **Supporting Collaboration**: Open-source foundation encourages community improvements and shared learning.
- **Fostering Best Practices**: Working example that can be adapted to different organizational needs.

## Setup Instructions

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/datatrustengineering/DataTrustEngineering.git
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

See [CONTACT.md](/CONTACT.md) for support channels.

## License

This project is licensed under the MIT License. See [LICENSE.md](/LICENSE) for details.

## Community Resources

- [DTE Manifesto](/Manifesto.md): Core principles and philosophy.
- [Contributing Guide](/CONTRIBUTING.md): How to contribute effectively.
- [Code of Conduct](/CODE_OF_CONDUCT.md): Community standards.
- [Governance](/community/GOVERNANCE.md): Decision-making processes.
- [Case Study Template](/docs/case-studies/template.md): Share implementation experiences.
- [Report Issues](https://github.com/datatrustengineering/DataTrustEngineering/issues): Bug reports and feature requests.

## Acknowledgments

The DTE Trust Dashboard demonstrates practical approaches to AI governance and monitoring. We thank the community for feedback, contributions, and collaboration that help improve these tools for everyone.

---

*Built with Data Trust Engineering principles of collaboration and practical implementation.*