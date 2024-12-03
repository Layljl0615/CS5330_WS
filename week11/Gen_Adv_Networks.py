generator = nn.Sequential(
    nn.Linear(latent_dim, 128),  # Fully connected layer: maps input noise to 128 features
    nn.ReLU(),                   # Activation function: introduces non-linearity
    nn.Linear(128, 256),         # Expands the feature space to 256 dimensions
    nn.ReLU(),                   # Another activation function to make learning non-linear
    nn.Linear(256, 28 * 28),     # Output layer: maps features to 784 pixels (28x28 image)
    nn.Tanh()                    # Scales output pixel values to the range [-1, 1]
)
discriminator = nn.Sequential(
    nn.Linear(28 * 28, 256),    # Input layer: takes flattened 28x28 image (784 pixels)
    nn.LeakyReLU(0.2),          # Activation: allows small gradients for negative inputs (slope = 0.2)
    nn.Linear(256, 128),        # Hidden layer: reduces features to 128 dimensions
    nn.LeakyReLU(0.2),          # Another activation for non-linearity
    nn.Linear(128, 1),          # Output layer: maps features to a single value (real/fake score)
    nn.Sigmoid()                # Activation: outputs probability [0, 1] (real = 1, fake = 0)
)
# Calculate loss for real images
real_loss = criterion(discriminator(real_imgs), real_labels)  # How well the discriminator classifies real images as real

# Calculate loss for fake images
fake_loss = criterion(discriminator(fake_imgs.detach()), fake_labels)  # How well the discriminator classifies fake images as fake

# Total loss for the Discriminator
d_loss = real_loss + fake_loss  # Combine losses for real and fake images

# Backpropagation to compute gradients
d_loss.backward()  # Update weights to minimize the Discriminator's loss

# Apply the weight updates
optimizer_D.step()  # Update Discriminator parameters using the computed gradients

# Get the discriminator's predictions for the fake images
fake_preds = discriminator(fake_imgs)  # Check how "real" the discriminator thinks the fake images are

# Calculate the Generator's loss
g_loss = criterion(fake_preds, real_labels)  # Goal: Fool the discriminator into thinking fake images are real

# Backpropagation to compute gradients for the Generator
g_loss.backward()  # Update Generator's weights to minimize its loss

# Apply the weight updates
optimizer_G.step()  # Update Generator parameters using the computed gradients
