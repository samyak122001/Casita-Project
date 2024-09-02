# La Casita's Menu Generator

I created this random menu generator to make weekly meal planning easier! 

## Overview
This Menu Generator is a tool that automates the creation of weekly menus, providing users with detailed ingredient lists with precise quantities and an estimate of the grocery bill. 
The goal is to facilitate meal planning with a focus on time-savings and cost-efficiency. 
Currently, the project includes functionality for generating menus and ingredient lists, with cost estimation features as a work in progress.

Here's a short description of what's in here:

### `recipe_class.py`
This Python file defines a `Recipe` class that is used to represent a recipe object (OOP) with attributes for name, ingredients, and servings. It includes a constructor and a representation method to print the recipe name.

### `recipes.txt`
A JSON-formatted file that stores a collection of recipes. Each recipe is categorized by meal type (e.g., Breakfast, Lunch) and includes details such as ingredients, quantities, and servings. This file serves as a database for the application, from which meal plans can be generated.

### `prices.txt`
A Python file that establishes a dictionary mapping ingredient names to their respective prices. This is presumably used to calculate the cost of recipes based on the ingredients used. THIS IS WORK IN PROGRESS :)

### `generate_menu.ipynb`
Processes recipes to create weekly menus, including functionality to handle recipes with components like carbs or vegetables, ensuring flexibility in menu creation.

### `generate_list.ipynb`
This notebook focuses on generating detailed ingredient lists from the selected recipes for the weekly menu. 

###`main.ipynb`
The makeshif "UI". Acts as the starting point for users interacting with the Menu Generator project. It introduces the application and may guide users through the process of generating a menu.

### `recipe_entry.ipynb`
Provides a mechanism for adding new recipes into the system, ensuring they are correctly formatted and integrated into the application's recipe database.

### `generate_data.ipynb`
Provides the logic to add and remove recipes from the recipes.txt (DB).

### `generate_excel.ipynb` 
Provides logic to export the menu and its respective ingredients list into an excel file.

### `generate_html.ipynb`
Exports to HTML (work in progress)


## Installation

### Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package installer)
- Jupyter Notebook or JupyterLab
- 

## Running the Application

After installing the project follow these steps to start using the Menu Generator:

1. **Boot Jupyter Lab**: Open a terminal and run the following command:
`jupyter lab`

2. **Open `main.ipynb` Notebook**: In the Jupyter interface, navigate to and open the `main.ipynb` notebook. This notebook serves as the entry point to the Menu Generator.

3. **Restart Kernel and Run All Cells**: To ensure the application runs smoothly, it's a good practice to restart the kernel and run all cells:
   - In Jupyter Notebook: Go to the menu bar, select `Kernel` > `Restart & Run All`.
   - In JupyterLab: Go to the menu bar, select `Kernel` > `Restart Kernel and Run All Cells...`.

4. **Follow the Instructions**: The `main.ipynb` notebook will guide you through generating menus, adding recipes, and utilizing other features provided by the Menu Generator. Follow the prompts and instructions within the notebook to explore its capabilities.

By following these steps, you'll be able to fully utilize the Menu Generator to create weekly menus, generate shopping lists, and estimate grocery expenses. Have fun! :)

**THIS IS WORK IN PROGRESS**
