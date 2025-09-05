# Guide to Using dbt Power User Extension in VS Code

This guide will teach you how to use the dbt Power User extension in VS Code from start to end, including installation, setup, and running your dbt models to view data.

## Step 1: Install the dbt Power User Extension

1. Open VS Code.
2. Go to the Extensions view by clicking the Extensions icon in the sidebar (or press `Ctrl+Shift+X`).
3. Search for "dbt Power User".
4. Click on the extension by "innoverio" and click "Install".
5. Wait for the installation to complete.

## Step 2: Set Up the Extension

1. After installation, you may need to reload VS Code (click the reload button if prompted).
2. The extension will automatically detect your dbt project if it's open in VS Code.
3. If not, open your dbt project folder in VS Code (File > Open Folder > select your akash_dbt_project folder).

## Step 3: Configure dbt Profile

1. The extension uses your existing dbt profiles.yml file.
2. Make sure your profiles.yml is correctly configured for Databricks (as in your project).
3. If needed, you can set the dbt profile in VS Code settings:
   - Open VS Code settings (File > Preferences > Settings).
   - Search for "dbt" and look for dbt Power User settings.
   - Set the profile name if different from default.

## Step 4: Explore Your dbt Project

1. In the VS Code sidebar, you should see a new "dbt Power User" section.
2. It will show your models, sources, tests, etc.
3. Click on "Models" to see your fact_sales.sql model.

## Step 5: Run Your dbt Model

1. Right-click on the fact_sales.sql file in the Explorer or in the dbt Power User panel.
2. Select "dbt Power User: Run Model" from the context menu.
3. Alternatively, use the command palette:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac).
   - Type "dbt Power User: Run Model" and select it.
4. Choose the target (e.g., dev) if prompted.
5. The extension will run `dbt run --models fact_sales` in the terminal.

## Step 6: View the Model Data

1. After the model runs successfully, right-click on fact_sales.sql again.
2. Select "dbt Power User: Show Model Data" or "dbt Power User: Preview Model".
3. This will execute a `SELECT * FROM your_model` query and display the results in a new tab.
4. You can also use "dbt Power User: Compile and Show SQL" to see the compiled SQL.

## Step 7: Run Tests

1. To run tests on your model:
   - Right-click on fact_sales.sql.
   - Select "dbt Power User: Run Tests".
2. This will run all tests associated with the model.

## Step 8: Additional Features

- **Lineage Graph**: View the lineage of your models by clicking on the lineage icon in the dbt Power User panel.
- **Documentation**: Generate and view dbt docs by running "dbt Power User: Generate Docs".
- **Debug**: Use "dbt Power User: Debug" to check your dbt setup.

## Troubleshooting

- If the extension doesn't detect your project, ensure your dbt_project.yml is in the root of the opened folder.
- Make sure your Python environment has dbt installed and is activated.
- Check the terminal output for any errors during runs.

## Example Workflow

1. Open akash_dbt_project in VS Code.
2. Right-click on models/fact_sales.sql.
3. Select "dbt Power User: Run Model".
4. Wait for it to complete.
5. Right-click again and select "dbt Power User: Show Model Data".
6. View the data in the results tab.

This guide covers the basics to get you started with viewing your fact_sales data using the dbt Power User extension.
