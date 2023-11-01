# Project: ClimSim - Machine Learning for Climate Modeling

### [Full Project Description](doc/project3_desc.md)

<img src="https://leap-stc.github.io/ClimSim/_images/fig_1.png" alt="climsim" width="300"/>

Term: Fall 2023

-   Team 4
-   Team members
    -   Shreya Verma
    -   Daniel Rafael Lam
    -   Michael Wiley
    -   Zhenhui Wang
    -   Puqi Song
-   Project summary: In challenge I, we reproduced the quickstart notebook and created a report. In challenge II, Zhenhui implemented the quickstart notebook on Google Colab using Google Drive. Puqi developed an app using Huggingface Spaces that can directly show the quickstart notebook.
-   Link to Huggingface Space：<https://huggingface.co/spaces/puqi/climsim>

**Contribution statement**:

Michael Wiley: Ran full starter code. Modified starter code to be more robust and explicit. Subsampled dataset for other to use. Created process to subsample data based on system specs. Created script to determine system specs. Various code enhancements to main repo for modularity, reproducibility, and scalability. Various slides on final presentation.

Daniel Lam: Contributed to overcoming problems faced in challenge I. Assisted in data loading process and validation of data loading notebooks.

Shreya Verma: Developed the data loader using Huggingface hub. It uses the load function from Huggingface to import the data directly from the source, eliminating the step of downloading the data on our loca machine. The data is of large size and using this data loader will make it easy for everyone to work with data without worrying about the avaiable space on their local systems. Ran tests on multiple datasets by comparing the resulting array from our function with the original downloaded dataset. Added slides to the presentation about the value being added to the ClimSim project, easiness of integration, and future work that can be done to improve it further. 

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is organized as follows.

```         
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
