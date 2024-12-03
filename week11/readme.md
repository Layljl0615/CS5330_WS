# Lab 11: Generative AI
- Generative AI: involves models and techniques that create new content, such
as images, videos, or text.
- Generative AI has applications in:
  - Digital Art: Generating creative artworks.
  - Content Creation: Automating design and animation processes.
  - Medical Imaging: Synthesizing CT or MRI scans for research

### Adversarial Images
- Adversarial Images: images altered slightly to trick AI models
- An example of this would be misclassifying a “stop” sign as “yield”
- The purpose of adversarial images is to test model robustness and improve
security against adversarial attacks
- A technique to accomplish this is to add noise
- For example, through the FGSM (Fast Gradient Sign) method

### FGSM Example
- cv2.addWeighted(src1, alpha, src2, beta, gamma):
  - src1: First input array (e.g., original image).
  - alpha: Weight of the first array.
  - src2: Second input array (e.g., adversarial noise).
  - beta: Weight of the second array.
  - gamma: Scalar added to each sum.
- This function combines two images with specified weights and
adds a scalar value.

### Generative Adversarial Networks
- GANs (Generative Adversarial Networks) consist of two models:
  - Generator: Produces fake images from random noise.
  - Discriminator: Distinguishes between real and fake images.
- The models are trained together in a competitive setting.
- Training Objective:
  - Generator tries to "fool" the discriminator by producing realistic samples.
  - Discriminator learns to better detect fake images.
  - Adversarial loss ensures both networks improve simultaneously.

### Additional information:
Generative AI refers to models that generate new content, such as images, videos, or text, and is used in fields like digital art, content creation, and medical imaging. One application is the creation of adversarial images, which are slightly altered to deceive AI models. Techniques like FGSM (Fast Gradient Sign Method) add noise to images, tricking models into making incorrect predictions. Generative Adversarial Networks (GANs) consist of a generator and a discriminator, where the generator creates fake images, and the discriminator attempts to identify them as fake. Both networks are trained in competition, improving through adversarial loss.







