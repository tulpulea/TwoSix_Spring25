# TwoSix_Spring25
CMSE 495 group project for "Analyzing Public Feedback on Environmental Policies Using Natural Language Processing" for Two Six

## Contributors

- [Archan Tulpule](https://github.com/tulpulea)

### Some notes for this branch
- currently working on trying to unify database creation with modeling
- hence why this branch was sourced on scraping
- Some actions I'm taking:
    1) Updating env file: environment.yml was updated with specfic dependencies and more chromadb, removing unnecessary packages
    2) Implementing the database creation - potentially updating 
    scripts to also take care of seperate collection for policies
        - Approach: As per the documentation, the Regulations.gov API allows
                    result page size to be in [5,250] and the page number
                    to be in [1,20]. This implies the algorithm will do the following:
                    - first search for comments by "climate"
                    - iterate through the N pages of comments, saving document id and comment id
                    - then search for documents leveraging document id, saving data
                    - search for comment strings, leveraging comment ids, saving data
                    
            
    3) Deciciding and implementing embeddings models & processes
    4) Setting up chromadb to store embeddings 
    5) Facilitating further modeling & visualization
