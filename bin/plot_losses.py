import matplotlib.pyplot as plt
import h5py

# Load losses
with h5py.File('../results/train_losses.h5') as f:
    losses = f['/train_losses'].value

# Save plot
plt.ioff()
plt.plot(losses)
plt.ylim([0, 14])
plt.savefig('../results/train_losses_1000_batches.png')
