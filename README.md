# Collaborative project

This educational dashboard aims to mimic a large collaborative project to promote a team work and exercise basic skills underlying collaborative software development.
Specifically, the objective of the project is to implement the following development steps:

- creating virtual environment and installing required packages
- forking/cloning existing repository using git
- creating branches and developing new features within the existing project
- testing code locally
- committing and merging branches with the changes

**Disclaimer**: 
This project doesn't serve as an example of "good coding practice" for web app or any other python development.
It is created solely for educational purposes and represents a flexible framework where students can exercise team work and code writing.

## Project description

The project is focused on development of functionality for a simple molecules mining dashboard. The dashboard consists of four panels: *input panel*, *results summary*, *molecules properties* and *examples of molecules*. 
The dashboard performs a search over [ChEMBL database](https://www.ebi.ac.uk/chembl/) (using REST API) to retrieve molecules similar to the input molecule or scaffold. 
If molecules are found, the statistics on their physicochemical properties is printed in the table in *results summary* and visualized as histograms in *molecules properties*. 
Additionally, it plots images of retrieved molecules given the selection criteria in *examples of molecules*. 

Initially, dashboard is empty: it retrieves the molecules but results do not pop up in *results summary* and *molecules properties* sections, as well as the molecules visualization doesn't adjust to selection criteria in *examples of molecules*. 
So, your task is to fix it! 

You need to implement the functions computing statistics on each molecule property (there are 8 of them in `src/project_web/molecules_properties/` folder), as well as the function that performs selection of molecules for visualization given a criteria (`src/project_web/molecules_structures/select_structures.py`). 
As soon as the correctly implemented functionality is there, the corresponding object will pop up on the dashboard, so you don't need to worry about implementing this part. 
You can implement as many as you want or focus on few and customize them. 

If you carefully follow all the instructions and steps, as well as the docstring descriptions and hints in the code, you should obtain the following result [minimum_example](./dashboard_examples/example_min.pdf) after implementing all the functions. 
With partial implementation, missing plots will appear as blank area on the dashboard. 
If you feel confident, you also can customize the plots as you like them, for example: [here](./dashboard_examples/example_custom.pdf).

**Important:** You don't need any experience with web app development or any knowledge of REST API and Plotly Dash to succeed with this task. 
All the implementations are few lines of code performing iterations over the list with molecules data.

## Project directory

The source code for the app is located in `src/` folder.
File `app.py` is analoguos to `main.py` and running it starts the server. 
All the web layouts and callback logics are located at `src/project_web`.

 - `src/project_web/assets` - CSS files, images and other auxiliary files
 - `src/project_web/chembl_search` - functionality performing API calls to ChEMBL DB
 - `src/project_web/components` - HTML components for core layout, molecules properties, molecules_strucures and results table visualization
 - `src/project_web/molecule_properties` - functionality that extracts molecules properties from raw data
 - `src/project_web/molecule_structures` - functionality that extracts molecule structures.

## Preparation for the project

1. Form a team of ~8-10 people and choose a person who will be a "Project Leader". This person will be maintaining the repository with the code, do informal "code review" and merge all the created branches with changes at the end.

2. The Project lead should fork the code from HERE to his own repository. This step is important to make sure that you get your own result that will be different from other teams and to avoid conflicts between the same branches from other teams.

3. Clone the code from the repo of your Project lead (NOT THE ORIGINAL ONE) to your local machine: 

   `git clone <LINK_TO_THE_FORKED_REPO>`

   The code you create will have to be committed also into the forked repo.

## Creating environment and installing required packages

1. On your local machine, create virtual environment for the project and activate it:

   `conda create -n <ENV_NAME> python=3.9`

   `conda activate <ENV_NAME>`

2. Go to the cloned project directory and install required packages:

   `pip install -r requirements.txt`

3. To make sure everything is installed properly, got to `src` run the server:

   `python app.py`

4. In your browser, type in the address line: `localhost:8053`. If everything works well, you will see the framework of the dashboard. Try querying the ChEMBL DB with the following prompt: SMILES `COC(=O)c1ccc(CBr)cc1` and similarity 50. You should see the response "Found 54 molecules" and visualization of those molecules.


## Developing new features

In order to populate dashboard with the content, you need to implement functionality given in `src/project_web/molecules_properties/` directory. 
Each of the files there corresponds to a molecule property: aLogP, number of aromatic rings, number of H-bond acceptors (HBA) and donors (HBD), molecule weight, polar surface area (PSA), number of "rule of five" violations (RO5) and Tanimoto similarity w.r.t. the input molecule. 
You need to complete function `get_data()` in each of the files. 
If you have time, you can also modify function `draw_component()` in the same file to style your plot as you like it. 
Use [Plotly docs](https://plotly.com/python/) for reference. 

More advanced task includes implementation of selection function that sorts out the molecules for visualization every time you move the sliders in *examples of molecules* section. 
This is located in `src/molecules_structures/select_structures.py`. 

Keep in mind, you need only implement the body of the function, following description in the docstrings. 
DO NOT change the signature or name of the function! 
DO NOT change other files! 

**Communicate within your team to distribute the tasks and make sure each of you implements different functionality to avoid conflicts when merge the results.**

### Creating your own branch for the feature

After you assigned the tasks

1. Create a local branch in the project with a unique name. Usually, branches are named to reflect the features, additional functionalities, or issues fixes that they contain:

   `git checkout -b <BRANCH_NAME>`

2. Make sure you are working in the correct branch:

   `git branch`

3. Modify your part of the code: follow the hints in the docstrings and methods description, debug and test it locally.

4. See your modifications in browser locally (run server with `python app.py`). If everything is done correct, you will be able to see your implemented functionality in the dashboard. 

5. Check the changes in the project directory (should show the files you modified):

   `git status`

6. Add and commit the files you changed:

   `git add <CHANGED_FILE>`

   `git commit -m "Implemented <NAME_OF_THE_FUNCTION>`

7. Push the changes to the forked project:

   `git push origin <BRANCH_NAME>`

8. If you are a project lead, make sure to merge all the branches created by team members to the `main` branch. 

### Checking final product:

To see all the changes done by your teammates, pull the updated code from `main` branch after you pushed your own code and you branch has been merged:

   `git pull origin main`

## Finally...

The goal of this project is not coding with python but rather to give you a sense of collaborative development that you will often encounter in industry or large scientific teams. 
Oftentimes, when you join a new team, there is already established development process and the software that has been maintained by different people over time.
It is quite rare that you start your own project that is not connected to any other projects already existing in the team. 
Therefore, with this project, we recommend you to focus on understanding the whole workflow and making sure it works well at the end, rather than on writing perfect python code. 

Good luck!