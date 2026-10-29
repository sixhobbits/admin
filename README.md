# Flask Hello World

A small Flask app with an HTML frontend, ready for PaaS deployment.

## Run locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/flask --app app run
```

Open <http://127.0.0.1:5000>.

## Deploy

The included `Procfile` starts the app with Gunicorn:

```text
web: gunicorn app:app
```

If your provider asks for a start command, use `gunicorn app:app`. The app also
provides a health check at `/health` and respects the platform's `PORT`
environment variable.

## Login proof-of-concept

`/login` renders a mock HCode Admin sign-in form, clearly stamped
`[PHISHING POC]`. It exists to exercise a form-based page on the PaaS; it does
not store, log, or transmit credentials, creates no session, and has no
authentication backend. The demo credentials default to `demo` / `demo` and can
be overridden with `DEMO_USERNAME` and `DEMO_PASSWORD`.
