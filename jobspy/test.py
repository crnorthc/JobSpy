from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["linkedin"],
    search_term="software engineer",
    location="Palo Alto, CA",
    distance=20,
    results_wanted=2,
    hours_old=24,
    offset=0,
    country_indeed="USA",
    linkedin_fetch_description=True,
)

jobs = jobs.drop(
    columns=[
        "job_type",
        "salary_source",
        "job_level",
        "job_function",
        "listing_type",
        "emails",
        "company_industry",
        "company_url",
        "company_logo",
        "company_url_direct",
        "company_addresses",
        "company_revenue",
        "skills",
        "experience_range",
        "company_rating",
        "company_reviews_count",
        "vacancy_count",
        "work_from_home_type",
    ]
)

records = jobs.to_dict(orient="records")

print(records[0])
