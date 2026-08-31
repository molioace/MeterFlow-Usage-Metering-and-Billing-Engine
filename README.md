# MeterFlow - Usage Metering & Billing Engine

A backend service for SaaS applications to track customer usage, enforce quotas, calculate costs, and handle billing.

The goal is to answer three core questions:

* **How much has this customer used?**
* **What does their usage cost?**
* **Have they reached their limit?**

## What It Covers

* Usage metering
* Customer quotas and limits
* Subscription and plan management
* Accurate money calculations
* Idempotent usage events
* Rate limiting
* Stripe test-mode billing

## Tech Stack

* **FastAPI** — API
* **Supabase / PostgreSQL** — persistent data
* **Redis** — rate limiting, counters, caching, and idempotency
* **Stripe** — billing in test mode
* **Docker** — containerization
* **uv** — Python dependency management

## Project Status

🚧 **In development**

The project is being built incrementally with a focus on correctness, especially around usage tracking, quotas, and money calculations.
