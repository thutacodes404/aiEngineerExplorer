collection = client.get_collection(
  name="netflix_titles",


reference_texts = ["children's story about a car", "lions"]

# Query two results using reference_texts
result = collection.query(

    query_texts=reference_texts,
    n_results=2,
)
  # Filter for titles with a G rating released before 2019
    where={
       "$and":{
            "rating": {"$eq": "G"},
            "release_year": {"$lt": 2019}
       }
    }

