{{ config(
    materialized='incremental',
    unique_key='github_username'
 ) }}
 

 -- What if data is split across two runs
/* Switch your model back to using just the most recent run time (i.e. remove the date_add function), and add a new record to the form.
Then rerun your model. For your record, how many events is it currently counting? Is that right?
When I do this, I see only one event being counted, because my where clause only gives me the events since my last run.
No matter where we put our cutoff line, we run the risk of splitting data into two that needs to be grouped together.
We can use some modeling strategies to overcome this, like finding all the events that are associated with that user:
*/

 with events as (
    select * from {{ source('advanced_dbt_examples', 'form_events') }}
    {% if is_incremental() %}
    where github_username in (
        select distinct github_username from {{ source('advanced_dbt_examples', 'form_events') }}
        where timestamp >= (select max(last_form_entry) from {{ this }})
    )
    {% endif %}
 ),

aggregated as (
    select
        github_username,
        min(timestamp) as first_form_entry,
        max(timestamp) as last_form_entry,
        count(*) as number_of_entries
    from events
    group by 1
 )
 
select * from aggregated