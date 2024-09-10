{% test is_unique(model, column_name) %}

with validation as (

    select
        {{ column_name }} as unique_column,
        ROW_NUMBER() over (PARTITION BY {{ column_name }}) as column_row_num

    from {{ model }}

),

validation_errors as (

    select
        unique_column

    from validation
    -- if this is true, then even_field is actually odd!
    where column_row_num > 1

)

select *
from validation_errors

{% endtest %}