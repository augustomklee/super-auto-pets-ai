# Super Auto Pets AI Player & Coach

## Project Overview

This project implements an intelligent agent for Super Auto Pets (SAP), a turn-based auto battler game, coupled with a coaching interface to assist human players. We combine reinforcement learning with computer vision to create a system that can both play autonomously and provide strategic guidance.

![System Demo](https://github.com/lanierjh/Sapaifull/raw/main/examples/demo.gif)

## Game Context

Super Auto Pets presents players with several strategic challenges:

- Managing a team of 5 pets with unique abilities and stats
- Making decisions during the buy stage (purchasing pets/items, selling, re-rolling, re-ordering)
- Resource management with limited coins per turn (10 coins per shop turn)
- Planning without complete information
- Adapting to randomized shop offerings
- Optimizing for long-term rewards

## Team Members

- John Bettinger
- Jackson Lanier
- Justin Zhu
- Augusto Lee

## Technical Implementation

### Environment Adaptation

- Updated the SAPAI simulation environment and SAPAI gym training framework
- Limited scope to the free turtle pack available in the base game
- Updated pet stats and abilities to match current game version
- Implemented new pets (wolverine, armadillo, pigeon) not present in previous versions

### Training Methodology

We trained our reinforcement learning model using different approaches:

- **Model Architecture:** MaskablePPO from the Super ML Pets repository
- **Training Methods:**
- Fine-tuning with Random Opponent Generator
- Fine-tuning with Difficulty Scaling Opponent Generator
- Continuous training with Random Opponent Generator
- Continuous training with Difficulty Scaling Opponent Generator
- **Training Steps:** 1,000,000 steps for each approach
- **Key Finding:** Continuous training resulted in more consistently improving results versus fine-tuning, which peaked before performance degradation

### AI Coaching System

- **Computer Vision:** Image recognition to read the shop screen and identify available pets
- **Decision Engine:** Processed shop state through our trained RL agent to determine optimal actions
- **Action Explanation:** Integrated with Google's LLM Gemini via API to translate AI decisions into understandable commands
- **User Interface:** Presented recommendations through a chat-box interface

## Technical Challenges

- **Image Recognition Bottleneck:** While using a pre-trained model with access to high-definition sprites, accuracy and speed remained below expectations
- **Environment Simulation:** Required significant updates to match current game mechanics and pet abilities
- **Opponents Modeling:** Created custom opponent generators to simulate realistic gameplay progression

## Future Work

- Improve image recognition for better pet detection in the shop
- Expand the coach to provide multiple strategic options and branching decisions
- Continuously update the simulation environment for game balance changes
- Add support for additional pet packs beyond the turtle pack
- Explore direct game training (rather than simulation) using improved image recognition
- Address the challenge of obtaining shop data without relying on image recognition

## Acknowledgments

- Super ML Pets repository
- SAPAI simulation environment
- SAPAI gym training framework
- Team Toast for creating Super Auto Pets

## License

MIT License
