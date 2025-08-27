# DTE Trust Dashboard - Streamlit App Instructions

This guide explains how to run the Data Trust Engineering (DTE) Trust Dashboard (`app.py`) locally to visualize AI governance metrics and charts.

## Prerequisites
- **Python**: Version 3.8 to 3.11 installed (`python3 --version` to check).
- **Operating System**: macOS, Linux, or Windows.
- **Project Directory**: `/datatrustengineering/static/tools/data-trust-dashboard/`.

## Setup
1. **Navigate to the Project Directory**:
   ```bash
   cd /Users/brianbrewer/Code/datatrustengineering/static/tools/data-trust-dashboard
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   You should see `(venv)` in your terminal prompt.

4. **Install Dependencies**:
   Install the required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` includes:
   ```
   streamlit==1.28.1
   pandas==2.1.3
   plotly==5.17.0
   numpy==1.25.2
   ```
   If `requirements.txt` is missing, create it with the above content or install manually:
   ```bash
   pip install streamlit==1.28.1 pandas==2.1.3 plotly==5.17.0 numpy==1.25.2
   ```

## Running the App
1. **Start the Streamlit Server**:
   With the virtual environment activated, run:
   ```bash
   streamlit run app.py
   ```
   This will launch the app and open a browser window at `http://localhost:8501`.

2. **Access the Dashboard**:
   - If the browser doesn’t open automatically, navigate to `http://localhost:8501`.
   - Verify the dashboard displays:
     - **Metrics**: AI Fairness (0.92), Model Explainability (78%), Guardrails Adherence (95%), GenAI Safety (0.88).
     - **Charts**: Bar charts (Fairness, Explainability, Safety), Radar chart (Guardrails), Line chart (Performance).
     - **Theme**: Cobalt background (#1a1a1a), green accents (#00d787), blue radar (#0057d8).
     - **Explanations**: List of metrics and a link to the Data Trust Manifesto.

## Troubleshooting
- **Charts Not Rendering**:
  - Check the browser console (F12) for errors.
  - Ensure dependencies are installed: `pip list` should show `streamlit==1.28.1`, `pandas==2.1.3`, `plotly==5.17.0`, `numpy==1.25.2`.
  - Clear Streamlit cache: `streamlit cache clear`.
  - Try Firefox or Safari if Chrome fails.
- **Port Conflict**:
  - If `localhost:8501` is unavailable, check for conflicts:
    ```bash
    lsof -i :8501
    ```
  - Run on a different port if needed:
    ```bash
    streamlit run app.py --server.port 8502
    ```
- **Dependency Issues**:
  - Update pip: `pip install --upgrade pip`.
  - Reinstall dependencies: `pip install -r requirements.txt`.
- **Theme Issues**:
  - If the cobalt theme doesn’t apply, clear the browser cache (Chrome: DevTools > Application > Clear site data).

## Notes
- The app is designed for local use but can be deployed to Streamlit Community Cloud by pushing `app.py` and `requirements.txt` to a GitHub repository.
- For further assistance, contact the Data Trust Engineering team or refer to the [Data Trust Manifesto](/Manifesto.md).

*Last updated: August 26, 2025, 01:44 PM EDT*