import torch
import time

def main():
    # Define the model
    model = ...

    # Define the input tensor
    input_tensor = torch.randn(1, 3, 224, 224) 

    # Measure the FPS
    num_runs = 3
    total_time = 0
    for i in range(num_runs):
        start_time = time.perf_counter()
        with torch.no_grad():
            output = model(input_tensor)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    fps = 1 / (total_time / num_runs)

    # Measure the FLOPS
    flops = torch.cuda.memory_allocated() * 2 / (total_time / num_runs)
    print('FPS: {:.2f}, FLOPS: {:.2f}'.format(fps, flops))


if __name__ == '__main__':
    main()

