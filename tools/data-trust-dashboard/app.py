import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="Data Trust Engineering (DTE) Trust Dashboard",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for cobalt theme
st.markdown("""
    <style>
    .main {
        background-color: #1a1a1a;
        color: #d4d4d4;
        font-family: Arial, sans-serif;
    }
    h1 {
        color: #ffffff;
        text-align: center;
        font-size: 2.5rem;
    }
    h2 {
        color: #00d787;
        font-size: 1.8rem;
        margin: 30px 0 15px;
    }
    .metric {
        background: #0d1117;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #00d787;
        box-shadow: 0 0 8px rgba(0, 215, 135, 0.3);
        text-align: center;
    }
    .metric h3 {
        color: #ffffff;
        font-size: 1.2rem;
        margin-bottom: 10px;
    }
    .metric p {
        font-size: 1.5rem;
        color: #40ffa0;
        margin: 0;
    }
    .metric small {
        color: #8b949e;
        font-size: 0.9rem;
    }
    .stMarkdown {
        color: #d4d4d4;
    }
    a {
        color: #00d787;
        text-decoration: none;
    }
    a:hover {
        color: #40ffa0;
    }
    @media (max-width: 768px) {
        h1 {
            font-size: 2rem;
        }
        h2 {
            font-size: 1.5rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Data Trust Engineering (DTE) Trust Dashboard")

# AI Governance Overview
st.header("AI Governance Overview")
cols = st.columns(4)
with cols[0]:
    st.markdown('<div class="metric"><h3>AI Fairness Score</h3><p>0.92</p><small>+0.05</small></div>', unsafe_allow_html=True)
with cols[1]:
    st.markdown('<div class="metric"><h3>Model Explainability</h3><p>78%</p><small>+12%</small></div>', unsafe_allow_html=True)
with cols[2]:
    st.markdown('<div class="metric"><h3>Guardrails Adherence</h3><p>95%</p><small>+3%</small></div>', unsafe_allow_html=True)
with cols[3]:
    st.markdown('<div class="metric"><h3>GenAI Safety Index</h3><p>0.88</p><small>+0.07</small></div>', unsafe_allow_html=True)

# AI Fairness Across Protected Attributes
st.header("AI Fairness Across Protected Attributes")
fairness_data = pd.DataFrame({
    "Attribute": ["Gender", "Age", "Race", "Income"],
    "Score": [0.95, 0.88, 0.91, 0.86]
})
fig_fairness = px.bar(
    fairness_data,
    x="Attribute",
    y="Score",
    text="Score",
    range_y=[0, 1],
    color_discrete_sequence=["#00d787"],
    template="plotly_dark"
)
fig_fairness.update_traces(textposition="outside", marker_opacity=0.6)
fig_fairness.update_layout(
    plot_bgcolor="#0d1117",
    paper_bgcolor="#0d1117",
    font_color="#d4d4d4",
    xaxis_title="",
    yaxis_title="Fairness Score",
    showlegend=False
)
st.plotly_chart(fig_fairness, use_container_width=True)

# Model Explainability Across Features
st.header("Model Explainability Across Features")
explainability_data = pd.DataFrame({
    "Model": ["A", "A", "A", "A", "A", "B", "B", "B", "B", "B", "C", "C", "C", "C", "C", "D", "D", "D", "D", "D", "E", "E", "E", "E", "E"],
    "Feature": ["F1", "F2", "F3", "F4", "F5"] * 5,
    "Score": [0.9, 0.3, 0.5, 0.7, 0.1, 0.6, 0.8, 0.2, 0.4, 0.9, 0.7, 0.5, 0.8, 0.3, 0.6, 0.2, 0.7, 0.9, 0.4, 0.5, 0.5, 0.4, 0.3, 0.8, 0.7]
})
fig_explain = px.bar(
    explainability_data,
    x="Model",
    y="Score",
    color="Feature",
    barmode="group",
    range_y=[0, 1],
    color_discrete_sequence=["#00d787", "#40ffa0", "#006633", "#99ff99", "#00a86b"],
    template="plotly_dark"
)
fig_explain.update_layout(
    plot_bgcolor="#0d1117",
    paper_bgcolor="#0d1117",
    font_color="#d4d4d4",
    xaxis_title="",
    yaxis_title="Explainability Score",
    legend_title="Feature"
)
st.plotly_chart(fig_explain, use_container_width=True)

# Guardrails Adherence Radar
st.header("Guardrails Adherence Radar")
guardrails_data = pd.DataFrame({
    "Metric": ["Data Privacy", "Ethical Use", "Robustness", "Transparency", "Accountability"],
    "Score": [95, 80, 90, 70, 85]
})
theta = guardrails_data["Metric"].tolist() + [guardrails_data["Metric"].iloc[0]]
r = guardrails_data["Score"].tolist() + [guardrails_data["Score"].iloc[0]]
fig_radar = go.Figure(data=go.Scatterpolar(
    r=r,
    theta=theta,
    fill="toself",
    line_color="#0057d8",
    marker=dict(size=10)
))
fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(color="#d4d4d4")),
        angularaxis=dict(tickfont=dict(color="#d4d4d4"))
    ),
    showlegend=False,
    plot_bgcolor="#0d1117",
    paper_bgcolor="#0d1117",
    font_color="#d4d4d4"
)
st.plotly_chart(fig_radar, use_container_width=True)

# GenAI Safety Metrics
st.header("GenAI Safety Metrics")
safety_data = pd.DataFrame({
    "Metric": ["Toxicity", "Bias", "Hallucination", "Privacy", "Accuracy"],
    "Score": [0.05, 0.12, 0.08, 0.03, 0.92],
    "Threshold": [0.10, 0.15, 0.10, 0.05, 0.90]
})
fig_safety = px.bar(
    safety_data.melt(id_vars="Metric", value_vars=["Score", "Threshold"]),
    x="Metric",
    y="value",
    color="variable",
    barmode="group",
    text="value",
    range_y=[0, 1],
    color_discrete_map={"Score": "#00d787", "Threshold": "#ff6384"},
    template="plotly_dark"
)
fig_safety.update_traces(textposition="outside")
fig_safety.update_layout(
    plot_bgcolor="#0d1117",
    paper_bgcolor="#0d1117",
    font_color="#d4d4d4",
    xaxis_title="",
    yaxis_title="Score",
    legend_title=""
)
st.plotly_chart(fig_safety, use_container_width=True)

# AI Model Performance Over Time
st.header("AI Model Performance Over Time")
performance_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Accuracy": [0.64, 0.70, 0.67, 0.73, 0.76, 0.74, 0.76, 0.78, 0.76, 0.81, 0.83, 0.86],
    "F1 Score": [0.60, 0.63, 0.62, 0.68, 0.71, 0.70, 0.73, 0.76, 0.74, 0.78, 0.80, 0.81],
    "AUC-ROC": [0.68, 0.69, 0.68, 0.74, 0.76, 0.74, 0.78, 0.80, 0.76, 0.83, 0.86, 0.88]
})
fig_perf = px.line(
    performance_data.melt(id_vars="Month", value_vars=["Accuracy", "F1 Score", "AUC-ROC"]),
    x="Month",
    y="value",
    color="variable",
    range_y=[0, 1],
    color_discrete_map={"Accuracy": "#00d787", "F1 Score": "#0057d8", "AUC-ROC": "#9966ff"},
    template="plotly_dark"
)
fig_perf.update_layout(
    plot_bgcolor="#0d1117",
    paper_bgcolor="#0d1117",
    font_color="#d4d4d4",
    xaxis_title="",
    yaxis_title="Score",
    legend_title=""
)
st.plotly_chart(fig_perf, use_container_width=True)

# Key Metrics Explained
st.header("Key Metrics Explained")
st.markdown("""
- **AI Fairness Score**: Measures overall fairness of AI models across protected attributes, ensuring equitable outcomes.
- **Model Explainability**: Percentage of model decisions that can be clearly explained to stakeholders.
- **Guardrails Adherence**: Measures adherence to data trust guardrails (privacy, ethics, robustness, transparency, accountability).
- **GenAI Safety Index**: Composite score reflecting the safety and reliability of generative AI models.
- **Fairness Across Protected Attributes**: Breakdown of fairness scores for demographic groups (e.g., gender, age).
- **Model Explainability Across Features**: Visualizes feature importance across AI models for transparency.
- **Guardrails Adherence Radar**: Multi-dimensional view of adherence to data trust principles.
- **GenAI Safety Metrics**: Tracks toxicity, bias, hallucination, privacy leakage, and factual accuracy for generative AI.
- **AI Model Performance Over Time**: Monitors accuracy, F1 score, and AUC-ROC to ensure consistent quality.
""")
st.markdown('Built with Data Trust principles of agility and collaboration. See the <a href="/Manifesto">Data Trust Manifesto</a> for details on engineering rigor.', unsafe_allow_html=True)