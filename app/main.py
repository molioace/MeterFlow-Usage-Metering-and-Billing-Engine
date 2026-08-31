from fastapi import FastAPI

from app.api.routes import tenants, plans, subscriptions, usage

app = FastAPI(title="Usage Metering and Billing Engine")

app.include_router(tenants.router)
app.include_router(plans.router)
app.include_router(subscriptions.router)
app.include_router(usage.router)