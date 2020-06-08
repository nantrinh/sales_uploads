## Dependencies

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## How to run

- `docker-compose up -d --build`
- Navigate to `http://localhost:3000/`

## Demo

![](https://i.imgur.com/VsEK51P.gif)

<blockquote class="imgur-embed-pub" lang="en" data-id="VsEK51P"><a href="//imgur.com/VsEK51P"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>
Note: File explorer opens up in another window when the "Choose File" button is clicked.

Run `./connect-to-db.sh` to connect to the PostgreSQL database.
Run `SELECT * FROM sales;` to view the inserted rows.

Sample data:
![](https://i.imgur.com/EQG8GNP.png)

## TODOs and considerations

- Authentication
- Tests
- Backend
  - Use environment variables for the database params
  - Use configs for development, production, and testing
  - Check the content-length before reading into memory; multi-threading may be desirable to process large files
- Frontend
  - Can do some validation before sending the request to the backend, for example, are all the required fields present

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
