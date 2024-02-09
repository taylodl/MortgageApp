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

## UI Tier Tech Stack ##
**Context:** Technology to be used for building the UI tier.  
**Decision:** Python Flask will be used to build the UI tier.  
**Rationale:** It's a POC and we don't have to explicitly run a web server.  
**Consequence:** We'll be using Jinga2 scripting in HTML files. This feels an awful like like PHP programming.  
**Date:** Feb 7, 2024  

## Data Tier Tech Stack ##
**Context:** Technology to be used for building the data tier.  
**Decision:** The data tier will be accessed via a service. This allows us to change the actual implementation to use whatever backing store we desire. In the POC we'll be using memcached.  
**Rationale:** We're planning on migrating this to Kubernetes anyway. We can deal with data volumes and all that stuff then. This gets the interfaces defined so we can proceed with the implementation and we do get caching.  
**Consequence:** This is work we were going to have to address when we migrated to Kubernetes, but by utilizing a service interface it will only be this container (pod) that's affected.  
**Date:** Feb 8, 2024




