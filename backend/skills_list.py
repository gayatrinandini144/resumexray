# Keyword bank for skill matching + role skill-sets for match scoring.
# Extend freely.

SKILLS_DB = [
    "python", "java", "c++", "c", "javascript", "typescript", "sql", "r",
    "go", "rust", "php", "kotlin", "swift", "matlab", "scala",
    "html", "css", "react", "angular", "vue", "node.js", "express",
    "django", "flask", "spring boot", "next.js", "bootstrap", "tailwind",
    "machine learning", "deep learning", "nlp", "computer vision",
    "pandas", "numpy", "scikit-learn", "tensorflow", "keras", "pytorch",
    "data analysis", "data visualization", "power bi", "tableau",
    "opencv", "yolo", "spacy", "nltk",
    "mysql", "postgresql", "mongodb", "sqlite", "oracle", "firebase", "redis",
    "aws", "azure", "gcp", "docker", "kubernetes", "git", "github",
    "ci/cd", "linux", "jenkins",
    "gis", "remote sensing", "arcgis", "qgis", "google earth engine",
    "satellite imagery", "image classification",
    "communication", "teamwork", "leadership", "project management",
    "problem solving", "time management",
]

# Target-role skill sets, used to compute a "role fit" percentage
# and highlight missing skills for that role.
ROLE_SKILLS = {
    "Web Developer": [
        "html", "css", "javascript", "react", "node.js", "express",
        "mongodb", "git", "sql",
    ],
    "Data Analyst": [
        "python", "sql", "pandas", "numpy", "data analysis",
        "data visualization", "power bi", "tableau", "excel",
    ],
    "Machine Learning Engineer": [
        "python", "machine learning", "deep learning", "pandas", "numpy",
        "scikit-learn", "tensorflow", "pytorch", "sql", "git",
    ],
    "Java Backend Developer": [
        "java", "spring boot", "sql", "mysql", "git", "docker",
        "aws", "linux", "rest",
    ],
    "GIS / Remote Sensing Analyst": [
        "gis", "remote sensing", "arcgis", "qgis", "python",
        "google earth engine", "satellite imagery", "image classification",
    ],
}
