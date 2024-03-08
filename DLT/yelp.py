import dlt
from dlt.sources.helpers import requests


@dlt.source
def yelp_source(api_secret_key=dlt.secrets.value):
    return yelp_resource(api_secret_key)


def _create_auth_headers(api_secret_key):
    headers = {"Authorization": f"Bearer {api_secret_key}"}
    return headers


@dlt.resource(write_disposition="replace")
def yelp_resource(api_secret_key=dlt.secrets.value):
    headers = _create_auth_headers(api_secret_key)
    url = "https://api.yelp.com/v3/businesses/search"

    params = {
        "term": "taxi services",
        "location": "NYC",
        "limit": 50  # Maximum allowed by Yelp
    }

    page = 0
    max_offset = 950  

    while True:
        params['offset'] = page * 50
        if params['offset'] > max_offset:
            break  # Stop retrieving results once we hit the offset limit

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error if Yelp returns an error code

        data = response.json()

        
        if 'total' in data and page * 50 >= data['total']:  
            break  # We've reached the maximum number of results

        if not data['businesses']:  # Handle case of no more results in this page
            break  

        yield data  
        page += 1


# configure the pipeline with your destination details
pipeline = dlt.pipeline(
    pipeline_name='yelp', 
    destination='postgres', 
    dataset_name='yelp_data'
)

# print credentials by running the resource
data = list(yelp_resource())

# print the data yielded from resource
print(data)

# run the pipeline with your parameters
load_info = pipeline.run(yelp_source())

# pretty print the information on data that was loaded
print(load_info)
