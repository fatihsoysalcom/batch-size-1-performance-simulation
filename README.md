# batch-size-1-performance-simulation
This example simulates the performance difference when generating multiple items one by one (batch size 1) versus processing them in a single batch. It highlights how fixed overheads per inference call can significantly slow down operations when not amortized across a larger batch, a common issue in image generation models.
