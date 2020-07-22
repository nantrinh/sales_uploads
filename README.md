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
