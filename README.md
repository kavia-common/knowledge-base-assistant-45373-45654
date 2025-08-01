# knowledge-base-assistant-45373-45654

## End-to-End Integration Testing Guide

To validate full frontend-backend integration (file upload, Q&A, references, chart, history, admin), use the `e2e_fullstack_api_test.py` Python script in the `utils/` directory.

### Prerequisites
- Backend server (FastAPI) running at http://localhost:8000
- Frontend is not directly needed for this test, but you should also verify UI separately.
- Python dependencies: `requests`

### Running the E2E test
```bash
pip install requests
python utils/e2e_fullstack_api_test.py
```

This will:
- Upload a test file
- Ask a question, verify references
- Fetch chart data and check formats
- Fetch query history
- Validate admin endpoints (including bad/good token handling)
- Check CORS policy on upload endpoint

A summary will be printed, and exit code will be nonzero if any check fails.
