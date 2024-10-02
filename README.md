# Quantum Entanglement Game
## Game Name: Space Socks
## Genre: Educational
## Description:
Quantum Computing is the future. However, like the popular phrase goes “It’s simple, it’s not quantum mechanics”- there is a misconception that the quantum world is too complicated for everyone to understand. 

While the quantum world is truly vastly different from our everyday universe, it hosts potential to transform the future and it is crucial to clear these misconceptions and instill a basic and fundamental understanding of quantum concepts to pave the path for the future of quantum computing.

According to Boston Consulting Group’s projection, quantum computing will create $450 billion to $850 billion of economic value by 2040. The quantum computing future is here and the world needs to be equipped for it.

Our endeavors to support this cause was to gamify the approach of quantum entanglement and quantum hotspots. 

Taking the popular example of Prof.Bertlmann's mismatched socks to illustrate quantum entanglement, **Space Socks** is a single-player game that simulates quantum entanglement and teleportation.

## Quantum Entanglement:
Quantum entanglement is one of the most profound yet confusing aspects of quantum mechanics. When two particles are in entangled quantum states, measuring a property of one of the particles reveals information about the other particle without even needing to check. 



![Entangled socks](https://github.com/Celeste-A-Space-Research-Center/quantum-entanglement-game-space-socks/blob/main/assets/entangled_socks.jpg)


If I have a pair of socks- one left and one right and I send my friend Bob a sock, we can call this pair of socks entangled. Without checking what sock I have, if Bob checks the sock I sent him- he automatically knows about my sock. If Bob received a left sock, I must have a right sock and vice versa.

## Who it is for, and why we think you should play the game:

Our quantum entanglement game is designed for curious learners, tech enthusiasts, and anyone interested in quantum mechanics and its real-world applications. Whether you are new to the subject or a seasoned science enthusiast, the game provides an engaging way to explore ****quantum teleportation****, ****entanglement swapping****, and the emerging ****quantum internet****. It’s also ideal for those who want to grasp future technologies in an intuitive and interactive manner.

The game introduces the mechanism involved to ensure data delivery through quantum internet, and all the operations you perform in the game manually, can be implemented by a ****Software-Defined Network****. Quantum internet comes in with a lot of future applications in ****scientific phenomenon exploration****, ****space communication**** and ****disaster management****, to name a few.

## Requirements:

Your system has to be set up to contain the following to play the game.

* Terminal / Command Prompt.
* Python version >=3.0.0
* Pygame
* Your favourite code editor /IDE (Visual Studio Code / Jupiter Notebook/ PyCharm) can come in handy.

## The game involves:

* The **transmitter** (Alice) placed at a stationary point called the point of reference to understand relative speed of satellite rotation and entanglement.
  
* The **teleporter** (A satellite) made to rotate around the earth at a speed that equals the optimum time taken to run a quantum **teleportation circuit** on the accessible quantum processors and simulators (viz, IBM's qasm).
  
* The **receiver** (Bob) made to rotate around the earth in a spaceship around the earth at a speed that equals the optimum time taken to run a quantum teleportation circuit.
  
* 3 pairs each of red- and yellow-colored socks rotating consecutively around the earth at a speed matching the time taken to run the **teleportation circuit**. 

By building a proper circuit and playing the game well, you can help Alice send a message to Bob maintaining quantum entanglement. And boom- now you too understand quantum circuits, quantum entanglement and essentially how the quantum world works. Maybe we’re one step closer to flipping the saying from **“It’s simple, it’s not quantum mechanics”** to **“It’s as simple as quantum mechanics”**.

## How to Play:
### Objective:
The primary objective is to help Alice send her message to Bob by selecting the appropriate quantum circuit (lines), adjusting angles and distances, and choosing the correct quantum gate to maintain the entanglement. Success is measured by delivering the message without disruption.

![The First Screen](https://github.com/Celeste-A-Space-Research-Center/quantum-entanglement-game-space-socks/blob/main/assets/The%20first%20scene.png)


### Controls:
* **Build your Teleportation Circuit**: Teleport your message with the colour of sock that you intend to let Bob know about, as shown in the demo video. Hit on the green **Run** button, and voila, you can proceed once you succeed. This is the start of your quantum communication action.
  
* **Select your Line**: Successful building of the quantum circuit will activate the sock you have chosen, and also the **Line**, **Angle** and **Distance** boxes.Choose the line that Alice's message will travel along. You can select a line either by typing the line number (e.g., Line 1, Line 2) or clicking on the line directly using the mouse.

![Line Activation](https://github.com/Celeste-A-Space-Research-Center/quantum-entanglement-game-space-socks/blob/main/assets/Line%20activation.png)


* **Input the angle**: After selecting a line, input the angle (θ) at which the message should travel. The angle is essential in determining the trajectory. You can enter the angle using the keyboard, or adjust using the on-screen controls.

![Angle Activation](https://github.com/Celeste-A-Space-Research-Center/quantum-entanglement-game-space-socks/blob/main/assets/Angle%20activation.png)


* **Input the distance**: After the angle is set, input the distance the message will travel along the line.Similar to the angle, input this value via the keyboard or on-screen controls.

 ![Distance Activation](https://github.com/Celeste-A-Space-Research-Center/quantum-entanglement-game-space-socks/blob/main/assets/Distance%20Activation.png)
 

## Gameplay Mechanism:
1. **Message (Sock)**: Alice's message is represented by a colored sock (red or yellow). The color of the sock determines the type of quantum gate that should be selected to ensure entanglement.

2. **Quantum Gates**: The game features various quantum gates like the H Gate, X Gate, T Gate, etc. These gates modify how the message interacts with the circuit. Choosing the wrong gate will disrupt the entanglement, causing the message to fail.

3. **Globe Movement**: The game environment includes a globe, and the message travels around its surface based on the line, angle, and distance inputs. The player must ensure that Alice's message stays within the globe’s boundaries.

4. **Quantum Entanglement**: Success is determined by whether or not Alice’s message remains entangled as it travels to Bob. If the message successfully reaches Bob while maintaining its quantum properties, the player wins the round.

## Step-by-Step Guide:
1. **Launch the Game**:

   ****To run it on your personal computer****: Clone this github repository to Visual Studio Code. Make sure you have python setup on VS Code. Install the pygame 
   package with *pip install pygame* on the VS Code terminal that appears when you open the folder that is created as a result of cloning. Start the game by running 
   the quantum_game.py script.
  

2. **Drag the Gates on to the Coloured Line**:Select the quantum gate that corresponds to the message's color. Choose wisely, as the wrong gate will disrupt the quantum entanglement.Build the teleportation circuit and hit on run.You can proceed to the entanglement swapping operations after building the teleportation circuit successfully.

3. **Select a Line**: Choose a line for Alice's message to travel by typing the line number or clicking on it. There are 9 lines available to choose from.

4. **Input Angle and Distance**: After selecting the line, enter the angle (θ) and distance that will guide the message to Bob.

5. **Hit Enter**: Once all inputs are ready, hit the enter key on the keyboard to send the message from Alice to Bob.

6. **Observe the Result**: Watch as the message travels along the line. If it successfully reaches Bob, you will see a "Quantum Entanglement Success" message. If it fails, you will need to try again with different inputs.

 ![Distance Validity](https://github.com/Celeste-A-Space-Research-Center/quantum-entanglement-game-space-socks/blob/main/assets/Distance%20Validity.png)

 ![Game Scene](https://github.com/Celeste-A-Space-Research-Center/quantum-entanglement-game-space-socks/blob/main/assets/game%20scene.png)


## Demo of the Game

[Demo Video .mp4 with narration](https://github.com/Celeste-A-Space-Research-Center/quantum-entanglement-game-space-socks/blob/main/assets/Demo%20of%20the%20game.mp4)

![Demo Gif](https://github.com/Celeste-A-Space-Research-Center/quantum-entanglement-game-space-socks/blob/main/assets/Demoofthegame.gif)


## Game Strategy and Tips:
1. **Gate Selection**: Pay close attention to the color of Alice's sock (message). The correct quantum gate is crucial to maintaining the message's entanglement.

2. **Experiment with Angles and Distances**: Some levels may require trial and error. Adjusting angles and distances slightly can make all the difference in whether the message reaches Bob.

3. **Stay Within the Globe**: Ensure that your message travels along the globe’s surface. Going outside the globe will result in a lost message and a failed circuit.

![Entanglement Success](https://github.com/Celeste-A-Space-Research-Center/quantum-entanglement-game-space-socks/blob/main/assets/entanglement_success.png)


## How Do I Win: 

1. **Perfectly Match the Socks**: Carefully observe the color of the socks passing by and initiate the teleportation only when Bob is correctly positioned with a sock of the same color. The game is won when Alice’s message successfully reaches Bob with a matching sock, maintaining quantum entanglement. A message stating "Quantum Entanglement Success!" will confirm your victory.

2. **Master Entanglement**: To ensure a flawless transfer, precisely manage the entanglement swapping process by strategically selecting the optimal path for message transmission. Your choices will directly impact the success of the transfer.

3. **Maximize Your Reach**: For higher scores, focus on maximizing the distance between Alice and Bob during each successful information transfer. The further apart they are when the message is successfully delivered, the more points you will earn.

## Scoring:
1. **Earn Points**: Points are awarded based on the distance over which you successfully transfer quantum information. Longer distances result in higher scores.

2. **Detect Hotspots**: Each successful teleportation action adds a point to your "Quantum Internet Hotspot" list. Accumulate enough hotspots to dominate the game and achieve ultimate victory.

## Future Scope:
In subsequent versions of the game, we aim to enhance gameplay by simulating quantum communication through the teleporter and implementing an entanglement swapping mechanism. This will be processed in real-time through circuit runtime, allowing players to explore complex concepts in quantum physics while enjoying an engaging and interactive experience.

## Contributors:
This research project has followed open science and open research principles to ensure that knowledge and resources are accessible to the broader community. The contributors involved in various aspects of the project include:

* **Game Concept Designer**:
Suma Mallapragada

* **Developers**:
Samiksha Mekala, Supriya Nalla, Ananya Sangani

* **Documentation and Writing**:
Nikhita Makam, Samiksha Mekala, Ananya Sangani

### Acknowledgements

This research activity was undertaken under **Celeste GNITS**, a space research center at **G. Narayanamma Institute of Technology and Science, Hyderabad**. We extend our thanks to the team at Celeste GNITS for their valuable support.We also acknowledge the faculty and administration of G. Narayanamma Institute of Technology and Science, Hyderabad for their valuable contributions in providing both research insights and essential resources.
