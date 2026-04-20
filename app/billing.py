"""Runtime settings for the billing integration."""

import os

STRIPE_KEY = os.environ["STRIPE_SECRET_KEY"]
if not STRIPE_KEY.startswith("sk_live_"):
    raise ValueError("expected a live secret key")
