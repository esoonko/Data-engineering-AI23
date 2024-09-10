{{ config(materialized='view') }}

SELECT modified_timestamp,
JSON_VALUE(data.chance_of_rain) as chance_of_rain,
JSON_VALUE(data.chance_of_snow) AS chance_of_snow,
JSON_VALUE(data.cloud) AS cloud,
JSON_VALUE(data.condition.text) AS condition,
JSON_VALUE(data.dewpoint_c) AS dewpoint_c,
JSON_VALUE(data.feelslike_c) AS feelslike_c,
JSON_VALUE(data.gust_kph) AS gust_kph,
JSON_VALUE(data.heatindex_c) AS heatindex_c,
JSON_VALUE(data.humidity) AS humidity,
JSON_VALUE(data.precip_mm) AS precip_mm,
JSON_VALUE(data.temp_c) as temp_c,
JSON_VALUE(data.`time`) as temp_time,
JSON_VALUE(data.wind_kph) as wind_kph
FROM {{ source('de_ai23_project','_src_weather_stockholm') }}
WHERE 1=1 -- Needed for qualify
QUALIFY ROW_NUMBER() OVER (PARTITION BY temp_time ORDER BY MODIFIED_TIMESTAMP DESC) = 1


