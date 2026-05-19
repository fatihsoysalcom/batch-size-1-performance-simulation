import time

# Simulate a fixed overhead that occurs once per "batch" or "inference call".
# In real ML models (like diffusion models), this could be model loading, GPU context switching,
# kernel launch overhead, data transfer setup, etc. This overhead is paid even for a single item.
OVERHEAD_PER_BATCH_MS = 50  # milliseconds

# Simulate the actual processing time for each individual item.
# This scales linearly with the number of items in the batch.
PROCESSING_PER_ITEM_MS = 10  # milliseconds

def simulate_image_generation(batch_size: int) -> float:
    """
    Simulates the time taken to generate images for a given batch size.
    Returns the total time in seconds.
    """
    start_time = time.perf_counter()

    # Apply the fixed overhead that happens once per inference call
    time.sleep(OVERHEAD_PER_BATCH_MS / 1000.0) # Convert ms to seconds

    # Apply processing time for each item in the batch
    time.sleep((PROCESSING_PER_ITEM_MS * batch_size) / 1000.0) # Convert ms to seconds

    end_time = time.perf_counter()
    return end_time - start_time

if __name__ == "__main__":
    NUM_IMAGES_TO_GENERATE = 5 # Total number of images we want to generate

    print(f"Simulating generation of {NUM_IMAGES_TO_GENERATE} images...")
    print("-" * 40)

    # --- Scenario 1: Generating images one by one (Batch Size 1) ---
    print(f"Scenario 1: Generating {NUM_IMAGES_TO_GENERATE} images individually (Batch Size = 1)")
    total_time_batch_1 = 0.0
    for i in range(NUM_IMAGES_TO_GENERATE):
        # Each call incurs the fixed overhead, making it inefficient for multiple items
        item_time = simulate_image_generation(batch_size=1)
        total_time_batch_1 += item_time
        print(f"  Image {i+1}/{NUM_IMAGES_TO_GENERATE}: took {item_time:.4f} seconds")

    print(f"\nTotal time for Batch Size 1 (generating {NUM_IMAGES_TO_GENERATE} images): {total_time_batch_1:.4f} seconds")
    print("-" * 40)

    # --- Scenario 2: Generating all images in a single batch ---
    print(f"Scenario 2: Generating {NUM_IMAGES_TO_GENERATE} images in one batch (Batch Size = {NUM_IMAGES_TO_GENERATE})")
    # The fixed overhead is incurred only once for the entire batch, amortizing it
    total_time_batch_N = simulate_image_generation(batch_size=NUM_IMAGES_TO_GENERATE)
    print(f"  Generated {NUM_IMAGES_TO_GENERATE} images in one go: took {total_time_batch_N:.4f} seconds")

    print(f"\nTotal time for Batch Size {NUM_IMAGES_TO_GENERATE} (generating {NUM_IMAGES_TO_GENERATE} images): {total_time_batch_N:.4f} seconds")
    print("-" * 40)

    # --- Comparison ---
    print("\n--- Comparison ---")
    print(f"Batch Size 1 total time: {total_time_batch_1:.4f} seconds")
    print(f"Batch Size {NUM_IMAGES_TO_GENERATE} total time: {total_time_batch_N:.4f} seconds")

    if total_time_batch_1 > total_time_batch_N:
        speedup_factor = total_time_batch_1 / total_time_batch_N
        print(f"\nBatching provides a speedup of approximately {speedup_factor:.2f}x!")
        print("This demonstrates how amortizing fixed overheads across multiple items in a batch improves efficiency.")
    else:
        print("\nBatching did not provide a significant speedup in this simulation.")
        print("This might happen if per-item processing dominates or overhead is negligible.")
