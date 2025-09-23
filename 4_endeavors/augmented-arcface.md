---
tags:
  - endeavors/research
status: backlog
---
- arcface is an _activation function_ that is used as an alternative to softmax
- it maps distributions onto a unit sphere?
- potential augmentation: learn a radius value so that the mapping is not required to be on the unit sphere
- intuition:
    - more narrow terms (i.e. corgi, poodle) can exist farther radii
    - more broad terms (i.e, mammal, dog) can exist closer to the origin
    - the farther away from the origin, the more space there is for representation of distinct subtypes
    - but as you get closer to the origin, broader terms can represent the same concepts, but fully encapsulate them in the angular $\theta$ domain

- how can we make stuff closer/farther away?
    - entropy? if the model is more confused than it could be an arbitrary concept

- Project 5 (++) _Semi-supervised image classification_:
    - assuming that only M out of N images in the training data have ground truth labels, design and implement a weakly supervised training of classification network that can benefit from unlabeled examples in the training dataset (e.g. MNIST or CIFAR-10, but you need to ignore labels on a subset of training examples)
    - You should demonstrate how the performance changes as M gets progressively smaller
    - While you can use any well-motivated ideas, one basic approach could be to combine cross-entropy on labeled points with (unsupervised) K-means clustering loss over deep features (e.g. in the last layer before the linear classifier)
        - It is also advisable to use augmentation (a loss enforcing consistent labeling of augmented training examples)
    - You can also explore Mutual Information loss function formulated in Bridle & MacKay "Unsupervised Classifiers, Mutual Information and Phantom Targets", NIPS 1991