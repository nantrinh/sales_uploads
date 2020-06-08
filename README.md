# Sales Uploads

A simple application that allows users to upload CSVs of sales.

Built with a React frontend, Flask API, and PostgreSQL database.

Each component is containerized and Docker-Compose is used to orchestrate the containers.

See [`backend/test_api.py`](https://github.com/nantrinh/sales_uploads/blob/master/backend/test_api.py) for a test of the API functionality.

## Demo

<img src="https://i.imgur.com/VsEK51P.gif" width="600">

Note: File explorer opens up in another window when the "Choose File" button is clicked.

- Run `./connect-to-db.sh` to connect to the PostgreSQL database.
- Run `SELECT * FROM sales;` to view the inserted rows.

Sample data:
![](https://i.imgur.com/EQG8GNP.png)

## Dependencies

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## How to run

- `docker-compose up -d --build`
- Navigate to `http://localhost:3000/`

File constraints:

- The file must be a CSV.
- The columns must be in this order: Customer Name, Item Description, Item Price, Quantity, Merchant Name, Merchant Address
- The first line in the CSV is assumed to be the header and discarded in parsing.

## TODOs and considerations

- Authentication
- More tests
- Stream the download on the server side
- Backend
  - Use environment variables for the database params
  - Use configs for development, production, and testing
  - Be more flexible about column order (don't assume the columns are ordered a certain way, and do not assume all of the columns are there)
  - Be more flexible about addresses (state, country, zip)
  - Handle commas in merchant names or descriptions
- Database
  - Is 250 chars enough for descriptions, merchant names, etc?
  - Impose limits on price and quantity values?
- Frontend
  - Can do some validation before sending the request to the backend, for example, are all the required fields present
  - Can restrict to csv files only
  - Display revenue with commas

## Scaling Up

- Consider another framework for the backend with better performance (e.g., [FastAPI](https://fastapi.tiangolo.com/), [Starlette](https://www.starlette.io/))
- Consider using Go instead for the backend
- To scale up writes to the database:
  - Consider using another data store, for example Cassandra. Clients can connect to any node and issue writes to that node. Each node knows which of the other nodes are responsible for certain subsets of the data, so it can forward the writes to the appropriate nodes. Quorums can be used for consistent writes and reads.
    - Benefits:
      - Automatic data partitioning and replication
      - Horizontally scalable
      - Easier to replace failed nodes
      - Fast writes (append-only data structures)
    - Drawbacks:
      - Schema might have to be enforced on the application side
      - Deletes can be very expensive
  - Consider treating each sale as an event and write them to an append-only log, such as Kafka.
    - Benefits:
      - Fast writes
      - Horizontally scalable (more partitions)
      - If you have use cases in the future that require querying or working with the data in multiple formats, you can set up multiple data stores to ingest the data from the topics and stay updated as new data comes in. You get the flexibility of working with data in the formats you require, and you're not overloading the database with queries.
    - Drawbacks:
      - Can be more complex to set up and maintain
