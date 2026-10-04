# HypothesisX AI — Data Explorer

This is the **Data Explorer Agent** of the HypothesisX AI multi-agent system.

## What it does

The Data Explorer is the first stage of HypothesisX AI. It inspects a dataset before other agents perform pattern mining, hypothesis generation, and validation.

It currently checks:

- Number of rows
- Number of columns
- Column names
- Data types
- Missing values
- Duplicate rows
- Unique values
- First 10 rows
- Basic descriptive statistics

## Supported files

- CSV
- Excel `.xlsx`
- Excel `.xls`

## Project structure

```text
HypothesisX_Data_Explorer/
├── app.py
├── data_explorer.py
├── requirements.txt
├── README.md
└── data/
    └── simulated_weather.xlsx
```

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Streamlit:

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Next development stage

After this Data Explorer is working, the next agents can be added:

1. Pattern Mining Agent
2. Hypothesis Generation Agent
3. Alternative Explanation Agent
4. Statistical + ML/DL Validation Agent
5. Robustness + Evidence Agent
6. Orchestrator Agent

The Data Explorer should remain focused on understanding the dataset rather than generating hypotheses.
