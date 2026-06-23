# AI Customer Refund Agent

## Overview

AI Customer Refund Agent is a web application that automates the refund review process for an e-commerce platform.

The application accepts customer refund requests through a chat interface, validates the request against predefined refund policies, and returns an approval or denial decision. An admin dashboard displays the internal reasoning steps used by the agent during the decision-making process.

The project demonstrates how AI-assisted workflows can help customer support teams process refund requests consistently while enforcing company policies.

---

## Features

* Customer chat interface
* AI-generated customer responses using Groq LLM
* Mock CRM database with customer profiles
* Order database with multiple refund scenarios
* Refund policy validation
* Refund approval and denial workflows
* Admin dashboard with reasoning logs
* Tool-based backend architecture
* Environment variable based API key management

---

## Project Structure

```text
AI_Refund_Agent

backend
│
├── app
│   │
│   ├── data
│   │   ├── customers.json
│   │   ├── orders.json
│   │   └── refund_policy.txt
│   │
│   ├── tools
│   │   ├── customer_tool.py
│   │   ├── order_tool.py
│   │   └── policy_tool.py
│   │
│   ├── llm.py
│   ├── refund_agent.py
│   ├── schemas.py
│   └── main.py
│
├── requirements.txt
└── .env

frontend
│
├── index.html
├── style.css
└── script.js

README.md
```

---

## Architecture

```text
Customer Request
        │
        ▼
Refund Agent
        │
        ▼
Order ID Extraction
        │
        ▼
Customer Lookup Tool
        │
        ▼
Order Lookup Tool
        │
        ▼
Policy Validation Tool
        │
        ▼
Refund Decision
        │
        ▼
Groq LLM Response
        │
        ▼
Customer Response
```

---

## Refund Policy Rules

The agent evaluates refund requests using the following rules:

* Refund requests must be submitted within 30 days of purchase.
* A valid order ID must be provided.
* The order must exist in the system.
* Digital products are not refundable.
* Clearance products are not refundable.
* Orders that have not been delivered are not refundable.
* Eligible orders are approved automatically.

---

## How It Works

1. Customer submits a refund request.
2. The system extracts the order ID from the message.
3. The Customer Lookup Tool searches the CRM database.
4. The Order Lookup Tool retrieves order information.
5. The Policy Validation Tool checks refund eligibility.
6. The refund decision is generated.
7. Groq generates a customer-friendly response.
8. All reasoning steps are displayed in the admin dashboard.

---

## Example Requests

### Approved Refund

```text
Refund for O1001
```

### Refund Outside Policy Window

```text
Refund for O1002
```

### Digital Product Refund

```text
Refund for O1003
```

### Missing Order ID

```text
I want a refund
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI_Refund_Agent
```

### Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Create Environment File

Create a `.env` file inside the `backend` directory.

```env
LLM_PROVIDER=groq
GROQ_API_KEY=your_api_key
```

### Run Backend

```bash
cd backend
uvicorn app.main:app --reload
```

### Launch Frontend

Open:

```text
frontend/index.html
```

in your browser.

---

## Tech Stack

### Backend

* Python
* FastAPI

### Frontend

* HTML
* CSS
* JavaScript

### AI

* Groq
* Llama 3.3 70B Versatile

### Data Storage

* JSON files

---

## Future Improvements

* Voice-based customer support
* Database integration
* Order history tracking
* Authentication and authorization
* LangGraph-based agent workflows
* Multi-policy support

---

## Demo Scenarios

### Scenario 1: Successful Refund

Customer submits:

```text
Refund for O1001
```

Result:

```text
Refund Approved
```

### Scenario 2: Refund Window Exceeded

Customer submits:

```text
Refund for O1002
```

Result:

```text
Refund Denied
```

### Scenario 3: Digital Product Refund

Customer submits:

```text
Refund for O1003
```

Result:

```text
Refund Denied
```

### Scenario 4: Missing Order ID

Customer submits:

```text
I want a refund
```

Result:

```text
Agent requests a valid order ID
```
