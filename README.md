# craft-a11y-insight-api

**Automated Accessibility Auditing as a Service**

## Project Naming Convention

This project follows a personal naming convention to distinguish development approaches:
- `craft-*` repositories: Hand-crafted without AI code generation
- `create-*` repositories: Built with AI assistance for rapid development

This project is hand-crafted to ensure deep understanding of the underlying technologies.

---

## Overview

A11y-Insight API is a REST API designed to automate accessibility auditing for modern web applications. With the European Accessibility Act (EAA) coming into force in June 2025, organizations need scalable solutions to ensure their digital products meet WCAG 2.1 Level AA compliance requirements.

### The Problem

Current accessibility auditing approaches face several limitations:
- Manual audits are time-consuming and expensive
- Existing automated tools lack integration with modern CI/CD pipelines
- Enterprise solutions are often cost-prohibitive for smaller teams
- Single-Page Applications (React, Vue, Angular) require browser rendering for accurate testing

### The Solution

This API provides automated accessibility scanning using industry-standard tools (Axe-core) combined with browser automation (Playwright) to accurately assess JavaScript-heavy applications. Designed as a cloud-native service, it integrates seamlessly into existing development workflows.

---

## Technical Architecture

### Core Technologies

**Backend Framework**
- Python 3.14+ (async/await support)
- FastAPI (high-performance async REST framework)
- Pydantic (data validation and type safety)

**Testing Engine**
- Playwright (headless browser automation)
- Axe-core (WCAG 2.1 Level AA compliance testing)

**Infrastructure** (planned)
- Docker (containerization)
- GitHub Actions (CI/CD)
- Cloud deployment (AWS/Heroku)

---

## Installation

### Prerequisites
- Python 3.11 or higher
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/your-username/craft-a11y-insight-api.git
cd craft-a11y-insight-api

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Configure environment
cp .env.example .env
# Edit .env with your configuration
```

### Running the API
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

Interactive API documentation: `http://localhost:8000/docs`

---

## API Endpoints

**Status:** In Development

### Planned Endpoints

**Health Check**
```
GET /status
Returns server health and version information
```

**Accessibility Audit**
```
POST /audit
Request body: { "url": "https://example.com" }
Returns: Detailed accessibility report with violations and score
```

Full API documentation available via Swagger UI at `/docs` when running locally.

---

## Development Approach

This project is built without AI code generation to ensure comprehensive understanding of:
- Asynchronous programming patterns in Python
- FastAPI framework architecture
- Browser automation with Playwright
- Production-ready API design principles
- Modern DevOps practices

Learning resources utilized include official documentation, technical tutorials, and conceptual discussions. All code is written manually to maximize learning outcomes.

---

## Project Motivation

This project serves as a practical demonstration of backend development capabilities while addressing a real-world compliance requirement. It combines:

**Technical Skills**
- Backend API development (Python/FastAPI)
- Asynchronous programming patterns
- Browser automation architecture
- RESTful API design
- Modern deployment practices

**Domain Expertise**
- Web accessibility standards (WCAG 2.1)
- Compliance requirements (EAA)
- Single-Page Application testing challenges

**Professional Development**
- Transition from frontend to fullstack/backend engineering
- Production-ready software design
- DevOps and cloud deployment

---

## Project Status

**Current Phase:** Week 1 - Setup and Foundation

**Completed**
- Project structure and environment setup
- Documentation and repository initialization
- Dependency management

**In Progress**
- Core API functionality (Playwright + Axe-core integration)

**Planned**
- Docker containerization
- CI/CD pipeline implementation
- Cloud deployment
- Comprehensive error handling
- API rate limiting and authentication

---

## Testing

Testing infrastructure to be implemented in Week 4.

---

## Contributing

This is a personal learning project and is not currently accepting contributions. However, feedback and suggestions are welcome via GitHub issues.

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback regarding this project, please open an issue on GitHub.

---

**Project Timeline**

- Week 1: Setup & Foundation
- Week 2: Core functionality (Playwright + Axe-core integration)
- Week 3: Docker & Error handling
- Week 4: Documentation & polish
- Week 5+: CI/CD & Cloud deployment