# Brain Modeling: Computational Modeling of Neurodegenerative Diseases
This project implements a computational framework to simulate and compare brain dynamics in **healthy conditions** versus **Alzheimer’s Disease** (AD) and **Frontotemporal Dementia** (FTD). 
Using a "MiniBrain" approach, the study investigates how pathology alters network responsiveness.

## Key Highlights
- **Model**: Implemented a 10-node Wilson-Cowan neural mass model representing disease-vulnerable regions (DMN and frontotemporal nodes).

- **Dynamics**: Conducted phase-plane analysis to study the stability of the system and identify the operating points of the network.

- **Findings**: Proved that neurodegeneration acts as a functional rescaling (shifting operating points) rather than a structural change in intrinsic local dynamics.

- **Disease Signatures**: AD showed diffuse sensitivity reduction, while FTD exhibited focal frontotemporal alterations.

## Methodology
- **Network Reconstruction**: Built a reduced connectivity matrix (MiniBrain) from the Harvard-Oxford atlas and TVB (The Virtual Brain) structural data.
- **Simulation**: Parametric modulation of excitatory/inhibitory gain to simulate disease severity ($\alpha$ parameter).
- - **Sensitivity Analysis**: Evaluated how nodes respond to external stimuli under different pathological loads.
 
## Visualizations
- **Phase Portraits**: Trajectories of excitatory ($E$) and inhibitory ($I$) populations.
- **Spatial Maps**: Mapping of sensitivity loss across the DMN and Frontotemporal networks.
- **Bifurcation Analysis**: Investigation of the system's stability near critical points.

----
### Tech Stack
- **Language**: Python

- **Libraries**: NumPy, SciPy (differential equations), Matplotlib, Seaborn.

- **Frameworks**: Concepts derived from The Virtual Brain (TVB).

### Repository Content
- **BrainModelingProject.ipynb**: Python implementation of the Wilson-Cowan dynamics and simulations.

- **BrainModelingReport.pdf**: Full scientific report detailing the mathematical framework and neurobiological implications.

