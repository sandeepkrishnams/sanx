# Runbook

Quick operational runbook for deploying and troubleshooting sanx instances.

Start (dev):

```bash
python -m sanx.core
```

Start (production with TLS):

1. Create or obtain cert/key (PEM files).
2. In your deploy script, build an SSLContext via `sanx.ssl_utils.build_ssl_context(certfile, keyfile)`.

Scaling:

- Use `worker.py` to spawn multiple preforked processes (one per CPU) behind a load balancer.
- Place an edge proxy (nginx, envoy) in front for connection buffering, TLS termination (or pass-through), and rate limiting.

Troubleshooting:

- Check logs for stack traces in `core` when handlers raise exceptions.
- Use metrics hooks (Prometheus) to monitor request latencies and error rates.
