#!/usr/bin/env python3
"""Can torch see a ROCm device? That's the whole script."""

def main() -> None:
    try:
        import torch
    except ImportError:
        print("torch not installed")
        return

    print("torch", torch.__version__)
    print("hip", getattr(torch.version, "hip", None))
    ok = torch.cuda.is_available()
    print("cuda.is_available (HIP under the hood on ROCm):", ok)
    if not ok:
        print("no device — check drivers / HIP_VISIBLE_DEVICES")
        return
    n = torch.cuda.device_count()
    print("count:", n)
    for i in range(n):
        print(f"  [{i}]", torch.cuda.get_device_name(i))
        # TODO: print total memory once I remember the right API on this build
        try:
            props = torch.cuda.get_device_properties(i)
            print(f"       total_mem_gb≈{props.total_memory / (1024**3):.1f}")
        except Exception as e:  # noqa: BLE001 — probe script, shrug
            print("       props failed:", e)


if __name__ == "__main__":
    main()
