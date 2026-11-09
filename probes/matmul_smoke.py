#!/usr/bin/env python3
"""
Dumb matmul timing. NOT a real benchmark.
I use this to see if the GPU is doing *something* before I start a long model load.
"""
import time

def main() -> None:
    import torch

    if not torch.cuda.is_available():
        print("no gpu, abort")
        return

    device = torch.device("cuda:0")
    print("device:", torch.cuda.get_device_name(0))

    # sizes picked because they feel fine, not because of a paper
    n = 4096
    a = torch.randn(n, n, device=device, dtype=torch.float16)
    b = torch.randn(n, n, device=device, dtype=torch.float16)

    # warmup
    for _ in range(3):
        _ = a @ b
    torch.cuda.synchronize()

    t0 = time.perf_counter()
    for _ in range(10):
        c = a @ b
    torch.cuda.synchronize()  # FIXME: I forgot this once and believed a miracle
    dt = time.perf_counter() - t0
    print(f"{n}x{n} fp16 matmul x10 -> {dt:.3f}s (vibes only)")
    print("checksum", float(c[0, 0]))  # keep c alive


if __name__ == "__main__":
    main()
