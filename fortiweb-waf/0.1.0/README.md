# FortiWeb WAF Add-on

Validated on FortiWeb **8.0.5** trial.

Provides FortiDashboard with a push-telemetry channel from FortiWeb. FortiWeb
forwards Attack, Traffic, and Event logs to the dashboard endpoint at
`POST /api/soc/ingest/fortiweb`. The dashboard normalizes those logs into the
SIEM event types `waf.attack`, `waf.dos`, `waf.blocked_request`, and
`http.attack`, which `siem_kowalski` turns into incidents.

## Package layout

```
fortiweb-waf/0.1.0/
  addon.json
  connector/__init__.py
  fixtures/attack-log.json
  README.md
```

## Connect form

| Field        | Type    | Required | Notes                                    |
|--------------|---------|----------|------------------------------------------|
| host         | url     | yes      | FortiWeb management URL.                 |
| apiKey       | secret  | no       | Optional REST health probe.              |
| ingestMode   | text    | yes      | Default `push`.                          |
| verifyTls    | boolean | no       | Default `false` for lab trials.          |

## Lab setup

See the FortiDashboard runbook
`docs/operations/fortiweb-landing-waf-lab.md` for the full topology and the
log-forwarding configuration on FortiWeb 8.0.5.
