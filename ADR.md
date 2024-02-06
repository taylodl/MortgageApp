# MortgageApp Architecture Decision Record

## Simplified Local Development for POC - Docker Compose ##
**Context:** Client desires final delivered application to run in a Kubernetes environment so it will run anywhere they need it to.  
**Decision:** Since this is a POC that we want to be able to deliver to the client and have them to be able to easily run it, we'll deliver the POC using Docker Compose.  
**Rationale:** The application will still be containerized, having the exact same UI and API containers that will be K8S pods. The POC can be easily transitioned to K8S later.  
**Consequences:** The data tier will have a proper interface. That allows us to change the implementation of the data tier to etcd when we deploy to K8S without having to change the UI or API tiers. Depending on the data tier maintaining the same interface across deployments.  
**Date:** Feb 6, 2024


## API Tier Tech Stack ##
**Context:** Technology to be used for building the API tier.  
**Decision:** Python Flask will be used to build the API tier.  
**Rationale:** The client has staff proficient in Python. It's their preferred language.  
**Consequences:** Python will require more infrastructure should this scale-out as Python is not as efficient of a language. Client doesn't expect that to be a problem.  
**Date:** Feb 6, 2024


