# amd-rocm-benchkit

Tiny ROCm health checks I run before blaming the model.

Half the time "the LLM is slow" is actually "the driver is weird" or "I pointed at the wrong device". This repo is a pile of small probes — not a serious suite like rocBLAS benches, just enough to know the box is alive.

## scripts

| script | does |
|--------|------|
| `scripts/gpu_snapshot.sh` | rocm-smi + rocminfo snippet |
| `scripts/torch_probe.py` | can pytorch see the GPU |
| `probes/matmul_smoke.py` | dumb matmul timing (not a real benchmark!!) |

## usage

```bash
./scripts/gpu_snapshot.sh
python3 scripts/torch_probe.py
python3 probes/matmul_smoke.py
```

Output goes to stdout. Redirect somewhere if you care.

## caveats

- numbers from `matmul_smoke` are vibes, not publication-grade
- I wrote this for MI300X curiosity but it should work on other ROCm GPUs
- still waiting on access to the big card, so MI300X-specific quirks unknown

See also: my [openai server notes](https://github.com/aloohhg-rgb/amd-mi300x-openai-server).

MIT.

if this helps you cool; if not, also cool.
