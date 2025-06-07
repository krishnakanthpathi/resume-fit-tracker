
# Resume Fit Evaluation System

This project is an intelligent API-based system that evaluates how well a candidate's resume fits a given job description using natural language processing and sentence embeddings.

## 🚀 Features

- Fit score generation using `SentenceTransformer (MiniLM)`
- Skill extraction using `SpaCy` and a custom skills dataset
- Matched vs. missing skills identification
- Personalized learning path recommendations based on skill gaps
- RESTful API powered by `FastAPI`
- Batch evaluation support

## 🛠️ Technologies Used

- Python 3.x
- FastAPI
- SentenceTransformers (`all-MiniLM-L6-v2`)
- SpaCy
- Pandas
- Scikit-learn
- JSON

## 📦 Project Structure

```
RESUME_FIT_TRACKER/
│
├── app/
│   ├── data/
│   │   ├── config.json                  # Configuration thresholds (fit scores, learning cutoffs)
│   │   ├── learning_paths.json          # Skill-wise learning steps
│   │   ├── missing_track.json           # (Optional) Alternative track data
│   │   └── skills_dataset.csv           # List of known skills for extraction
│   │
│   ├── models/
│   │   ├── common_models.py             # Shared model structures (like learning_step)
│   │   ├── request_models.py            # Pydantic models for API requests
│   │   ├── response_models.py           # Pydantic models for API responses
│   │   └── models.py                    # (Optional) Base or other models
│   │
│   ├── services/
│   │   ├── fit_score_engine.py          # Core logic for score calculation and verdict
│   │   ├── learning_paths_extractor.py  # Suggest learning steps for missing skills
│   │   └── skill_extractor.py           # Extract matched and missing skills using SpaCy
│   │
│   ├── tests/
│   │   ├── tests_api.py                 # API endpoint tests
│   │   ├── tests_fit_score.py           # Unit tests for score logic
│   │   ├── tests_skills_extractor.py    # Tests for skill extraction logic
│   │
│   ├── utils/
│   │   └── __init__.py                  # Utility package init (can hold text_cleaner, etc.)
│   │
│   └── main.py                          # FastAPI entry point with route definitions
│
├── .dockerignore                        # (If Dockerized) Ignore rules for build context
├── .gitignore                           # Git ignore rules
└── README.md                            # Project documentation


```

## 🧠 How It Works

1. **Input**: Resume text and Job Description.
2. **Embedding**: Texts are encoded using `SentenceTransformer` to get semantic vectors.
3. **Similarity**: Cosine similarity calculates a Fit Score (0 to 1) uses v1.
4. **Verdict**: Based on score, result is classified as `Strong Fit`, `Moderate Fit`, or `Weak Fit`.
5. **Skills**: Skills are extracted using `SpaCy PhraseMatcher`.
6. **Learning Path**: For missing skills, learning steps are suggested.

***version*** : v1 - TF-IDF + Cosine Similarity
          v2 - SentenceTransforme

## 🖥️ API Endpoints

| Method | Endpoint             | Description                     |
|--------|----------------------|---------------------------------|
| GET    | `/`                  | Welcome message                 |
| GET    | `/health`            | Health check                    |
| GET    | `/version`           | API version                     |
| POST   | `/evaluate-fit`      | Evaluate a single resume        |
| POST   | `/evaluate-fit-all`  | Evaluate multiple resumes       |

## 📝 Sample Request

```json
{
  "resume_text": "Experienced software engineer skilled in Python, Java, and Docker.",
  "job_description": "Looking for a developer with Python, Kubernetes, and Docker experience."
}
```

## 📊 Sample Response

```json
{
  "fit_score": 0.88,
  "verdict": "strong_fit",
  "matched_skills": ["Python", "Docker"],
  "missing_skills": ["Kubernetes"],
  "recommended_learning_track": [
    {
      "skill": "Kubernetes",
      "steps": ["core concepts", "deployment", "networking"]
    }
  ],
  "status": "ok"
}
```

## ✅ Future Enhancements

- Add frontend UI for visualization
- Resume improvement suggestions
- Live job scraping for automated JD input
- User authentication and history tracking

---

### 👨‍💻 Author

**Krishna Kanth Pathi**  
🔗 [Portfolio](https://krishnakanth.epizy.com/) | [GitHub](https://github.com/krishnakanthpathi)

