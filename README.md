# Resume Analyzer (Full Stack)

A resume analyzer with a **Flask backend** (parsing + ATS scoring API) and a
**single-page frontend** (drag-and-drop upload, animated scan preview, score
dial, skill chips, role-fit gap analysis).

## Structure
```
resume_analyzer/
├── backend/
│   ├── app.py            # Flask server + /api/analyze endpoint
│   ├── resume_core.py     # parsing + scoring logic
│   ├── skills_list.py     # skill keyword bank + role skill-sets
│   ├── requirements.txt
│   └── uploads/           # temp storage, files deleted right after parsing
└── frontend/
    └── index.html         # single-file UI (served by Flask)
```

## Setup

```bash
cd backend
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Run

```bash
cd backend
python app.py
```

Then open **http://127.0.0.1:5000** in your browser. The Flask app serves
both the API and the frontend, so there's nothing else to start.

## What it does
1. Upload a PDF/DOCX resume (drag-and-drop or browse).
2. Optionally pick a **target role** from the dropdown (Web Developer, Data
   Analyst, ML Engineer, Java Backend Developer, GIS/Remote Sensing Analyst).
3. The backend extracts Name, Email, Phone, Skills, Education, Experience
   and computes:
   - an **ATS readiness score** (/100, weighted across contact info, name,
     education, experience, skill count)
   - a **role-fit percentage** and list of **missing skills** for the
     selected role, if one was picked.
4. Results render as a score dial, breakdown bars, detected-field grid,
   skill chips, and a role-fit gap list.

Files are deleted from the server immediately after each analysis — nothing
is persisted.

## Extending
- Add more roles/skills in `skills_list.py` → `ROLE_SKILLS`.
- Swap the keyword-based skill matcher for a trained NER model (see the
  DataTurks dataset below) for more robust extraction.
- Add a `/api/history` endpoint + a small SQLite table if you want to keep
  a log of past analyses.

## Test data
Real resumes to batch-test parsing accuracy against (not required to run
the app — the app works on any single resume you drop into it):

- **Kaggle Resume Dataset** (~2400 resumes, 25 job categories, PDF):
  https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset
- **DataTurks Resume Entities for NER** (labeled Name/Skills/Degree spans,
  useful if you later train a custom spaCy NER model instead of keyword
  matching):
  https://www.kaggle.com/datasets/dataturks/resume-entities-for-ner
