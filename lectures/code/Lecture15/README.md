# DBT Coding example
This DBT Coding example follows somewhat the guide that is available online: https://docs.getdbt.com/guides/manual-install?step=1

1. Create a new venv through python -m venv venv
2. Install dbt-core and dbt-bigquery packages
`pip install dbt-core` and `pip install dbt-bigquery`
3. Check you have dbt installed through `dbt --version`
It should show Core as installed with bigquery as Plugin.
4. Create a dbt project through `dbt init <project-name>`
6. Create a profiles.yml and adjust information according to the layout given here: https://docs.getdbt.com/guides/manual-install?step=4
5. Check connection to your project through `dbt debug`.
- Remember to update Google ADC through `gcloud auth application-default login`

