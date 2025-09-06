{% macro print_fact_sales() %}
  {% set query %}
    select * from {{ ref('fact_sales') }}
  {% endset %}
  {{ return(query) }}
{% endmacro %}
